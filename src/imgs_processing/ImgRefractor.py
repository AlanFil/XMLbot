"""
Funkcja desc_img:
- sprawdza czy ścieżka prowadzi do zdjęcia,
- weryfikuje rozszerzenie pliku. Jeżeli jest różne niż .jpg i .png, to wyświetla komunikat i próbuje zapisać plik w .jpg
- pobiera plik i dobiera szerokość do normy MatrixMedia (480 lub 1180px)
- zapisuje zdjęcie pod wskazaną ścieżką
"""

import requests
from PIL import Image, UnidentifiedImageError


def DescImg(product_folder_name, img_link, img_name, border=800, crop=False, force_small=False):
    try:
        res = requests.get(img_link)
    except:
        try:
            res = requests.get(img_link.replace('//', 'https://', 1))
        except:
            try:
                res = requests.get('https://' + img_link)
            except:
                print(f'{img_link} - nie udało się pobrać zdjęcia z tego linku')
                return 0

    # verify file type
    if 'svg' in img_link.lower():
        file_type = 'svg'
    elif 'jpg' in img_link[-5:].lower() or 'jpeg' in img_link[-5:].lower():
        file_type = 'jpg'
    elif 'png' in img_link[-5:].lower():
        file_type = 'png'
    elif 'gif' in img_link[-5:].lower():
        file_type = 'gif'
    else:
        print('Rozszerzenie różne niż .jpg, .png, .svg i .gif. Przypisuję .jpg: ' + img_link)
        file_type = 'jpg'

    IMAGE_PATH = f'bin/{product_folder_name}/description_imgs/{img_name}.{file_type}'

    # download an image
    with open(IMAGE_PATH, 'wb') as file_format:
        file_format.write(res.content)

    if file_type == 'gif':
        return file_type

    try:
        im = Image.open(IMAGE_PATH)
    except UnidentifiedImageError:
        return file_type

    # crop empty area
    if crop:
        im = im.crop(im.getbbox())

    # scaling image to half- or fullscreen width
    width, height = im.size
    # size = 'full'
    ratio = 1
    if width < border or force_small:
        ratio = width / 480
        # size = 'half'
    elif width > 1180:
        ratio = width / 1180

    if ratio != 1:
        new_width = round(width / ratio)
        new_height = round(height / ratio)
        im = im.resize((new_width, new_height))

    # save image changes
    try:
        im.save(IMAGE_PATH)
    except OSError:
        print('Nie udało się zapisać zdjęcia: ' + img_link)

    return file_type


def prod_img(product_folder_name, img_link, img_name, crop=False):
    res = requests.get(img_link)

    # verify file type
    if 'jpg' in img_link[-5:].lower():
        file_type = 'jpg'
    elif 'png' in img_link[-5:].lower():
        file_type = 'png'
    else:
        print('Rozszerzenie różne niż .jpg i .png. Przypisuję .jpg')
        print(img_link)
        file_type = 'jpg'

    IMAGE_PATH = f'bin/{product_folder_name}/product_imgs/{img_name}.{file_type}'
    IMAGE_PATH_RAW = f'bin/{product_folder_name}/product_imgs_raw/{img_name}.{file_type}'
    # download an image
    with open(IMAGE_PATH, 'wb') as file_format:
        file_format.write(res.content)
    # download an image that will not be modified
    with open(IMAGE_PATH_RAW, 'wb') as file_format:
        file_format.write(res.content)

    try:
        im = Image.open(IMAGE_PATH)
    except UnidentifiedImageError:
        return 0

    # crop empty area
    if crop:
        im = im.crop(im.getbbox())

    # scaling photo for MatrixMedia sizes
    width, height = im.size
    if width > 600:
        ratio = width / 600
        new_width = round(width / ratio)
        new_height = round(height / ratio)
        im = im.resize((new_width, new_height))

    if height > 600:
        ratio = height / 600
        new_width = round(width / ratio)
        new_height = round(height / ratio)
        im = im.resize((new_width, new_height))

    result = Image.new(im.mode, (600, 600), (255, 255, 255))
    width, height = im.size
    paste_position = (
        (600 - width)//2,
        (600 - height)//2
    )
    result.paste(im, paste_position)

    # save changed image
    try:
        result.save(IMAGE_PATH)
    except OSError:
        print(f'WARNING: OSError. Could save a photo: {img_link}')

    return file_type
