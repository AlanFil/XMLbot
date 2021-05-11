import re

import requests
from scrapy import Selector

from globals import func_name
from imgs_processing.save_images import save_images


def description(sel):
    desc = sel.xpath('//div[@id="content_sub"]//div[contains(@class, "newkeyvisual")]')

    for i in range(len(desc)):
        direction = 'right' if i % 2 == 0 else 'left'

        try:
            link = 'https://www.blaupunkt.com/' + desc[i].xpath('.//img/@src').extract()[0]
        except IndexError:
            link = ''

        desc[i] = desc[i].extract()

        if re.findall(r'<div class="newkeyimage.*?</div>', desc[i]):
            desc[i] = desc[i].replace(re.search(r'<div class="newkeyimage.*?</div>', desc[i]).group(),
                                      f'<img src="{link}" />')

        if re.findall(r'<div class="newkeyvisual.*?>', desc[i]):
            desc[i] = desc[i].replace(re.search(r'<div class="newkeyvisual.*?>', desc[i]).group(),
                                      f'<div class="two-col-asymmetrically">')

        desc[i] = desc[i].replace('newkeytext', f'{direction}-side')

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def short_and_tech_desc(sel):
    tech_raw = sel.xpath('//div[@id="tab-details"]/ul/li/text()').extract()

    tech = []
    short = []
    tech_end = []
    for ele in tech_raw:
        if len(ele.split(':')) == 2:
            name, value = ele.split(':')
            tech.append(f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>')
        else:
            if len(short) < 7:
                short.append(f'<li>{ele}</li>')
            if not tech_end:
                tech_end.append(f'<tr><td class="c_left">Dodatkowo</td><td class="c_left">{ele}</td></tr>')
            else:
                tech_end.append(f'<tr><td class="c_left"></td><td class="c_left">{ele}</td></tr>')

    tech.extend(tech_end)

    return '<ul>' + ''.join(short) + '</ul>', \
           '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = ['https://www.blaupunkt.com/' + img for img in
                  sel.xpath('//div[@id="product_gallery_new"]//img/@src').extract()]

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


def blaupunkt_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short, tech = short_and_tech_desc(sel)

    return [desc, short, tech]


@func_name
def blaupunkt_manage(full_product):
    full_product['manufacturer'] = '170'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = blaupunkt_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Power audio BLAUPUNKT MB06', 'sku': '5901750501906', 'weight': '1', 'status': '2', 'manufacturer': '', 'url_key': 'Power audio BLAUPUNKT MB06', 'manufacturer_code': 'MB06', 'link_ceneo': '', 'pickup_store': '1', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '0', 'supplier': '27', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://www.blaupunkt.com/pl/nc/produkty/sprzet-audio/power-audio/products/single/15016/', 'product_folder_name_in': 'Blaupunkt - MB06', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
