"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector
from tqdm import tqdm

from globals import join_strip
from imgs_processing.ImgRefractor import prod_img


def description(sel):
    desc_raw = sel.xpath('//div[@class="wrapper-opisy"]/*')

    desc = []
    for i in range(len(desc_raw)):
        header = join_strip(desc_raw[i].xpath('.//div[@class="col-5-6"]//h3[not(@class)]/text()').extract())
        content = join_strip(desc_raw[i].xpath('.//div[@class="col-5-6"]//p/text()').extract())
        img = join_strip(desc_raw[i].xpath('.//div[@class="col-5-6"]//img/@src').extract())
        img = 'https://sklepasus.pl' + img if not img.startswith('https://sklepasus.pl/') else img

        desc.append(
            f"""<div><h1 class="important-header" style="text-align: center;">{header}</h1>
            <p style="text-align: center;">{content}</p></div>
            <div style="text-align: center;">
            <img alt="" src="{img}" /></div>""")

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def short_desc(sel):
    short = sel.xpath('//ul[contains(@class, "m-offer_descList")]//li').extract()
    short = [x.replace('  ', '').replace('\n', '').replace(':', ': ') for x in short]
    return '<ul>' + ''.join(short) + '</ul>'


def tech_desc(sel):
    tech_raw = sel.xpath('//div[@class="m-offerShowData_table"]/*')

    tech = ['<tr class="specs_category"><td colspan="2">Specyfikacja</td></tr>']
    for i in range(len(tech_raw)):
        name = join_strip(tech_raw[i].xpath('./div[contains(@class, "name")]//text()').extract())
        value = join_strip(tech_raw[i].xpath('./div[contains(@class, "value")]//text()').extract())

        tech.append(f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>')

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('//div[contains(@id, "offerGallery")]//img[@class="m-offerGallery_picture"]/@data-zoom-image').extract()]
    imgs_links = ['https://sklepasus.pl' + img for img in imgs_links if not img.startswith('https://sklepasus.pl')]

    imgs_links = list(dict.fromkeys(imgs_links))  # remove duplicates

    imgs_names = []
    print("Pobieranie zdjęć produktu...")
    for i in tqdm(range(len(imgs_links))):
        if i == 0:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}-base', crop=False)
            imgs_names.append(f'{ean}-{i}-base.{file_type}')
        else:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}', crop=False)
            imgs_names.append(f'{ean}-{i}.{file_type}')

    return imgs_names


def sklepasus_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def sklepasus_manage(full_product):
    full_product['manufacturer'] = '5878'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = sklepasus_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])
