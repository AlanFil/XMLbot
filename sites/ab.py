from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from globals import func_name
from imgs_processing.SaveImages import SaveImages


def description(driver):
    try:
        desc = driver.find_element_by_xpath('//div[@class="desc"]//div[@class="prmDesc"]').get_attribute('innerHTML')
    except NoSuchElementException:
        desc = ''

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def tech_desc(driver):
    tech = driver.find_element_by_xpath('//table[@class="prmTab"]/tbody').get_attribute('innerHTML')

    tech = tech.replace('class="l"', 'class="c_left"').replace('class="v"', 'class="c_left"')
    tech = tech.replace('\n', '').replace('\t', '')
    tech = tech.replace('<p>', '').replace('</p>', '')

    return '<table id="plan_b" class="data-table"><tbody><tr class="specs_category"><td colspan="2">Specyfikacja</td></tr>' + ''.join(tech) + '</tbody></table>'


def product_imgs(driver, product_folder_name_in, ean):
    imgs_links = driver.find_elements_by_xpath('//div[@id="productImageScroll"]//div[@id="images"]//img')
    imgs_links = [img.get_attribute('src').replace('&w=80&h=80&m=square', '') for img in imgs_links]
    for img in imgs_links:
        img = 'https://cdn.ab.pl' + img if not img.startswith('https://cdn.ab.pl') else img

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names


def ab_descriptions(sku):
    driver = webdriver.Chrome('resources/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.abonline.pl/default/pl/_/')
    driver.find_element_by_name('login_login').send_keys('Milena')
    driver.find_element_by_name('login_passwd').send_keys('UQCcUT')
    driver.find_element_by_name('accept_cookie').click()
    driver.find_element_by_name('login_passwd').send_keys(Keys.ENTER)

    driver.find_element_by_id('inpSearchBoxPhrase').send_keys(sku)
    driver.find_element_by_id('inpSearchBoxPhrase').send_keys(Keys.ENTER)

    desc = description(driver)
    tech = tech_desc(driver)

    return [desc, '', tech], driver


@func_name
def ABManage(full_product):
    full_product['manufacturer'] = '7173'
    full_product['pickup_store'] = '1'
    full_product['descriptions'], driver = ab_descriptions(full_product['sku'])
    full_product['imgs'] = product_imgs(driver, full_product['product_folder_name_in'],
                                        full_product['sku'])

    driver.close()
