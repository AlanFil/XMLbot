"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector

from src.globals import func_name
from src.imgs_processing.SaveImages import SaveImages


def Description(sel):
    desc_raw = sel.xpath('')

    desc = []
    for i in range(len(desc_raw)):
        pass

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def ShortDesc(sel):
    short_raw = sel.xpath('')

    short = []
    for i in range(len(short_raw)):
        pass

    return '<ul>' + ''.join(short) + '</ul>'


def TechDesc(link):
    link = link + 'specs' if link.endswith('/') else link + '/specs'
    sel = Selector(text=requests.get(link).content)

    tech_element = sel.xpath('//ul[@class="large-accordion__list"]/*')

    tech = []
    for ele in tech_element:
        title = ''.join(ele.xpath('.//span[contains(@class, "title")]//text()').extract())

        tech.append(f'<tr class="specs_category"><td colspan="2">{title}</td></tr>')
        for param in ele.xpath('.//div[contains(@class, "large-accordion__inner")]'):
            name = ''.join(param.xpath('./div//text()').extract())
            value = '<br/>'.join(param.xpath('./p//text()').extract())

            if value.strip() == '':
                value, name = name, ''

            tech.append(f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>')

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def ProductImgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('').extract()]

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def HuaweiDescriptions(link):
    sel = Selector(text=requests.get(link).content)

    # desc = Description(sel)
    # short = ShortDesc(sel)
    tech = TechDesc(link)

    return ['desc', 'short', tech]


@func_name
def huawei_manage(full_product):
    full_product['manufacturer'] = '202'
    full_product['pickup_store'] = '1, 24'
    full_product['price_negotiation_hide'] = '1'
    full_product['descriptions'] = HuaweiDescriptions(full_product['link'])
    # full_product['imgs'] = ProductImgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Laptop HUAWEI Matebook D15 [15,6" | i5-1135G7 | 16GB RAM | 512GB | Win10 Home]', 'sku': '6941487219391', 'weight': '1', 'status': '2', 'manufacturer': '202', 'url_key': 'Laptop HUAWEI Matebook D15 [15,6" | i5-1135G7 | 16GB RAM | 512GB | Win10 Home]', 'manufacturer_code': '53010_i5', 'link_ceneo': '', 'pickup_store': '1', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '1', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '128', 'supplier': '4', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://consumer.huawei.com/pl/laptops/matebook-d-15-2021/', 'product_folder_name_in': 'Huawei - 53010i5', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
