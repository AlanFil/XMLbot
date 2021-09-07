import requests
from scrapy import Selector

from src.globals import func_name
from src.imgs_processing.SaveImages import SaveImages


def description(sel):
    desc_raw = sel.xpath('//div[@class="tab-content"]//div[contains(@id, "tab0")]//div[@class="content"]/*')

    desc = []
    for i in range(len(desc_raw)):
        if 'h2' not in desc_raw[i].extract():
            continue

        title = ''.join(desc_raw[i].xpath('.//h2[@class="feature_title"]//text()').extract())
        content = ''.join(desc_raw[i].xpath('.//div[@class="feature_desc"]//text()').extract())
        img = ''.join(desc_raw[i].xpath('.//div[@class="feature_image"]//img/@src').extract())
        img = 'https://scentre.pl' + img if not img.startswith('https://scentre.pl') else img

        desc.append(
            f"""
            <div class="two-col-asymmetrically">
                <div class="right-side">
                    <h2 class="important-header">{title}</h2>
                    <p>{content}</p>
                </div>
                
                <img alt="" src="{img}" />
            </div>
            """)

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def short_desc(sel):
    short = ''
    return short


def tech_desc(sel):
    tech = sel.xpath('//div[@class="tab-content"]//div[contains(@id, "tab1")]/*')

    tech_ready = []
    for i in range(len(tech)):
        tech_ready.append(
            '<tr class="specs_category"><td colspan="2">' +
            ''.join(tech[i].xpath('.//div[@class="name"]//text()').extract()).strip() +
            '</td></tr>'
        )

        name_value = tech[i].xpath('.//div[@class="group"]/*')
        for nv in name_value:
            tech_ready.append(
                '<tr><td class="c_left">' +
                ''.join(nv.xpath('.//div[@class="desc"]//text()').extract()).strip() +
                '</td><td class="c_left">' +
                ''.join(nv.xpath('.//div[@class="value"]//text()').extract()).strip() +
                '</td></tr>'
            )

    tech_ready = '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech_ready) + '</tbody></table>'
    return tech_ready


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[contains(@class, "product_image_master")]/img/@src').extract():
        new_link = 'https://scentre.pl/' + img
        imgs_links.append(new_link)

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def scentre_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


@func_name
def scentre_manage(full_product):
    full_product['manufacturer'] = '252'
    full_product['pickup_store'] = '1,2,3,4,7,8,9,10,11,21,25'
    full_product['descriptions'] = scentre_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
