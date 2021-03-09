import xml.etree.ElementTree as xml
from time import gmtime, strftime
import os

from FTP_connection.transfer import *
from XML.create_XML import create_XML
from collect_data_from_sites import collect_data_from_sites
from collect_data_oyo import collect_data_oyo
from imgs_processing.download_imgs_and_replace_links import download_imgs_and_replace_links

if __name__ == '__main__':
    """ HARD CODE ALERT """
    # products = [''].split(\t)
    products = [['TEST', 'Samsung Próba generalna', '1234567891234', '9999', 'SAM_AKC', 'Matrix',
                 'https://www.samsung.com/pl/lifestyle-tvs/the-sero/ls05t-43-inch-the-sero-4k-smart-tv-navy-blue-qe43ls05tauxxh/']]
    """ HARD CODE ALERT """

    # define an XML file to write products data inside
    root = xml.Element('Products')
    tree = None
    for product in products:  # quantitiy of products to add
        # (1) gather all necessary data on your own (oyo)
        full_product = collect_data_oyo(product)

        # (3) gather all necessary data from given page(s)
        collect_data_from_sites(full_product)

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
