import requests
from scrapy import Selector
from selenium import webdriver

from globals import func_name
from imgs_processing.SaveImages import SaveImages


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
            key = dl[i].find_element_by_xpath(f'.//p[contains(@class, "key")][{j + 1}]').text
            value = dl[i].find_element_by_xpath(f'.//div[contains(@class, "value")][{j + 1}]').text

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

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


@func_name
def PhilipsHueManage(full_product):
    full_product['manufacturer'] = '234'
    full_product['pickup_store'] = '1'
    full_product['descriptions'], imgs_links = philips_hue_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(imgs_links, full_product['product_folder_name_in'],
                                        full_product['sku'])
