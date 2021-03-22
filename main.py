import xml.etree.ElementTree as xml
from time import gmtime, strftime

from FTP_connection.transfer import *
from XML.create_XML import create_XML
from XML.preview_html import preview_html
from collect_data_from_sites import collect_data_from_sites
from collect_data_oyo import collect_data_oyo
from imgs_processing.download_imgs_and_replace_links import download_imgs_and_replace_links

if __name__ == '__main__':
    """ HARD CODE ALERT """
    products = """BAT_HEXPLORER	Bateria zewnętrzna do HAMMER Explorer	5902983609520	9999	MYPHONE	Matrix .xls	https://sklep.mptech.eu/akc000800.html
HBLADE3	Smartfon HAMMER Blade 3	5902983609490	9999	MYPHONE	Matrix .xls	https://sklep.mptech.eu/tel000560.html
HPROFBS21	Smartfon HAMMER Professional BS21 	5902983609254	9999	MYPHONE	Matrix .xls	https://sklep.mptech.eu/tel000539.html
HWATCH	Smartwatch HAMMER Watch	5902983610205	9999	MYPHONE	Matrix .xls	https://sklep.mptech.eu/tab000474.html
MYPHONEFUN6	Smartfon myPhone Fun 6 czarny	5902983608899	9999	MYPHONE	Matrix .xls	https://sklep.mptech.eu/sma002411.html
MYPHONENOW	Smartfon myPhone Now eSIM	5902983612193	9999	MYPHONE	Matrix .xls	https://sklep.mptech.eu/sma002503.html
MYPHONEHERED	Telefon myPhone Halo Easy czerwony 	5902052866625	9999	MYPHONE	Matrix	https://sklep.mptech.eu/Halo_Easy.html""".split('\n')
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
        if preview_html(full_product['descriptions'][0], full_product['sku']) == -1:
            passed.append(full_product['sku'])
            continue

        # (4) download imgs from description and replace links
        download_imgs_and_replace_links(full_product['product_folder_name_in'], full_product['descriptions'][0])

        # (5) create XML out of collected data
        tree = create_XML(root, full_product)

    if tree is not None:
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
