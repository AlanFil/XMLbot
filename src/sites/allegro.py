import requests
from scrapy import Selector

from src.globals import func_name
from src.imgs_processing.SaveImages import save_images


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('//img[@role="presentation"]/@src').extract()]

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


@func_name
def allegro_manage(full_product):
    full_product['manufacturer'] = '195'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = ['<div class="product-description-section"></div>', '', '']
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'],
                                        full_product['sku'])

# full_product =
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
