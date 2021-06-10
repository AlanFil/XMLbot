""" DJI """

import re

import requests
from scrapy import Selector
from tqdm import tqdm

from globals import separate_by_tag, func_name
from imgs_processing.SaveImages import SaveImages


def description(sel):
    desc = sel.xpath('//div[contains(@id, "longdescription")]/*').extract()
    short_desc = []
    for i in tqdm(range(len(desc))):
        desc[i] = desc[i].replace('\n', '').replace('\t', '')

        for span in separate_by_tag('span', desc[i]):
            if 'font-size: 14px' in span:
                span.replace(re.search(r'<span.*?>', span).group(),
                             '<h1 class="important-header" style="text-align: center;">')
                span.replace('</span>', '</h1>')
                if len(short_desc) < 7:
                    short_desc.append(span[span.find('>'):span.rfind('<')])
            elif 'font-size: 12px' in span:
                span.replace(re.search(r'<span.*?>', span).group(), '<p>')
                span.replace('</span>', '</p>')

        desc[i] = desc[i].replace('src="/data', 'src="https://rcpro.pl/data')

    return '<div class="product-description-section">' + ''.join(desc) + '</div>', \
           '<ul>' + ''.join(short_desc) + '</ul>'


def tech_desc(sel):
    tech = ''
    return tech


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = sel.xpath('//*[@id="projector_form"]//ul[@class="bxslider"]//li//img/@src').extract()
    imgs_links = ['https://rcpro.pl' + img for img in imgs_links if not img.startswith('https://rcpro.pl')]

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def dji_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc, short = description(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


@func_name
def DJIManage(full_product):
    full_product['manufacturer'] = '185'  # DJI
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = dji_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
