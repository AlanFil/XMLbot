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
    products = """""".split('\n')

    send_via_FTP = True
    print_result = False
    yes_to_all = True
    """ HARD CODE ALERT """

    # define an XML file to write products data inside
    root = xml.Element('Products')
    tree = None
    declined = []
    marked = []
    for product in products:
        # (1) gather all necessary data On Your Own (OYO)
        full_product = collect_data_oyo(product.split('\t'))
        print(f"=============== {full_product['name']} ===============")

        # (2) gather all necessary data from given page(s)
        collect_data_from_sites(full_product)

        # (3) preview description
        preview_result = preview_html(full_product, full_product['sku'], yes_to_all)
        if preview_result == -1:
            declined.append(full_product['sku'])
            continue
        elif preview_result == 1:
            marked.append(full_product['sku'])

        # (4) download imgs from description and replace links
        download_imgs_and_replace_links(full_product)

        # (5) create XML out of collected data
        tree = create_XML(root, full_product)

        if print_result:
            print('PRINTING SCRAPPED DESCRIPTIONS...')
            print(full_product["descriptions"][0])
            print('-' * 15)
            print(full_product["descriptions"][1])
            print('-' * 15)
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

    if marked:
        print(f'Marked by user: ')
        [print(f"{i}. {ele}") for i, ele in enumerate(marked)]

    if declined:
        print(f'Declined by user: ')
        [print(f"{i}. {ele}") for i, ele in enumerate(declined)]
    else:
        print('All products were added')
