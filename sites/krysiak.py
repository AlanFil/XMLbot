import requests
from scrapy import Selector

from globals import separate_by_tag, func_name
from imgs_processing.SaveImages import SaveImages


def description(sel):
    desc = sel.xpath('//div[@id="tab-description"]/*')

    for i in range(len(desc)):
        desc[i] = desc[i].extract()

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def short_desc(sel):
    short = ''.join(sel.xpath('//div[@id="tab-specyfication"]/*').extract())
    li = separate_by_tag('li', short)
    short = short.replace(''.join(li[6:]), '')
    short = short.replace('<cechy>', '').replace('</cechy>', '').replace('<b>', '').replace('</b>', '')

    return short


def tech_desc(sel):
    tech = sel.xpath('//div[@id="tab-specyfication"]/ul/*')

    for i in range(len(tech)):
        tech[i] = ''.join(tech[i].xpath('.//text()').extract()).strip()
        if len(tech[i].split(':')) == 2:
            name, value = tech[i].split(':')
            tech[i] = f'<tr><td class="c_left">{name}</td><td class="c_left">{value}</td></tr>'
        else:
            tech[i] = f'<tr><td class="c_left"></td><td class="c_left">{tech[i]}</td></tr>'

    tech = '<table id="plan_b" class="data-table"><tbody><tr class="specs_category">' \
           '<td colspan="2">Specyfikacja</td></tr>' + ''.join(tech) + '</tbody></table>'
    return tech


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[contains(@id, "product")]//div[@class="images"]//a/@href').extract():
        imgs_links.append(img)

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def krysiak_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


@func_name
def krysiak_manage(full_product):
    full_product['manufacturer'] = '7156'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = krysiak_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
