import os

from globals import STARTING_DIRECTORY, timeit
from sites.LG import LGManage
from sites.ab import ABManage
from sites.blaupunkt import BlaupunktManage
from sites.bosch import BoschManage
from sites.cqe import CQEManage
from sites.garett import GarettManage
from sites.graef import GraefManage
from sites.krysiak import KrysiakManage
from sites.mptech import MptechManage
from sites.philips_hue import PhilipsHueManage
from sites.rcpro import DJIManage
from sites.samsung import SamsungManage
from sites.scentre import ScentreManage
from sites.sharp import SharpManage
from sites.sklepasus import SklepAsusManage


def CreateProductFolder(product_folder_name):
    product_folder_name = f'{STARTING_DIRECTORY}\\bin\\{product_folder_name}'
    try:
        os.mkdir(product_folder_name)
        os.mkdir(f'{product_folder_name}\\product_imgs')
        os.mkdir(f'{product_folder_name}\\product_imgs_raw')
        os.mkdir(f'{product_folder_name}\\description_imgs')
    except FileExistsError:
        print(f'INFO: Folder "{product_folder_name}" already exists in bin.')


@timeit
def CollectDataFromSites(full_product):
    if 'samsung.com' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Samsung' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        SamsungManage(full_product)

    elif 'rcpro.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'DJI' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        DJIManage(full_product)

    elif 'krysiak.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'KRYSIAK' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        KrysiakManage(full_product)

    elif 'scentre.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Sony' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        ScentreManage(full_product)

    elif 'mptech.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'myPhone' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        MptechManage(full_product)

    elif 'graef.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Graef' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        GraefManage(full_product)

    elif 'sharphome.eu' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Sharp' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        SharpManage(full_product)

    elif 'cqe.pl' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'CQE' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        CQEManage(full_product)

    elif 'blaupunkt.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Blaupunkt' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        BlaupunktManage(full_product)

    elif 'philips-hue.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Philips_HUE' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        PhilipsHueManage(full_product)

    elif 'sklepasus' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'ASUS' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        SklepAsusManage(full_product)

    elif 'garett.com' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'GARETT' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        GarettManage(full_product)

    elif '2' in full_product['supplier'] and full_product['link'].strip() == '':  # AB
        full_product['product_folder_name_in'] = 'Bosch' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        ABManage(full_product)

    elif 'bosch' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'Bosch' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        BoschManage(full_product)

    elif 'lg.' in full_product['link'].lower():
        full_product['product_folder_name_in'] = 'LG' + full_product['product_folder_name_in']
        CreateProductFolder(full_product['product_folder_name_in'])
        LGManage(full_product)

    else:
        print('WARNING: There was no scrapping function found')
