"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector
from tqdm import tqdm

from globals import func_name
from imgs_processing.ImgRefractor import prod_img
from imgs_processing.save_images import save_images


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

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


def XXX_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


@func_name
def XXX_manage(full_product):
    full_product['manufacturer'] = ''
    full_product['pickup_store'] = '1,2,3...'
    full_product['descriptions'] = XXX_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])

# full_product =
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
