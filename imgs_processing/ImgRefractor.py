"""
Funkcja desc_img:
- sprawdza czy ścieżka prowadzi do zdjęcia,
- weryfikuje rozszerzenie pliku. Jeżeli jest różne niż .jpg i .png, to wyświetla komunikat i próbuje zapisać plik w .jpg
- pobiera plik i dobiera szerokość do normy MatrixMedia (480 lub 1180px)
- zapisuje zdjęcie pod wskazaną ścieżką
"""

import requests
from PIL import Image, UnidentifiedImageError


def desc_img(product_folder_name, img_link, img_name, border=800, crop=False, force_small=False):
    try:
        res = requests.get(img_link)
    except:
        try:
            res = requests.get(img_link.replace('//', ''))
        except:
            try:
                res = requests.get('https://' + img_link)
            except:
                print(f'{img_link} - nie udało się pobrać zdjęcia z tego linku')
                return 0

    # zweryfikuj typ pliku
    if 'jpg' in img_link[-5:].lower():
        file_type = 'jpg'
    elif 'png' in img_link[-5:].lower():
        file_type = 'png'
    else:
        print('Rozszerzenie różne niż .jpg i .png. Przypisuję .jpg')
        print(img_link)
        file_type = 'jpg'

    IMAGE_PATH = f'bin/{product_folder_name}/description_imgs/{img_name}.{file_type}'
    # pobierz zdjęcie
    with open(IMAGE_PATH, 'wb') as file_format:
        file_format.write(res.content)

    try:
        im = Image.open(IMAGE_PATH)
    except UnidentifiedImageError:
        return 0

    # przytnij pustą przestrzeń
    if crop:
        im = im.crop(im.getbbox())

    # przeskalowanie do zdjęcia na pół ekranu lub cały
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

    # zapisz plik
    im.save(IMAGE_PATH)

    return file_type


def prod_img(product_folder_name, img_link, img_name, crop=False):
    res = requests.get(img_link)

    # zweryfikuj typ pliku
    if 'jpg' in img_link[-5:].lower():
        file_type = 'jpg'
    elif 'png' in img_link[-5:].lower():
        file_type = 'png'
    else:
        print('Rozszerzenie różne niż .jpg i .png. Przypisuję .jpg')
        print(img_link)
        file_type = 'jpg'

    IMAGE_PATH = f'bin/{product_folder_name}/product_imgs/{img_name}.{file_type}'
    # pobierz zdjęcie
    with open(IMAGE_PATH, 'wb') as file_format:
        file_format.write(res.content)

    try:
        im = Image.open(IMAGE_PATH)
    except UnidentifiedImageError:
        return 0

    # przytnij pustą przestrzeń
    if crop:
        im = im.crop(im.getbbox())

    # przeskalowanie do zdjęcia do rozmiarów na MatrixMedia
    width, height = im.size
    if width > 600:
        ratio = width / 600
        new_width = round(width / ratio)
        new_height = round(height / ratio)
        im = im.resize((new_width, new_height))

    # zapisz plik
    try:
        im.save(IMAGE_PATH)
    except OSError:
        print(f'OSError. Nie udało się zapisać zdjęcia: {img_link}')

    return file_type
