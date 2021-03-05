import ftplib
import xml.etree.ElementTree as xml
from time import gmtime, strftime
import os
import base64

STARTING_DIRECTORY = os.getcwd()


def create_product_folder(product_folder_name):
    pr_folder_path = f'{STARTING_DIRECTORY}\\bin\\{product_folder_name}'
    try:
        os.mkdir(pr_folder_path)
        os.mkdir(f'{pr_folder_path}\\product_imgs')
        os.mkdir(f'{pr_folder_path}\\description_imgs')
    except FileExistsError:
        print(f'Folder "{product_folder_name}" already exists in bin.')
        # return -1

    return pr_folder_path


def make_FTP_connection():
    FTP_HOST = "5.252.230.94"
    FTP_USER = "matrixmedia"

    # (1) decode password
    base64_message = 'WXpmOXkydU1zbnFldUtFYg=='
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    FTP_PASS = message_bytes.decode('ascii')

    # (2) make connection
    FTP = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    FTP.encoding = "utf-8"

    return FTP


def close_FTP_connection(FTP):
    FTP.quit()


def send_description_imgs_via_FTP(FTP, brand, product_folder_name):
    # move to proper folder in FTP
    try:
        FTP.mkd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}")
    except ftplib.error_perm:
        print(f'Folder {brand} already exists')
    finally:
        FTP.cwd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}")
    try:
        FTP.mkd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}/{product_folder_name}")
    except ftplib.error_perm:
        print(f'Folder {product_folder_name} already exists')
    finally:
        FTP.cwd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}/{product_folder_name}")

    description_imgs_path = f'{STARTING_DIRECTORY}\\bin\\{product_folder_name}\\description_imgs'
    for filename in os.listdir(description_imgs_path):
        with open(f'{description_imgs_path}\\{filename}', 'rb') as file:
            FTP.storbinary("STOR " + filename, file)


def send_product_via_FTP(FTP, product_file_path, xml_file_name):
    # sending an XML file
    FTP.cwd('/domains/matrixmedia.pl/public_html/import_products/xmls')
    with open(f'{product_file_path}\\{xml_file_name}', 'rb') as file:
        FTP.storbinary("STOR " + xml_file_name, file)

    # sending product imgs
    FTP.cwd('/domains/matrixmedia.pl/public_html/import_products/pictures')
    product_imgs_path = f'{product_file_path}\\product_imgs'
    for filename in os.listdir(product_imgs_path):
        with open(f'{product_imgs_path}\\{filename}', 'rb') as file:
            FTP.storbinary("STOR " + filename, file)


def create_XML(product_folder_name, product, descriptions, weight, manufacturer, pickup_store, imgs, ceneo_link='',
               search_keywords='',
               additional_description='', additional_description_from='', additional_description_to='',
               search_priority='', price_negotiation_hide='', question_form_show='', rule='', supplier='',
               export_ceneo='1', product_info_tabs_categories=None):
    if product_info_tabs_categories is None:
        product_info_tabs_categories = []

    root = xml.Element('Products')  #
    params = xml.Element('Product')  # setting "product" root
    root.append(params)  #

    xml.SubElement(params, "name").text = product[1]
    xml.SubElement(params, 'description').text = descriptions[0]
    xml.SubElement(params, 'short_description').text = descriptions[1]
    xml.SubElement(params, 'tech_description').text = descriptions[2]
    xml.SubElement(params, 'sku').text = product[2]
    xml.SubElement(params, 'weight').text = str(weight)
    xml.SubElement(params, 'status').text = "2"  # const - Nieaktywny
    xml.SubElement(params, 'manufacturer').text = manufacturer
    xml.SubElement(params, 'url_key').text = product[1].replace('+', 'plus')
    xml.SubElement(params, 'manufacturer_code').text = product[0]
    xml.SubElement(params, 'link_ceneo').text = ceneo_link
    xml.SubElement(params, 'pickup_store').text = ','.join(pickup_store)  # comma separated
    xml.SubElement(params, 'search_keywords').text = search_keywords
    xml.SubElement(params, 'additional_description').text = additional_description
    xml.SubElement(params, 'additional_description_from').text = additional_description_from
    xml.SubElement(params, 'additional_description_to').text = additional_description_to
    xml.SubElement(params, 'search_priority').text = search_priority
    xml.SubElement(params, 'price_negotiation_hide').text = price_negotiation_hide
    xml.SubElement(params, 'question_form_show').text = question_form_show

    xml.SubElement(params, 'price').text = "9999.99"  # conts
    xml.SubElement(params, 'tax_class_id').text = "0"  # conts - Brak

    xml.SubElement(params, 'rule').text = rule  # 61 - SAM_AKC
    xml.SubElement(params, 'supplier').text = supplier  # 4 - Matrix

    xml.SubElement(params, 'export_ceneo').text = export_ceneo

    xml.SubElement(params, 'product_info_tabs_categories').text = product_info_tabs_categories

    imgs_el = xml.Element('images')
    params.append(imgs_el)
    for i, img in enumerate(imgs):
        if i == 0:
            xml.SubElement(imgs_el, 'image', attrib={'base': 'True'}).text = img
        else:
            xml.SubElement(imgs_el, 'image').text = img

    tree = xml.ElementTree(root)

    product_file_path = f'bin\\{product_folder_name}\\'
    xml_file_name = f'Products_{strftime("%Y%m%d%H%M%S", gmtime())}.xml'
    try:
        with open(f'{product_file_path}\\{xml_file_name}', 'wb') as file:
            tree.write(file)
    except TypeError:
        print("There occurred an error during saving XML file")
        # return -1

    return product_file_path, xml_file_name


if __name__ == '__main__':
    """ HARD CODE ALERT """
    product_in = 'EP-TA800NBEGEU	Ładowarka sieciowa SAMSUNG EP-TA800 25W czarna	8806090973369	9999	SAM_AKC	Matrix	https://www.samsung.com/pl/mobile-accessories/wall-charger-for-super-fast-charging-25w-black-ep-ta800nbegeu/'.split(
        '\t')
    descriptions_in = ['long', 'short', 'tech']
    weight_in = 1
    manufacturer_in = '246'
    ceneo_link_in = ''
    pickup_store_in = ['1', '5', '6', '12', '13', '14', '15', '16', '17', '18', '19', '20', '23']
    imgs_in = ['8806090973369-1.png', '8806090973369-2.png']

    brand_in = 'Samsung'
    product_folder_name_in = 'EPTA800NBEGEU'
    """ HARD CODE ALERT """

    # (1) create folder with product data (for description images, product images and XML file)
    product_folder_path = create_product_folder(product_folder_name_in)

    # (2) gather all necessary data (description images, product images and for XML file)

    # (3) create XML out of collected data
    product_file_path, xml_file_name = create_XML(product_folder_name_in, product_in, descriptions_in, weight_in,
                                                  manufacturer_in, pickup_store_in, imgs_in, ceneo_link_in)

    FTP = make_FTP_connection()
    send_description_imgs_via_FTP(FTP, brand_in, product_folder_name_in)  # send images via FTP
    send_product_via_FTP(FTP, product_file_path, xml_file_name)  # send XML via FTP
    close_FTP_connection(FTP)
