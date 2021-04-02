"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector
from tqdm import tqdm

from imgs_processing.ImgRefractor import prod_img


def description(sel):
    desc_raw = sel.xpath('')

    desc = []
    for i in range(len(desc_raw)):
        pass

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def short_desc(sel):
    short_raw = sel.xpath('')

    short = []
    for i in range(len(short_raw)):
        pass

    return '<ul>' + ''.join(short) + '</ul>'


def tech_desc(sel):
    tech_raw = sel.xpath('')

    tech = []
    for i in range(len(tech_raw)):
        pass

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('').extract()]

    imgs_links = list(dict.fromkeys(imgs_links))  # remove duplicates

    imgs_names = []
    print("Pobieranie zdjęć produktu...")
    for i in tqdm(range(len(imgs_links))):
        if i == 0:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}-base', crop=False)
            imgs_names.append(f'{ean}-{i}-base.{file_type}')
        else:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}', crop=False)
            imgs_names.append(f'{ean}-{i}.{file_type}')

    return imgs_names


def XXX_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def XXX_manage(full_product):
    full_product['manufacturer'] = ''
    full_product['pickup_store'] = '1,2,3...'
    full_product['descriptions'] = XXX_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])

# full_product =
# link = full_product['link']
