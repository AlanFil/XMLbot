import xml.etree.ElementTree as xml
from time import gmtime, strftime
import os

from FTP_connection.transfer import *
from XML.create_XML import create_XML
from XML.preview_html import preview_html
from collect_data_from_sites import collect_data_from_sites
from collect_data_oyo import collect_data_oyo
from imgs_processing.download_imgs_and_replace_links import download_imgs_and_replace_links

if __name__ == '__main__':
    """ HARD CODE ALERT """
    products = """QE65QN800ATXXH	TVC SAMSUNG QE65QN800ATXXH	8 806 092 024 922	9999	SAM_RTV	Matrix	https://www.samsung.com/pl/tvs/qled-tv/qn800a-65-inch-neo-qled-8k-smart-tv-qe65qn800atxxh/
QE65QN85AATXXH	TVC SAMSUNG QE65QN85AATXXH	8 806 092 024 939	9999	SAM_RTV	Matrix	https://www.samsung.com/pl/tvs/qled-tv/qn85a-65-inch-neo-qled-4k-smart-tv-qe65qn85aatxxh/
QE65QN91AATXXH	TVC SAMSUNG QE65QN91AATXXH	8 806 092 036 253	9999	SAM_RTV	Matrix	https://www.samsung.com/pl/tvs/qled-tv/qn90a-65-inch-neo-qled-4k-smart-tv-qe65qn91aatxxh/
QE75QN800ATXXH	TVC SAMSUNG QE75QN800ATXXH	8 806 092 024 960	9999	SAM_RTV	Matrix	https://www.samsung.com/pl/tvs/qled-tv/qn800a-75-inch-neo-qled-8k-smart-tv-qe75qn800atxxh/
QE75QN85AATXXH	TVC SAMSUNG QE75QN85AATXXH	8 806 092 024 984	9999	SAM_RTV	Matrix	https://www.samsung.com/pl/tvs/qled-tv/qn85a-75-inch-neo-qled-4k-smart-tv-qe75qn85aatxxh/
QE75QN91AATXXH	TVC SAMSUNG QE75QN91AATXXH	8 806 092 036 307	9999	SAM_RTV	Matrix	https://www.samsung.com/pl/tvs/qled-tv/qn90a-75-inch-neo-qled-4k-smart-tv-qe75qn91aatxxh/""".split('\n')
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

    print(f'Opuszczono: {[print(f"{i}. {ele}") for i, ele in enumerate(passed)]}') if passed else print('Wszystkie produkty zostały dodane')
