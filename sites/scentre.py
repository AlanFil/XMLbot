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
    desc = sel.xpath('//div[@class="tab-content"]//div[contains(@id, "tab0")]/*')

    for i in tqdm(range(len(desc))):
        pass
    return desc


def short_desc(sel):
    short = ''
    return short


def tech_desc(sel):
    tech = sel.xpath('//div[@class="tab-content"]//div[contains(@id, "tab1")]/*')

    tech_ready = []
    for i in tqdm(range(len(tech))):
        tech_ready.append(
            '<tr class="specs_category"><td colspan="2">' +
            ''.join(tech[i].xpath('.//div[@class="name"]//text()').extract()).strip() +
            '</td></tr>'
        )

        name_value = tech[i].xpath('.//div[@class="group"]/*')
        for nv in name_value:
            tech_ready.append(
                '<tr><td class="c_left">' +
                ''.join(nv.xpath('.//div[@class="desc"]//text()').extract()).strip() +
                '</td><td class="c_left">' +
                ''.join(nv.xpath('.//div[@class="value"]//text()').extract()).strip() +
                '</td></tr>'
            )

    tech_ready = '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech_ready) + '</tbody></table>'
    return tech_ready


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[contains(@class, "product_image_master")]/img/@src').extract():
        new_link = 'https://scentre.pl/' + img
        print(new_link)
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


def scentre_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def scentre_manage(full_product):
    full_product['manufacturer'] = '252'
    full_product['pickup_store'] = '1,2,3,4,7,8,9,10,11,21,25'
    full_product['descriptions'] = scentre_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])


if __name__ == '__main__':
    full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'TVC SONY 55" XR55A90JAEP', 'sku': '4548736123274', 'weight': '1', 'status': '2', 'manufacturer': '0', 'url_key': 'TVC SONY 55" XR55A90JAEP', 'manufacturer_code': 'XR55A90JAEP', 'link_ceneo': '', 'pickup_store': '', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '64', 'supplier': '4', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://scentre.pl/shop/product/show?produkt=telewizor_sony_oled_65_cali_xr_65a90j_sluchawki_sony_wh_1000xm4', 'product_folder_name_in': 'Sony - XR55A90JAEP', 'attribute_set_id': '4'}
    scentre_manage(full_product)
