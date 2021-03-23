"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""

import requests
from scrapy import Selector
from tqdm import tqdm

from globals import separate_by_tag
from imgs_processing.ImgRefractor import prod_img


def description(sel):
    desc = sel.xpath('//div[@id="tab-description"]/*')

    for i in tqdm(range(len(desc))):
        desc[i] = desc[i].extract()

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def short_desc(sel):
    short = ''.join(sel.xpath('//div[@id="tab-specyfication"]/*').extract())
    li = separate_by_tag('li', short)
    short = short.replace(''.join(li[6:]), '')
    short = short.replace('<cechy>', '').replace('</cechy>', '').replace('<b>', '').replace('</b>', '')

    return short


def tech_desc(sel):
    tech = sel.xpath('//div[@id="tab-specyfication"]/ul/*')

    for i in tqdm(range(len(tech))):
        tech[i] = ''.join(tech[i].xpath('.//text()').extract()).strip()
        if len(tech[i].split(':')) == 2:
            name, value = tech[i].split(':')
            tech[i] = f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>'
        else:
            tech[i] = f'<tr><td class="c_left"></td><td class="c_left">{tech[i]}</td></tr>'

    tech = '<table id="plan_b" class="data-table"><tbody><tr class="specs_category">' \
           '<td colspan="2">Specyfikacja</td></tr>' + ''.join(tech) + '</tbody></table>'
    return tech


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[contains(@id, "product")]//div[@class="images"]//a/@href').extract():
        imgs_links.append(img)

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
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Podkaszarka akumulatorowa 4GARDEN APK2521 + akumulator i ładowarka ', 'sku': '5903357105303', 'weight': '1', 'status': '2', 'manufacturer': '0', 'url_key': 'Podkaszarka akumulatorowa 4GARDEN APK2521 plus akumulator i ładowarka ', 'manufacturer_code': '4GP_APK2521S', 'link_ceneo': '', 'pickup_store': '', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '189', 'supplier': '27', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://www.krysiak.pl/oferta/urzadzenia/urzadzenia-akumulatorowe/system-18v-20v/podkaszarka-akumulatorowa-20v-4garden-apk2521/', 'product_folder_name_in': 'KRYSIAK - 4GPAPK2521S', 'attribute_set_id': '4'}
