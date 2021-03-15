from sites.dji import dji_manage
from sites.samsung import samsung_manage
from globals import STARTING_DIRECTORY
import os


def create_product_folder(product_folder_name):
    product_folder_name = f'{STARTING_DIRECTORY}\\bin\\{product_folder_name}'
    try:
        os.mkdir(product_folder_name)
        os.mkdir(f'{product_folder_name}\\product_imgs')
        os.mkdir(f'{product_folder_name}\\description_imgs')
    except FileExistsError:
        print(f'Folder "{product_folder_name}" already exists in bin.')
        # return -1


def collect_data_from_sites(full_product):
    if 'samsung' in full_product['name'].lower():
        full_product['product_folder_name_in'] = 'Samsung' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        samsung_manage(full_product)

    elif 'dji' in full_product['name'].lower():
        full_product['product_folder_name_in'] = 'DJI' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        dji_manage(full_product)

