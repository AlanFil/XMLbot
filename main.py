import xml.etree.ElementTree as xml
from time import gmtime, strftime
import os

from FTP_connection.transfer import *
from XML.create_XML import create_XML
from collect_data import collect_data

from globals import STARTING_DIRECTORY


def create_product_folder(product_folder_name):
    pr_folder_path = f'{STARTING_DIRECTORY}\\bin\\{product_folder_name}'
    try:
        os.mkdir(pr_folder_path)
        os.mkdir(f'{pr_folder_path}\\product_imgs')
        os.mkdir(f'{pr_folder_path}\\description_imgs')
    except FileExistsError:
        print(f'Folder "{product_folder_name}" already exists in bin.')
        # return -1

    return pr_folder_path


if __name__ == '__main__':
    root = xml.Element('Products')
    tree = None
    adding_products = []
    for i in range(2):  # quantitiy of products to add
        # (1) gather all necessary data (description images, product images and for XML file)
        full_product = collect_data(i)

        # (2) create folder with product data (for description images, product images and XML file)
        product_folder_path = create_product_folder(full_product['product_folder_name_in'])

        # (3) create XML out of collected data

        tree = create_XML(root, full_product['product_folder_name_in'], full_product['product_in'],
                          full_product['descriptions_in'], full_product['weight_in'], full_product['manufacturer_in'],
                          full_product['pickup_store_in'], full_product['imgs_in'], full_product['ceneo_link_in'])

    if tree is not None:
        xml_file_name = f'Products_{strftime("%Y%m%d%H%M%S", gmtime())}.xml'

        with open(f'bin\\{xml_file_name}', 'wb') as file:
            tree.write(file)

        folders = [folder for folder in os.listdir('bin') if not folder.endswith('.xml') and len(folder.split(' - ')) == 2]
        for folder in folders:
            f = folder.split(' - ')
            FTP = make_FTP_connection()
            send_description_imgs_via_FTP(FTP, f[0], f[1])  # send description images via FTP
            send_products_imgs_via_FTP(FTP, folder)  # send product images via FTP
            send_XML_via_FTP(FTP, xml_file_name)  # send XML via FTP
            close_FTP_connection(FTP)
