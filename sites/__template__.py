"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')
"""


import requests
from scrapy import Selector
import re
from imgs_processing.ImgRefractor import prod_img


def description(sel):
    desc = ''
    return desc


def short_desc(sel):
    short = ''
    return short


def tech_desc(sel):
    tech = ''
    return tech


def product_imgs(link, product_folder_name, ean):
    imgs = ''
    return imgs


def XXX_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def dji_manage(full_product):
    full_product['manufacturer'] = ''
    full_product['pickup_store'] = '1,2,3...'
    full_product['descriptions'] = XXX_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])
