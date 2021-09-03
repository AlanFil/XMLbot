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


def description(sel):
    # there are at least two patterns. If first wont me found (list will be empty) the second will fill desc_raw list
    desc_raw = sel.xpath('//div[@itemprop="description"]//div[@class="beauty-opis-wrap"]/*')
    desc_raw.extend(sel.xpath('//div[@itemprop="description"]//div[@class="container-desc"]/*'))

    desc = []
    short = []
    for i in range(len(desc_raw)):
        try:
            html_class = re.search('class=".*?"', desc_raw[i].extract()).group()
        except AttributeError:
            continue

        title = ''.join(desc_raw[i].xpath('.//h3//text()').extract())
        content = ''.join(desc_raw[i].xpath('.//p//text()').extract())

        if 'Zestaw zawiera' in title or 'Prezentacja produktu' in title:
            continue

        if 'Zobacz film' in title:
            title = ''

        if title != '' and len(short) < 7:
            short.append(f'<li>{title}</li>')

        try:
            img = ''.join(desc_raw[i].xpath('.//*[contains(@class, "img")]//img/@src').extract()[0])
            img = 'https://garett.com.pl' + img if not img.startswith('https://garett.com.pl') else img
        except IndexError:
            img = ''

        try:
            img2 = ''.join(desc_raw[i].xpath('.//*[contains(@class, "img")]//img/@src').extract()[1])
            img2 = 'https://garett.com.pl' + img2 if not img2.startswith('https://garett.com.pl') else img2
        except IndexError:
            img2 = ''

        if 'full' in html_class:
            desc.append(f"""
            <div><h1 class="important-header" style="text-align: center;">{title}</h1>
            <p style="text-align: center;">{content}</p></div>
            <div style="text-align: center;">
            <img alt="" src="{img}" /></div>
            """)
        elif 'half' in html_class or 'photo-item' in html_class:
            direction = 'right' if i % 2 == 0 else 'left'
            if content.strip() == '' and img2 != '':
                desc.append(f"""
                            <div class="two-col-asymmetrically">
                            <img alt="" src="{img}" />
                            <img alt="" src="{img2}" /></div>""")
                continue

            desc.append(f"""
            <div class="two-col-asymmetrically"><div class="{direction}-side"><h2 class="important-header">{title}</h2>
            <p>{content}</p></div>
            <img alt="" src="{img}" /></div>
            """)

    return '<div class="product-description-section">' + ''.join(desc) + '</div>', '<ul>' + ''.join(short) + '</ul>'


def tech_desc(sel):
    tech_raw = sel.xpath('//table[@class="table"]//tr[contains(@class, "r--l")]')

    tech = []
    for i in range(len(tech_raw)):
        name = ''.join(tech_raw[i].xpath('./td[contains(@class, "name")]//text()').extract()).strip()
        value = ''.join(tech_raw[i].xpath('./td[contains(@class, "value")]//text()').extract()).strip()

        if value == '':
            tech.append(f'<tr class="specs_category"><td colspan="2">{name}</td></tr>')
        else:
            tech.append(f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>')

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('//div[@class="innersmallgallery"]//a/@href').extract()]
    for img in imgs_links:
        img = 'https://garett.com.pl' + img if not img.startswith('https://garett.com.pl') else img

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def garett_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc, short = description(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


@func_name
def garett_manage(full_product):
    full_product['manufacturer'] = '196'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = garett_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
