import xml.etree.ElementTree as xml
from time import gmtime, strftime

from FTP_connection.transfer import *
from XML.create_XML import create_XML
from XML.preview_html import preview_html
from collecting_data.collect_data_from_sites import collect_data_from_sites
from collecting_data.collect_data_oyo import collect_data_oyo
from imgs_processing.download_imgs_and_replace_links import download_imgs_and_replace_links

if __name__ == '__main__':
    """ HARD CODE ALERT """
    products = """NB-AS-A009	ASUS NB ExpertBook P2540FA-DM0561R i3-1011U 15.6 FHD 8GB DDR4 256GB Intel® UHD 3Y OnSite Win10Pro 90NX02L1-M07240	4718017950534	9999	None	Matrix	https://sklepasus.pl/laptopy-i-notebooki/asus-p2540fa-dm0561r-i3-10110u-15-6i-8gb
NB-AS-A010	ASUS NB ExpertBook P2540FA-DM0561T i3-1011U 15.6 FHD 8GB DDR4 256GB Intel® UHD 3Y OnSite Win10H 90NX02L1-M07130	4718017950541	9999	None	Matrix	https://sklepasus.pl/laptopy-i-notebooki/asus-expertbook-p2-p2450-p2540fa-dm0561t
NB-AS-A011	ASUS NB ExpertBook P2540FA-DM0562R i5-10210U 15.6 FHD 8GB DDR4 256GB Intel® UHD 3Y OnSite Win10Pro 90NX02L1-M07140	4718017950572	9999	None	Matrix	https://sklepasus.pl/laptopy-i-notebooki/asus-expertbook-p2-p2450-p2540fa-dm0562r
NB-AS-A012	ASUS NB ExpertBook P2451FA-EB0116R i3-10110U 14.0 FHD 8GB DDR4 256GB Intel® UHD 3Y OnSite Win10Pro 90NX02N1-M01380	4718017850315	9999	None	Matrix	https://sklepasus.pl/laptopy-i-notebooki/asus-expertbook-p2-p2451
NB-AS-A013	ASUS NB ExpertBook P2451FB-EB0018R i5-10210U 14.0 FHD 8GB DDR4 256GB GeForce MX110 3Y OnSite Win10Pro 90NX02P1-M00300	4718017857239	9999	None	Matrix	https://sklepasus.pl/laptopy-i-notebooki/asus-expertbook-p2-p2451-1
NB-AS-A014	ASUS NB ExpertBook P2540FA-DM0562T i5-10210U 15.6 FHD 8GB DDR4 256GB Intel® UHD 3Y OnSite Win10H 90NX02L1-M07660	4718017950565	9999	None	Matrix	https://sklepasus.pl/laptopy-i-notebooki/asus-expertbook-p2-p2450-p2540fa-dm0562t""".split('\n')

    send_via_FTP = True
    print_result = True
    yes_to_all = False
    """ HARD CODE ALERT """

    # define an XML file to write products data inside
    root = xml.Element('Products')
    tree = None
    passed = []
    for product in products:  # quantitiy of products to add
        # (1) gather all necessary data on your own (oyo)
        full_product = collect_data_oyo(product.split('\t'))

        # (2) gather all necessary data from given page(s)
        collect_data_from_sites(full_product)

        # (3) preview description
        if preview_html(full_product['descriptions'][0], full_product['sku'], yes_to_all) == -1:
            passed.append(full_product['sku'])
            continue

        # (4) download imgs from description and replace links
        download_imgs_and_replace_links(full_product)

        # (5) create XML out of collected data
        tree = create_XML(root, full_product)

        if print_result:
            print(full_product["descriptions"][0])
            print('=' * 15)
            print(full_product["descriptions"][1])
            print('=' * 15)
            print(full_product["descriptions"][2])

    if send_via_FTP and tree is not None:
        xml_file_name = f'Products_{strftime("%Y%m%d%H%M%S", gmtime())}.xml'

        with open(f'bin\\{xml_file_name}', 'wb') as file:
            tree.write(file)

        folders = [folder for folder in os.listdir('bin') if
                   not folder.endswith('.xml') and len(folder.split(' - ')) == 2]

        for folder in folders:
            f = folder.split(' - ')
            FTP = make_FTP_connection()
            send_description_imgs_via_FTP(FTP, f[0], f[1])  # send description images via FTP
            send_products_imgs_via_FTP(FTP, folder)  # send product images via FTP
            send_XML_via_FTP(FTP, xml_file_name)  # send XML via FTP
            close_FTP_connection(FTP)

    print(f'Opuszczono: ')
    [print(f"{i}. {ele}") for i, ele in enumerate(passed)] if passed else print('Wszystkie produkty zostały dodane')
