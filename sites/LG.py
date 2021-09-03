"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector

from globals import func_name
from imgs_processing.SaveImages import SaveImages


def Description(sel):
    desc = []

    # desc_raw = sel.xpath('')
    #
    # desc = []
    # for i in range(len(desc_raw)):
    #     pass

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def ShortDesc(sel):
    short = sel.xpath('//ul[1 and @class="feature-list"]/*').extract()

    for i in range(len(short)):
        short[i] = short[i].replace('<template>', '').replace('</template>', '')
        short[i] = short[i].replace('<li>*bulletFeatureDesc*</li>', '')

    short = list(dict.fromkeys(short))

    return '<ul>' + ''.join(short) + '</ul>'


def TechDesc(sel):
    tech_raw = sel.xpath('//div[@class="tech-spacs-wrap"]/div[contains(@class, "tech-spacs-area")]/*')

    tech = []
    for i in range(len(tech_raw)):
        if 'informacje o zgodności' in tech_raw[i].extract().lower():
            continue

        category_name = ''.join(tech_raw[i].xpath('./h2/text()').extract())
        tech.append(f'<tr class="specs_category"><td colspan="2">{category_name}</td></tr>')

        params = tech_raw[i].xpath('.//dl')
        for j in range(len(params)):
            title = ''.join(params[j].xpath('./dt').extract()).replace('<dt>', '').replace('</dt>', '').strip()
            value = ''.join(params[j].xpath('./dd').extract()).replace('<dd>', '').replace('</dd>', '').strip()

            tech.append(f'<tr><td class="c_left">{title}</td>')
            tech.append(f'<td class="c_left">{value}</td></tr>')

    tech = ''.join(tech).replace('●', 'Tak')

    return '<table id="plan_b" class="data-table"><tbody>' + tech + '</tbody></table>'


def ProductImgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('').extract()]

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def LGDescriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = Description(sel)
    short = ShortDesc(sel)
    tech = TechDesc(sel)

    return [desc, short, tech]


@func_name
def lg_manage(full_product):
    full_product['manufacturer'] = '211'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = LGDescriptions(full_product['link'])
    full_product['imgs'] = ProductImgs(full_product['link'], full_product['product_folder_name_in'],
                                       full_product['sku'])


# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'SŁUCHAWKI LG TONE Free HBS-FN7 Black',
#                 'sku': '8806091008855', 'weight': '1', 'status': '2', 'manufacturer': '211',
#                 'url_key': 'SŁUCHAWKI LG TONE Free HBS-FN7 Black', 'manufacturer_code': 'HBS-FN7 Black',
#                 'link_ceneo': '', 'pickup_store': '1', 'search_keywords': '', 'search_priority': '',
#                 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0',
#                 'rule': '133', 'supplier': '4', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [],
#                 'link': 'https://www.lg.com/pl/sluchawki/lg-hbs-fn7-black',
#                 'product_folder_name_in': 'LG - HBSFN7Black', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
