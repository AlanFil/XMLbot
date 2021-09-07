import re

import requests
from scrapy import Selector
from tqdm import tqdm

from src.globals import func_name
from src.imgs_processing.SaveImages import save_images


def description(sel):
    desc_raw = sel.xpath('//div[@id="box_description"]//div[@itemprop="description"]/*')

    desc = []
    for i in tqdm(range(0, len(desc_raw), 2)):

        try:
            # check if tech specyfication is in second analysling element. We need to check both but if anything
            # can result in an IndexError it will be the second one.
            if 'specyfikacja techniczna:' in desc_raw[i + 1].xpath('.//text()').extract():
                continue
        except IndexError:
            pass
        finally:
            # now check first element no matter what happend ealier
            if 'specyfikacja techniczna:' in desc_raw[i].xpath('.//text()').extract():
                continue

        text = ''.join(desc_raw[i].xpath('.//text()').extract()).strip()
        try:
            img = 'https://www.graef.pl' + desc_raw[i + 1].xpath('.//img/@src').extract()[0]
        except IndexError:
            img = ''
        direction = 'right' if i // 2 % 2 == 0 else 'left'

        desc.append(f"""
        <div class="two-col-asymmetrically">
        <div class="{direction}-side">
            <p>{text}</p>
        </div>
        
        <img alt="" src="{img}" />
        </div>
        """)

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def short_n_tech_desc(sel):
    tech_raw = sel.xpath('//div[@id="box_description"]//div[@itemprop="description"]/*')

    tech_raw_extracted = []
    for ele in tech_raw:
        if 'specyfikacja techniczna:' in ele.extract().lower():
            tech_raw_extracted.append(ele.extract())

    if not tech_raw_extracted:
        return '', ''

    tech_raw_extracted = tech_raw_extracted[0]
    tech = ['<tr class="specs_category"><td colspan="2">Specyfikacja</td></tr>']
    short = []
    for ele in re.findall('<strong>.*?<br>', tech_raw_extracted):
        if 'specyfikacja techniczna:' in ele.lower():
            continue

        ele_tech = ele.replace('<strong>', '<tr><td class="c_left">')
        ele_tech = ele_tech.replace('</strong>', '</td><td class="c_left">')
        ele_tech = ele_tech.replace('<br>', '</td></tr>')
        ele_tech = ele_tech.replace(':', '')
        tech.append(ele_tech)

        ele_short = ele.replace('<strong>', '<li>')
        ele_short = ele_short.replace('</strong>', '')
        ele_short = ele_short.replace('<br>', '</li>')
        short.append(ele_short)

    return '<ul>' + ''.join(short) + '</ul>', \
           '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//a[contains(@id, "prodimg")]/@href').extract():
        img = 'https://www.graef.pl' + img if not img.startswith('https://www.graef.pl') else img
        imgs_links.append(img)

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


def graef_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short, tech = short_n_tech_desc(sel)

    return [desc, short, tech]


@func_name
def graef_manage(full_product):
    full_product['manufacturer'] = '6745'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = graef_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
