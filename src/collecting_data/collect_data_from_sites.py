import os

from src.globals import STARTING_DIRECTORY, timeit
from src.sites.LG import lg_manage
from src.sites.ab import ab_manage
from src.sites.allegro import allegro_manage
from src.sites.blaupunkt import blaupunkt_manage
from src.sites.bosch import bosch_manage
from src.sites.cqe import cqe_manage
from src.sites.garett import garett_manage
from src.sites.graef import graef_manage
from src.sites.huawei import huawei_manage
from src.sites.huzaro import huzaro_manage
from src.sites.krysiak import krysiak_manage
from src.sites.mptech import mptech_manage
from src.sites.philips_hue import philips_hue_manage
from src.sites.rcpro import dji_manage
from src.sites.samsung import samsung_manage
from src.sites.scentre import scentre_manage
from src.sites.sharp import sharp_manage
from src.sites.sklepasus import sklep_asus_manage
from src.sites.swiss import swiss_manage


def create_product_folder(product_folder_name):
    product_folder_name = f'{STARTING_DIRECTORY}\\bin\\{product_folder_name}'
    try:
        os.mkdir(product_folder_name)
        os.mkdir(f'{product_folder_name}\\product_imgs')
        os.mkdir(f'{product_folder_name}\\product_imgs_raw')
        os.mkdir(f'{product_folder_name}\\description_imgs')
    except FileExistsError:
        print(f'INFO: Folder "{product_folder_name}" already exists in bin.')


@timeit
def collect_data_from_sites(full_product):
    if 'samsung.com' in full_product['link'].lower():
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

    elif 'philips-hue.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Philips_HUE' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        philips_hue_manage(full_product)

    elif 'sklepasus' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'ASUS' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        sklep_asus_manage(full_product)

    elif 'garett.com' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'GARETT' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        garett_manage(full_product)

    elif '2' in full_product['supplier'] and full_product['link'].strip() == '':  # AB
        full_product['product_folder_name_in'] = 'Bosch' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        ab_manage(full_product)

    elif 'bosch' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Bosch' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        bosch_manage(full_product)

    elif 'lg.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'LG' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        lg_manage(full_product)

    elif 'huzaro.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Huzaro' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        huzaro_manage(full_product)

    elif 'huawei.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Huawei' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        huawei_manage(full_product)

    elif '4swiss.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = '4swiss' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        swiss_manage(full_product)

    elif 'allegro.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Tenzi' + full_product['product_folder_name_in']
        create_product_folder(full_product['product_folder_name_in'])
        allegro_manage(full_product)

    else:
        print('WARNING: There was no scrapping function found')
