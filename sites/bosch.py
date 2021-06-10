"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from globals import func_name
from imgs_processing.SaveImages import SaveImages


def description(driver):
    driver.implicitly_wait(2)
    desc = ''
    i = 1
    while True:
        try:
            i += 1
            text = driver.find_element_by_xpath(f'//*[@id="section-highlights"]/*[{i}]').text

            if text == '':
                continue

            try:
                links = driver.find_elements_by_xpath(
                    f'//*[@id="section-highlights"]/*[{i}]//picture//source[@class="js_vp_3"]').get_attribute("src")
                links = [link.get_attribute('srcset') for link in links]
                links = ['https:' + link.split(', ')[0] for link in links if '.jpg' in link]
                try:
                    img = links[0]
                except IndexError:
                    img = ''
            except NoSuchElementException:
                img = ''

            replacements = ['Poprzednie', 'Następne', '1/2', '2/2', '1/3', '2/3', '3/3', 'Dowiedz się więcej',
                            '  Powrót', 'Dalej', 'Do produktów']
            for replacement in replacements:
                text = text.replace(replacement, '')

            text = text.split('\n')
            text = [e for e in text if e]

            direction = 'left' if i % 2 == 0 else 'right'
            if len(text) == 1:
                desc += f'<div><h1 class="important-header" style="text-align: center;">{text[0]}</h1></div>'
            elif len(text) == 2:
                desc += f"""<div class="two-col-asymmetrically"><div class="{direction}-side"><h2 class="important-header">
                            {text[0]}</h2>
                            <p style="font-size: large;">{text[1]}</p></div>
                            <img alt="" src="{img}" /></div>
                        """
            elif len(text) == 3:
                desc += f"""<div class="two-col-asymmetrically"><div class="{direction}-side"><h2 class="important-header">
                        {text[0]}</h2>
                        <p style="font-size: large;">{text[1]}
                        <br/><br/>
                        <small>{text[2]}</small></p></div>
                        <img alt="" src="{img}" /></div>
                    """

        except NoSuchElementException:
            break
    return '<div class="product-description-section">' + desc + '</div>'


def short_desc(driver):
    return '<ul>' + ''.join() + '</ul>'


def tech_desc(driver):
    return '<table id="plan_b" class="data-table"><tbody>' + ''.join() + '</tbody></table>'


def product_imgs(driver, product_folder_name_in, ean):
    imgs_links = driver.find_elements_by_xpath('//div[contains(@class, "mediagallery-wrapper")]//div[@class="slick-track" and contains(@style, "width: 3275px")]//source[@class="js_vp_3"]')
    imgs_links = [img.get_attribute('srcset') for img in imgs_links]
    imgs_links = ['https:' + img.split(', ')[0] for img in imgs_links if '.jpg' in img]

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def bosch_descriptions(link):
    driver = webdriver.Chrome('resources/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get(link)

    desc = description(driver)

    # short = short_desc(driver)
    # tech = tech_desc(driver)
    #
    return [desc, 'short', 'tech'], driver


@func_name
def BoschManage(full_product):
    full_product['manufacturer'] = ''
    full_product['pickup_store'] = '1,2,3...'
    full_product['descriptions'], driver = bosch_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(driver, full_product['product_folder_name_in'],
                                        full_product['sku'])

    driver.close()
# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Szuflada grzewcza BOSCH BIC630NB1  ', 'sku': '4242002813837', 'weight': '1', 'status': '2', 'manufacturer': '', 'url_key': 'Szuflada grzewcza BOSCH BIC630NB1  ', 'manufacturer_code': 'BIC630NB1', 'link_ceneo': '', 'pickup_store': '1,2,3...', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '177', 'supplier': '27', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://www.bosch-home.pl/lista-produktow/gotowanie-i-pieczenie/szuflady-grzewcze/BIC630NB1', 'product_folder_name_in': 'Bosch - BIC630NB1', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
