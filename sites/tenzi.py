"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector

from globals import func_name
from imgs_processing.SaveImages import SaveImages


@func_name
def tenzi_manage(full_product):
    full_product['manufacturer'] = '195'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = ['<p></p>', '', '']
    # full_product['imgs'] = ProductImgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])

# full_product =
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
