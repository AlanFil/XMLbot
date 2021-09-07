import requests
from scrapy import Selector

from src.imgs_processing.SaveImages import SaveImages


def ProductImgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('').extract()]

    imgs_names = SaveImages(imgs_links, product_folder_name_in, ean)

    return imgs_names
