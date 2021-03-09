import re

from imgs_processing.ImgRefractor import desc_img


def download_imgs_and_replace_links(product_folder_name, description):
    for i, link in enumerate(re.findall('src=".*?"', description)):
        link = link.replace('src="', '').replace('"', '')

        img_type = desc_img(product_folder_name, link, i)

        description = description.replace(link, f'https://matrixmedia.pl/media/wysiwyg/{product_folder_name.replace(" - ", "/")}/{i}.{img_type}')
