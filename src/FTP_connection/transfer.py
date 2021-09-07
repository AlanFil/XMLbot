import base64
import ftplib
import os

from src.globals import timeit
from src.secrets import FTP_PASS_MM, FTP_USER_MM, FTP_HOST_MM


def MakeFTPConnection():
    FTP_HOST = FTP_HOST_MM
    FTP_USER = FTP_USER_MM

    # (1) decode password
    base64_message = FTP_PASS_MM
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    FTP_PASS = message_bytes.decode('ascii')

    # (2) make connection
    FTP = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    FTP.encoding = "utf-8"

    return FTP


def CloseFTPConnection(FTP):
    FTP.quit()


@timeit
def SendDescriptionImgsViaFTP(FTP, brand, product_folder_name):
    # move to proper folder in FTP
    try:
        FTP.mkd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}")
    except ftplib.error_perm:
        print(f'INFO: Folder {brand} already exists')
    finally:
        FTP.cwd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}")
    try:
        FTP.mkd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}/{product_folder_name}")
    except ftplib.error_perm:
        print(f'INFO: Folder {product_folder_name} already exists')
    finally:
        FTP.cwd(f"/domains/matrixmedia.pl/public_html/current/files/products/{brand}/{product_folder_name}")

    description_imgs_path = f'bin\\{brand} - {product_folder_name}\\description_imgs'
    for filename in os.listdir(description_imgs_path):
        with open(f'{description_imgs_path}\\{filename}', 'rb') as file:
            FTP.storbinary("STOR " + filename, file)


@timeit
def SendXMLViaFTP(FTP, xml_file_name):
    # sending an XML file
    FTP.cwd('/domains/matrixmedia.pl/public_html/import_products/xmls')
    with open(f'bin\\{xml_file_name}', 'rb') as file:
        FTP.storbinary("STOR " + xml_file_name, file)


@timeit
def SendProductsImgsViaFTP(FTP, product_file_path):
    # sending product imgs
    FTP.cwd('/domains/matrixmedia.pl/public_html/import_products/pictures')
    product_imgs_path = f'bin\\{product_file_path}\\product_imgs'
    for filename in os.listdir(product_imgs_path):
        with open(f'{product_imgs_path}\\{filename}', 'rb') as file:
            FTP.storbinary("STOR " + filename, file)
