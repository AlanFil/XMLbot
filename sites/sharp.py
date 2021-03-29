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
    desc_raw = sel.xpath('//div[@id="tab-description"]//div[@class="et_pb_row"]/*')

    # tqdm()
    desc = []
    short = []
    for i in range(len(desc_raw)):
        direction = 'right' if i % 2 == 0 else 'left'
        h2 = ''.join(desc_raw[i].xpath('.//h3//text()').extract())
        p = ''.join(desc_raw[i].xpath('.//p//text()').extract()).strip()
        img = \
            ''.join(desc_raw[i].xpath('.//div[contains(@class, "img")]/@style').extract()).replace(
                'background-image: url(', '').replace(');', '')

        img = img[1:-1] if img.startswith("'") and img.endswith("'") else img

        desc.append(
            f'<div class="two-col-asymmetrically"><div class="{direction}-side">' +
            f'<h2 class="important-header">{h2}</h2>' +
            f'<p>{p}</p>' +
            '</div>' +
            f'<img alt="" src="{img}"/>' +
            '</div>'
        )

        if len(short) < 7:
            short.append("<li>" + h2 + "</li>")

    return '<div class="product-description-section">' + ''.join(desc) + '</div>', '<ul>' + ''.join(short) + '<ul>'


def tech_desc(sel):
    tech = ''.join(sel.xpath('//div[@id="tab-tableka"]//div[contains(@class, "column")]/*').extract())

    tech = tech.replace('\r', '')
    tech = tech.replace('\n', '')

    tech = tech.replace('<table class="table">', '').replace('</table>', '').replace('<tbody>', '').replace('</tbody>',
                                                                                                            '')
    tech = tech.replace('<h3 class="heading-zeta mb-half">', '<tr class="specs_category"><td colspan="2">').replace(
        '</h3>', "</td></tr>")

    tech = tech.replace('<b>', '').replace('</b>', '')
    tech = tech.replace('<td>', '<td class="c_left">')

    return '<table id="plan_b" class="data-table"><tbody>' + tech + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[@id="sync1"]//a/@href').extract():
        imgs_links.append(img)

    imgs_links = list(dict.fromkeys(imgs_links))  # remove duplicates

    imgs_names = []
    for i in tqdm(range(len(imgs_links))):
        if i == 0:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}-base', crop=False)
            imgs_names.append(f'{ean}-{i}-base.{file_type}')
        else:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}', crop=False)
            imgs_names.append(f'{ean}-{i}.{file_type}')

    return imgs_names


def sharp_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc, short = description(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def sharp_manage(full_product):
    full_product['manufacturer'] = '249'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = sharp_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
    full_product['forceSmallImg'] = True

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Suszarka SHARP KD-HHH7S7GW2-PL', 'sku': '2021032904', 'weight': '1', 'status': '2', 'manufacturer': '249', 'url_key': 'Suszarka SHARP KD-HHH7S7GW2-PL', 'manufacturer_code': 'KDHHH7S7GW2PL', 'link_ceneo': '', 'pickup_store': '1', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '131', 'supplier': '0', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://sharphome.eu/pl/sharp/pranie/kd-hhh7s7gw2/', 'product_folder_name_in': 'Sharp - KDHHH7S7GW2PL', 'attribute_set_id': '4'}
# link = full_product['link']
