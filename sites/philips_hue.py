"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector
from tqdm import tqdm
from selenium import webdriver
from imgs_processing.ImgRefractor import prod_img


def description(sel):
    desc_raw = sel.xpath('//div[@class="product-marketing-copy"]/*')

    desc = []
    short = []
    for i in range(len(desc_raw)):
        try:
            img = desc_raw[i].xpath('.//img/@src').extract()[0]
        except IndexError:
            img = ''

        title = ''.join(desc_raw[i].xpath('.//h3[contains(@class, "title")]//text()').extract()).strip()
        content = ''.join(desc_raw[i].xpath('.//p[contains(@class, "description")]//text()').extract()).strip()
        direction = 'left' if i % 2 == 0 else 'right'

        desc.append(
            f"""<div class="two-col-asymmetrically"><div class="{direction}-side">
                <h2 class="important-header">{title}</h2>
                <p>{content}</p></div>
                <img alt="" src="{img}" /></div>
            """
        )
        if len(short) < 7:
            short.append(f'<li>{title}</li>')

    return '<div class="product-description-section">' + ''.join(desc) + '</div>', '<ul>' + ''.join(short) + '</ul>'


def tech_desc(driver):
    imgs_webelements = [link for link in driver.find_elements_by_xpath('//div[@class="swiper-wrapper"]//img')]
    imgs_links = []
    for link in imgs_webelements:
        src = link.get_attribute('src')
        srcset = link.get_attribute('srcset')
        data_srcset = link.get_attribute('data-srcset')

        if src is not None and src != '':
            imgs_links.append(src[:src.find(' ')])
        elif srcset is not None and srcset != '':
            imgs_links.append(srcset[:srcset.find(' ')])
        elif data_srcset is not None and data_srcset != '':
            imgs_links.append(data_srcset[:data_srcset.find(' ')])

    dl = driver.find_elements_by_xpath('//div[@class="product-specifications-v2"]//dl')

    tech = []
    for i in range(len(dl)):
        title = dl[i].find_element_by_xpath('.//dt').text
        tech.append(f'<tr class="specs_category"><td colspan="2">{title}</td></tr>')

        for j in range(len(dl[i].find_elements_by_xpath('.//p[contains(@class, "key")]'))):
            key = dl[i].find_element_by_xpath(f'.//p[contains(@class, "key")][{j+1}]').text
            value = dl[i].find_element_by_xpath(f'.//div[contains(@class, "value")][{j+1}]').text

            tech.append(f'<tr><td class="c_left">{key}</td><td class="c_left">{value}</td></tr>')

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>', imgs_links


def philips_hue_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    driver = webdriver.Chrome('resources/chromedriver.exe')
    driver.get(link)
    driver.implicitly_wait(10)

    desc, short = description(sel)
    tech, imgs_links = tech_desc(driver)

    driver.close()
    return [desc, short, tech], imgs_links


def product_imgs(imgs_links, product_folder_name_in, ean):
    imgs_links = [img for img in imgs_links]

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


def philips_hue_manage(full_product):
    full_product['manufacturer'] = '234'
    full_product['pickup_store'] = '1'
    full_product['descriptions'], imgs_links = philips_hue_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(imgs_links, full_product['product_folder_name_in'],
                                        full_product['sku'])

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Philips Hue White Żarówka Filament E27 ST64 (1 szt.)', 'sku': '8718699688868', 'weight': '1', 'status': '2', 'manufacturer': '', 'url_key': 'Philips Hue White Żarówka Filament E27 ST64 (1 szt.)', 'manufacturer_code': '929002241201', 'link_ceneo': '', 'pickup_store': '1,2,3...', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '171', 'supplier': '27', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://www.philips-hue.com/pl-pl/p/hue-white-filament-1-pack-st64-e27-filament-edison/8718699688868', 'product_folder_name_in': 'Philips_HUE - 929002241201', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
