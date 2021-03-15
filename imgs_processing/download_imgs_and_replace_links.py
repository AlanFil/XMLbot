import re

from tqdm import tqdm

from imgs_processing.ImgRefractor import desc_img


def download_imgs_and_replace_links(product_folder_name, description):
    links = re.findall('src=".*?"', description)
    for i in tqdm(range(len(links))):
        links[i] = links[i].replace('src="', '').replace('"', '')

        img_type = desc_img(product_folder_name, links[i], i)

        description = description.replace(links[i], f'https://matrixmedia.pl/media/wysiwyg/{product_folder_name.replace(" - ", "/")}/{i}.{img_type}')
