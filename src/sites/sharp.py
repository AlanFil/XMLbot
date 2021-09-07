import requests
from scrapy import Selector

from src.imgs_processing.SaveImages import save_images


def description(sel):
    desc_raw = sel.xpath('//div[@id="tab-description"]//div[@class="et_pb_row"]/*')

    desc = []
    short = []
    for i in range(len(desc_raw)):
        direction = 'right' if i % 2 == 0 else 'left'
        h2 = ''.join(desc_raw[i].xpath('.//h3//text()').extract())
        p = ''.join(desc_raw[i].xpath('.//p//text()').extract()).strip()
        img = \
            ''.join(desc_raw[i].xpath('.//div[contains(@class, "img")]/@style').extract()).replace(
                'background-image: url(', '').replace(');', '')

        img = img[1:-1] if img.startswith("'") and img.endswith("'") else img

        desc.append(
            f'<div class="two-col-asymmetrically"><div class="{direction}-side">' +
            f'<h2 class="important-header">{h2}</h2>' +
            f'<p>{p}</p>' +
            '</div>' +
            f'<img alt="" src="{img}"/>' +
            '</div>'
        )

        if len(short) < 7:
            short.append("<li>" + h2 + "</li>")

    return '<div class="product-description-section">' + ''.join(desc) + '</div>', '<ul>' + ''.join(short) + '<ul>'


def tech_desc(sel):
    tech = ''.join(sel.xpath('//div[@id="tab-tableka"]//div[contains(@class, "column")]/*').extract())

    tech = tech.replace('\r', '')
    tech = tech.replace('\n', '')

    tech = tech.replace('<table class="table">', '').replace('</table>', '').replace('<tbody>', '').replace('</tbody>',
                                                                                                            '')
    tech = tech.replace('<h3 class="heading-zeta mb-half">', '<tr class="specs_category"><td colspan="2">').replace(
        '</h3>', "</td></tr>")

    tech = tech.replace('<b>', '').replace('</b>', '')
    tech = tech.replace('<td>', '<td class="c_left">')

    return '<table id="plan_b" class="data-table"><tbody>' + tech + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[@id="sync1"]//a/@href').extract():
        imgs_links.append(img)

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


def sharp_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc, short = description(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def sharp_manage(full_product):
    full_product['manufacturer'] = '249'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = sharp_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
    full_product['forceSmallImg'] = True
