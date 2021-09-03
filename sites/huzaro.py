"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import re
import requests
from scrapy import Selector

from globals import func_name
from imgs_processing.SaveImages import SaveImages


def Description(raw_desc):
    huzaro_link = 'https://huzaro.pl'

    desc = []
    for ele in raw_desc:
        link = ''.join(ele.xpath('.//img/@src').extract())
        link = huzaro_link + link if not link.startswith(huzaro_link) else link

        content = ''.join(ele.xpath('.//section[@class="text-item"]/*').extract())
        content = content.replace('\r', '').replace('\n', '')
        for rep in re.findall('<div.*?>', content):
            content = content.replace(rep, '')
        content = content.replace('</div>', '')
        for rep in re.findall('<h2.*?>', content):
            content = content.replace(rep, '<h2 class="important-header">')

        direction = 'left' if raw_desc.index(ele) % 2 == 0 else 'right'

        desc.append(f"""
        <div class="two-col-asymmetrically">
            <div class="{direction}-side">
                {content}
            </div>
            
            <img alt="" src="{link}" />
        </div>""")

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def ShortDesc(raw_desc):
    short = raw_desc.xpath('.//li').extract()

    return '<ul>' + ''.join(short) + '</ul>'


def TechDesc(raw_desc):
    elements = [ele.split(':') for ele in raw_desc.xpath('.//li').extract()]
    tech = []
    for ele in elements:
        name = ele[0].replace(re.search('<.*?>', ele[0]).group(), '').strip()
        try:
            value = ele[1].replace(re.search('<.*?>', ele[1]).group(), '').strip()
        except AttributeError:
            value = ele[1]
        except IndexError:
            value = name
            name = ''

        tech.append(f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>')

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def ProductImgs(link, product_folder_name_in, ean):
    huzaro_link = 'https://huzaro.pl'
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('//div[@class="innersmallgallery"]//a/@href').extract()]
    imgs_links = [huzaro_link + img for img in imgs_links if not img.startswith(huzaro_link)]

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def HuzaroDescriptions(link):
    sel = Selector(text=requests.get(link).content)
    desc_elements = sel.xpath('//*[@itemprop="description"]//section[@class="section"]')

    desc = Description(desc_elements[1:-1])
    short = ShortDesc(desc_elements[0])
    tech = TechDesc(desc_elements[-1])

    return [desc, short, tech]


@func_name
def huzaro_manage(full_product):
    full_product['forceSmall'] = True
    full_product['manufacturer'] = '7176'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = HuzaroDescriptions(full_product['link'])
    full_product['imgs'] = ProductImgs(full_product['link'], full_product['product_folder_name_in'],
                                       full_product['sku'])

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Fotel gamingowy Huzaro FORCE 2.5 Red', 'sku': '5907564629539', 'weight': '1', 'status': '2', 'manufacturer': '7176', 'url_key': 'Fotel gamingowy Huzaro FORCE 2.5 Red', 'manufacturer_code': 'HZ-Force 2.5 Red', 'link_ceneo': '', 'pickup_store': '1', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '0', 'supplier': '0', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://www.huzaro.pl/pl/p/Fotel-Gamingowy-HUZARO-FORCE-2.5-RED/105', 'product_folder_name_in': 'Huzaro - HZForce25Red', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
