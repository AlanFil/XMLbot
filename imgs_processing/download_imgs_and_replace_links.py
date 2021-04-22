import re

from tqdm import tqdm

from imgs_processing.ImgRefractor import desc_img


def download_imgs_and_replace_links(full_product):
    links = re.findall('src=".*?"', full_product['descriptions'][0])

    for i in tqdm(range(len(links))):
        links[i] = links[i].replace('src="', '').replace('"', '')

        if links[i].strip() == '':
            continue

        img_type = desc_img(full_product['product_folder_name_in'], links[i], i, force_small=full_product['forceSmallImg'])

        new_img = f'https://matrixmedia.pl/files/products/{full_product["product_folder_name_in"].replace(" - ", "/")}/{i}.{img_type}'
        full_product['descriptions'][0] = full_product['descriptions'][0].replace(links[i], new_img)
