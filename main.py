import xml.etree.ElementTree as xml
from time import gmtime, strftime
import os

from FTP_connection.transfer import *
from XML.create_XML import create_XML
from XML.preview_html import preview_html
from collect_data_from_sites import collect_data_from_sites
from collect_data_oyo import collect_data_oyo
from imgs_processing.download_imgs_and_replace_links import download_imgs_and_replace_links

if __name__ == '__main__':
    """ HARD CODE ALERT """
    products = """CP.QT.00004421.01	Ubezpieczenie DJI Care Refresh FPV - plan dwuletni (kod elektroniczny)	6941565908087	9999	DJI	DJI	https://rcpro.pl/product-pol-20077-DJI-Care-Refresh-FPV-dwuletni-plan-kod-elektroniczny.html?query_id=1
CP.FP.00000021.01	DJI FPV Fly More Kit 	6941565904027	9999	DJI	DJI	https://rcpro.pl/product-pol-20038-DJI-FPV-Fly-More-Kit.html?query_id=1
CP.QT.00004428.01	Ubezpieczenie DJI Care Refresh FPV 	6941565908162	9999	DJI	DJI	https://rcpro.pl/product-pol-20053-DJI-Care-Refresh-FPV.html?query_id=1
CP.QT.00004408.01	Ubezpieczenie DJI Care Refresh FPV (kod elektroniczny)	6941565907912	9999	DJI	DJI	https://rcpro.pl/product-pol-20078-DJI-Care-Refresh-FPV-kod-elektroniczny.html?query_id=1
CP.FP.00000019.01	Kontroler nadajnik DJI FPV	6941565904010	9999	DJI	DJI	https://rcpro.pl/product-pol-20066-Kontroler-nadajnik-DJI-FPV.html?query_id=1
CP.FP.00000023.01	Akumulator DJI FPV	6941565904041	9999	DJI	DJI	https://rcpro.pl/product-pol-20051-Akumulator-DJI-FPV.html?query_id=1
CP.FP.00000020.01	Kontroler DJI Motion Controller 	6941565910127	9999	DJI	DJI	https://rcpro.pl/product-pol-20036-DJI-Motion-Controller-Przedsprzedaz.html?query_id=2
CP.FP.00000025.01	Gimbal z kamerą DJI FPV	6941565904065	9999	DJI	DJI	https://rcpro.pl/product-pol-20048-Gimbal-z-kamera-DJI-FPV.html?query_id=2
CP.FP.00000039.01	Ładowarka samochodowa DJI FPV	6941565907738	9999	DJI	DJI	https://rcpro.pl/product-pol-20074-Ladowarka-samochodowa-DJI-FPV.html?query_id=2
CP.FP.00000036.01	Zasilacz AC DJI FPV	6941565904157	9999	DJI	DJI	https://rcpro.pl/product-pol-20062-Zasilacz-AC-DJI-FPV.html?query_id=1
CP.FP.00000035.01	Hub ładowania DJI FPV	6941565904140	9999	DJI	DJI	https://rcpro.pl/product-pol-20063-Hub-ladowania-DJI-FPV.html?query_id=2
CP.FP.00000030.01	Akumulator do gogli Akumulator DJI FPV Goggles	6941565904119	9999	DJI	DJI	https://rcpro.pl/product-pol-20050-Akumulator-DJI-FPV-Goggles.html?query_id=2
CP.FP.00000026.01	Osłony śmigieł DJI FPV	6941565904072	9999	DJI	DJI	https://rcpro.pl/product-pol-20069-Oslony-smigiel-DJI-FPV.html?query_id=2
CP.FP.00000041.01	Osłony ramion DJI FPV	6941565904164	9999	DJI	DJI	https://rcpro.pl/product-pol-20075-Oslony-ramion-DJI-FPV.html?query_id=2
CP.FP.00000032.01	Antena DJI FPV Goggles (Dual Band)	6941565904195	9999	DJI	DJI	https://rcpro.pl/product-pol-20073-Antena-DJI-FPV-Goggles-Dual-Band.html?query_id=2
CP.FP.00000024.01	Nóżki podwozia DJI FPV	6941565904058	9999	DJI	DJI	https://rcpro.pl/product-pol-20049-Nozki-podwozia-DJI-FPV.html?query_id=2
CP.FP.00000028.01	Górna osłona DJI FPV (2 sztuki)	6941565904096	9999	DJI	DJI	https://rcpro.pl/product-pol-20079-Gorna-oslona-DJI-FPV-2-sztuki.html?query_id=2
CP.FP.00000022.01	Śmigła DJI FPV	6941565904034	9999	DJI	DJI	https://rcpro.pl/product-pol-20056-Smigla-DJI-FPV.html?query_id=2
CP.FP.00000038.01	Kabel zasilający DJI FPV (USB-C)	6941565904133	9999	DJI	DJI	https://rcpro.pl/product-pol-20070-Kabel-zasilajacy-DJI-FPV-USB-C.html?query_id=2
CP.FP.00000034.01	Kabel zasilający do gogli DJI FPV Goggles (XT60)	6941565904126	9999	DJI	DJI	https://rcpro.pl/product-pol-20054-Kabel-zasilajacy-DJI-FPV-Goggles-XT60.html?query_id=1
CP.FP.00000029.01	Drążki kontrolera DJI FPV	6941565904102	9999	DJI	DJI	https://rcpro.pl/product-pol-20054-Kabel-zasilajacy-DJI-FPV-Goggles-XT60.html?query_id=1
CP.FP.00000027.01	Osłona gimbala DJI FPV	6941565904089	9999	DJI	DJI	https://rcpro.pl/product-pol-20068-Oslona-gimbala-DJI-FPV.html?query_id=2""".split('\n')
    # products = [['TEST', 'Samsung Próba generalna', '1234567891234', '9999', 'SAM_AKC', 'Matrix',
    #              'https://www.samsung.com/pl/lifestyle-tvs/the-sero/ls05t-43-inch-the-sero-4k-smart-tv-navy-blue-qe43ls05tauxxh/']]
    """ HARD CODE ALERT """

    # define an XML file to write products data inside
    root = xml.Element('Products')
    tree = None
    for product in products:  # quantitiy of products to add
        # (1) gather all necessary data on your own (oyo)
        full_product = collect_data_oyo(product.split('\t'))

        # (2) gather all necessary data from given page(s)
        collect_data_from_sites(full_product)

        # (3) preview description
        if preview_html(full_product['descriptions'][0]) == -1:
            continue

        # (4) download imgs from description and replace links
        download_imgs_and_replace_links(full_product['product_folder_name_in'], full_product['descriptions'][0])

        # (5) create XML out of collected data
        tree = create_XML(root, full_product)

    if tree is not None:
        xml_file_name = f'Products_{strftime("%Y%m%d%H%M%S", gmtime())}.xml'

        with open(f'bin\\{xml_file_name}', 'wb') as file:
            tree.write(file)

        folders = [folder for folder in os.listdir('bin') if
                   not folder.endswith('.xml') and len(folder.split(' - ')) == 2]

        for folder in folders:
            f = folder.split(' - ')
            FTP = make_FTP_connection()
            send_description_imgs_via_FTP(FTP, f[0], f[1])  # send description images via FTP
            send_products_imgs_via_FTP(FTP, folder)  # send product images via FTP
            send_XML_via_FTP(FTP, xml_file_name)  # send XML via FTP
            close_FTP_connection(FTP)
