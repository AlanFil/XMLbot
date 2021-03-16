"""
def enum(y):
    for i, x in enumerate(y):
        print(f'{i}. {x}')

"""

import re

import requests
from scrapy import Selector
from tqdm import tqdm

from globals import separate_by_tag
from imgs_processing.ImgRefractor import prod_img


def description(sel):
    desc = sel.xpath('//div[contains(@id, "longdescription")]/*').extract()
    short_desc = []
    for i in tqdm(range(len(desc))):
        desc[i] = desc[i].replace('\n', '').replace('\t', '')

        for span in separate_by_tag('span', desc[i]):
            if 'font-size: 14px' in span:
                span.replace(re.search(r'<span.*?>', span).group(), '<h1 class="important-header" style="text-align: center;">')
                span.replace('</span>', '</h1>')
                if len(short_desc) < 7:
                    short_desc.append(span[span.find('>'):span.rfind('<')])
            elif 'font-size: 12px' in span:
                span.replace(re.search(r'<span.*?>', span).group(), '<p>')
                span.replace('</span>', '</p>')

        desc[i] = desc[i].replace('src="/data', 'src="https://rcpro.pl/data')

    return '<div class="product-description-section">' + ''.join(desc) + '</div>',\
           '<ul>' + ''.join(short_desc) + '</ul>'


def tech_desc(sel):
    tech = ''
    return tech


def product_imgs(link, product_folder_name, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = sel.xpath('//*[@id="projector_form"]//ul[@class="bxslider"]//li//img/@src').extract()

    imgs_names = []
    for i, img_link in enumerate(imgs_links):
        img_link = 'https://rcpro.pl/' + img_link
        if i == 0:
            file_type = prod_img(product_folder_name, img_link, f'{ean}-{i}-base', crop=False)
            imgs_names.append(f'{ean}-{i}-base.{file_type}')
        else:
            file_type = prod_img(product_folder_name, img_link, f'{ean}-{i}', crop=False)
            imgs_names.append(f'{ean}-{i}.{file_type}')

    return imgs_names


def dji_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc, short = description(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def dji_manage(full_product):
    full_product['manufacturer'] = '185'  # DJI
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = dji_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])


if __name__ == '__main__':
    full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Ubezpieczenie DJI Care Refresh FPV - plan dwuletni (kod elektroniczny)', 'sku': '6941565908087', 'weight': '1', 'status': '2', 'manufacturer': '0', 'url_key': 'Ubezpieczenie DJI Care Refresh FPV - plan dwuletni (kod elektroniczny)', 'manufacturer_code': 'CP.QT.00004421.01', 'link_ceneo': '', 'pickup_store': '', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '121', 'supplier': '30', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://rcpro.pl/product-pol-20077-DJI-Care-Refresh-FPV-dwuletni-plan-kod-elektroniczny.html?query_id=1', 'product_folder_name_in': ' - CPQT0000442101', 'attribute_set_id': '4'}
    dji_manage(full_product)
