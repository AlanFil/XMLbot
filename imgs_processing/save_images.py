
from tqdm import tqdm

from imgs_processing.ImgRefractor import prod_img


def save_images(imgs_links, product_folder_name_in, ean):
    imgs_links = list(dict.fromkeys(imgs_links))  # remove duplicates

    imgs_names = []
    print("INFO: Downloading product images...")
    for i in tqdm(range(len(imgs_links))):
        if imgs_links[i].strip() == '' or '.gif' in imgs_links[i]:
            continue

        if i == 0:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}-base', crop=False)
            imgs_names.append(f'{ean}-{i}-base.{file_type}')
        else:
            file_type = prod_img(product_folder_name_in, imgs_links[i], f'{ean}-{i}', crop=False)
            imgs_names.append(f'{ean}-{i}.{file_type}')

    return imgs_names
