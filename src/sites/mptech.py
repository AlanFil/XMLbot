from time import sleep

import requests
from scrapy import Selector
from selenium import webdriver

from src.globals import func_name
from src.imgs_processing.SaveImages import save_images


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def description(sel):
    desc = sel.xpath('//div[@id="product.info.description"]//div[@class="value"]/*')

    desc_done = []
    for i in range(len(desc)):
        link = ''.join(desc[i].xpath('.//img/@src').extract())
        if link == '':
            continue
        old_link = link
        link = 'https://sklep.mptech.eu' + link if not link.startswith('https://sklep.mptech.eu') else link

        if 'youtube' in desc[i].extract():
            continue

        if 'productStrip' in desc[i].extract():
            direction = 'right' if i % 2 == 0 else 'left'
            desc_done.append(
                '<div class="two-col-asymmetrically">'
                f'<div class="{direction}-side">'
                '<h2 class="important-header">' +
                ''.join(desc[i].xpath('.//h2/text()').extract()).strip() +
                '</h2>'
                '<p>' +
                ''.join(desc[i].xpath('.//p/text()').extract()).strip() +
                '</p>'
                '</div>' +
                '<img alt="" src="' + link + '" />'
                '</div>'
            )
        else:
            desc[i] = desc[i].extract()
            desc[i] = desc[i].replace('<h2>', '<h1 class="important-header" style="text-align: center;">').replace('</h2>', '</h1>')
            desc[i] = desc[i].replace('class="mpSegment-txt"', '')
            desc[i] = desc[i].replace('class="mpSegment-img"', 'style="text-align: center;"')
            if not old_link == link:
                desc[i] = desc[i].replace(old_link, link)
            desc_done.append(desc[i])

    return '<div class="product-description-section">' + ''.join(desc_done) + '</div>'


def short_desc(sel):
    short = ''.join(sel.xpath('//div[@itemprop="description"]').extract())
    short = short.replace('<div class="value" itemprop="description">', '').replace('</div>', '')
    short = short.replace('<p>', '').replace('</p>', '')
    short = short.replace('<strong>', '').replace('</strong>', '')
    short = ''.join(f'<li>{s.strip()}</li>' for s in short.split('<br>'))
    short = short.replace('<li></li>', '')

    return '<ul>' + short + '</ul>'


def tech_desc(sel):
    try:
        tech_link = sel.xpath('//*[@id="product-attribute-specs-table"]//a/@href').extract()[0]
    except IndexError:
        return ''
    tech_sel = Selector(text=requests.get(tech_link).content)
    tech_raw = tech_sel.xpath('//div[@class="printer__item"]')

    tech = []
    for i in range(len(tech_raw)):
        tech.append(
            '<tr class="specs_category"><td colspan="2">' +
            ''.join(tech_raw[i].xpath('./div[@class="printer__subtitle"]//text()').extract()).strip() +
            '</td></tr>'
        )
        name_value = tech_raw[i].xpath('./div[@class="printer__value"]')
        for nv in name_value:
            value = ''.join(nv.xpath('./div[@class="printer__valueDetails"]//text()').extract()).strip()
            value = value if value != '' else 'Tak'
            tech.append(
                '<tr><td class="c_left">' +
                ''.join(nv.xpath('./div[@class="printer__valueName"]//text()').extract()).strip() +
                '</td><td class="c_left">' +
                value +
                '</td></tr>'
            )

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def product_imgs(link, product_folder_name_in, ean):
    driver = webdriver.Chrome('resources/chromedriver.exe')
    driver.get(link)
    driver.implicitly_wait(10)
    driver.find_elements_by_xpath('//img[@class="fotorama__img"]')
    sleep(3)
    links = driver.find_elements_by_xpath('//img[@class="fotorama__img"]')
    links = [link.get_attribute('src') for link in links]
    driver.close()

    imgs_names = save_images(links, product_folder_name_in, ean)

    return imgs_names


def mptech_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


@func_name
def mptech_manage(full_product):
    full_product['manufacturer'] = '286' if 'hammer' in full_product['name'].lower() else '285'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = mptech_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])
