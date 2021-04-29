"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm

from globals import func_name
from imgs_processing.ImgRefractor import prod_img
from imgs_processing.save_images import save_images


def description(driver):
    return '<div class="product-description-section">' + ''.join() + '</div>'


def short_desc(driver):
    return '<ul>' + ''.join() + '</ul>'


def tech_desc(driver):
    return '<table id="plan_b" class="data-table"><tbody>' + ''.join() + '</tbody></table>'


def product_imgs(driver, product_folder_name_in, ean):
    i = 1
    first = ''
    imgs_links = []
    while True:
        try:
            img = driver.find_element_by_xpath(f'//div[@class="slick-track"]/*[{i}]//picture/source[@type="image/jpeg"]').get_attribute(
                'src').replace('/600x337', '/1200x675')

            if i == 1:
                first = img
            else:
                if first == img:
                    break

            imgs_links.append(img)
            i += 1
        except NoSuchElementException:
            break

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


def bosch_descriptions(link):
    driver = webdriver.Chrome('resources/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get(link)

    # desc = description(driver)
    # short = short_desc(driver)
    # tech = tech_desc(driver)
    #
    # return [desc, short, tech]
    return 1, driver


@func_name
def bosch_manage(full_product):
    full_product['manufacturer'] = ''
    full_product['pickup_store'] = '1,2,3...'
    full_product['descriptions'], driver = bosch_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(driver, full_product['product_folder_name_in'],
                                        full_product['sku'])

    # driver.close()
# full_product =
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
