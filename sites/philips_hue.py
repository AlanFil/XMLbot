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
    desc_raw = sel.xpath('//div[@class="product-marketing-copy"]/*')

    desc = []
    short = []
    for i in range(len(desc_raw)):
        try:
            img = desc_raw[i].xpath('.//img/@src').extract()[0]
        except IndexError:
            img = ''

        title = ''.join(desc_raw[i].xpath('.//h3[contains(@class, "title")]//text()').extract()).strip()
        content = ''.join(desc_raw[i].xpath('.//p[contains(@class, "description")]//text()').extract()).strip()
        direction = 'left' if i % 2 == 0 else 'right'

        desc.append(
            f"""<div class="two-col-asymmetrically"><div class="{direction}-side">
                <h2 class="important-header">{title}</h2>
                <p>{content}</p></div>
                <img alt="" src="{img}" /></div>
            """
        )
        if len(short) < 7:
            short.append(f'<li>{title}</li>')

    return '<div class="product-description-section">' + ''.join(desc) + '</div>', '<ul>' + ''.join(short) + '</ul>'


def philips_hue_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc, short = description(sel)

    return [desc, short, '']


def philips_hue_manage(full_product):
    full_product['manufacturer'] = '234'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = philips_hue_descriptions(full_product['link'])

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Philips Hue White Żarówka Filament E27 ST64 (1 szt.)', 'sku': '8718699688868', 'weight': '1', 'status': '2', 'manufacturer': '', 'url_key': 'Philips Hue White Żarówka Filament E27 ST64 (1 szt.)', 'manufacturer_code': '929002241201', 'link_ceneo': '', 'pickup_store': '1,2,3...', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '171', 'supplier': '27', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://www.philips-hue.com/pl-pl/p/hue-white-filament-1-pack-st64-e27-filament-edison/8718699688868', 'product_folder_name_in': 'Philips_HUE - 929002241201', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
