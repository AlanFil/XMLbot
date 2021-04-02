"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import re

import requests
from scrapy import Selector
from tqdm import tqdm

from imgs_processing.ImgRefractor import prod_img


def description(sel):
    desc = ''.join(sel.xpath('//div[@id="popis"]//div[@class="desc"]/*').extract())

    for ele in re.findall(r'<p .*?>', desc):
        desc = desc.replace(ele, '<p>')
    for ele in re.findall(r'<br .*?>', desc):
        desc = desc.replace(ele, '<br />')
    for ele in re.findall(r'<strong .*?>', desc):
        desc = desc.replace(ele, '<strong>')
    for ele in re.findall(r'<span .*?>', desc):
        desc = desc.replace(ele, '')
    desc = desc.replace('</span>', '')
    desc = desc.replace('\r', '')
    desc = desc.replace('\n', '')

    return '<div class="product-description-section">' + desc + '</div>'


def short_and_tech_desc(sel):
    tech_raw_tr = sel.xpath('//*[@id="technical"]//tr')

    tech = []
    short = []
    for tr in tech_raw_tr:
        try:
            name, value = tr.xpath('./td').extract()
        except ValueError:
            name, value = tr.xpath('./td').extract()[0], tr.xpath('./td').extract()[1]

        if 'parametr' in name.lower():
            continue

        name = name.replace('<td>', '').replace('</td>', '').strip()
        value = value.replace('<td>', '').replace('</td>', '').strip()

        tech.append(f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>')
        if len(short) < 7:
            short.append(f'<li>{name}: {value}</li>')

    return '<ul>' + ''.join(short) + '</ul>', \
           '<table id="plan_b" class="data-table"><tbody><tr class="specs_category"><td colspan="2">Specyfikacja</td></tr>' + ''.join(tech) + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_pages = [img for img in sel.xpath('//div[@class="wrap_image"]//a/@href').extract()]

    imgs_pages = list(dict.fromkeys(imgs_pages))  # remove duplicates

    imgs_links = []
    for img_link in imgs_pages:
        try:
            img_sel = Selector(text=requests.get(img_link).content)
        except requests.exceptions.MissingSchema:
            continue
        imgs_links.append(img_sel.xpath('//img/@src').extract()[0])

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


def cqe_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short, tech = short_and_tech_desc(sel)

    return [desc, short, tech]


def cqe_manage(full_product):
    full_product['manufacturer'] = ''
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = cqe_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])
