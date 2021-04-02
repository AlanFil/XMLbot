import os

from globals import STARTING_DIRECTORY
from sites.blaupunkt import blaupunkt_manage
from sites.cqe import cqe_manage
from sites.graef import graef_manage
from sites.krysiak import krysiak_manage
from sites.mptech import mptech_manage
from sites.rcpro import dji_manage
from sites.rtveuroagd import rtveuroagd_manage
from sites.samsung import samsung_manage
from sites.scentre import scentre_manage
from sites.sharp import sharp_manage


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
    if 'samsung.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Samsung' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        samsung_manage(full_product)

    elif 'rcpro.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'DJI' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        dji_manage(full_product)

    elif 'krysiak.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'KRYSIAK' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        krysiak_manage(full_product)

    elif 'scentre.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Sony' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        scentre_manage(full_product)

    elif 'mptech.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'myPhone' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        mptech_manage(full_product)

    elif 'graef.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Graef' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        graef_manage(full_product)

    elif 'sharphome.eu' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Sharp' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        sharp_manage(full_product)

    elif 'cqe.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'CQE' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        cqe_manage(full_product)

    elif 'blaupunkt.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Blaupunkt' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        blaupunkt_manage(full_product)

    else:
        print('Nie przypisano metody zbierania danych')
