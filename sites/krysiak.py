"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
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


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[contains(@class, "pd-header-gallery")]//img/@data-desktop-src').extract():
        new_link = img.replace('//', 'https://').replace('$LazyLoad_Home', '').replace('$684_547', '')
        imgs_links.append(new_link)

    imgs_links = list(dict.fromkeys(imgs_links))  # remove duplicates
    imgs_names = []
    for i, img_link in enumerate(imgs_links):
        if i == 0:
            file_type = prod_img(product_folder_name_in, img_link, f'{ean}-{i}-base', crop=False)
            imgs_names.append(f'{ean}-{i}-base.{file_type}')
        else:
            file_type = prod_img(product_folder_name_in, img_link, f'{ean}-{i}', crop=False)
            imgs_names.append(f'{ean}-{i}.{file_type}')

    return imgs_names


def krysiak_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def krysiak_manage(full_product):
    full_product['manufacturer'] = '7156'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = krysiak_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])
