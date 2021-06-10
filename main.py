import xml.etree.ElementTree as xml
from time import gmtime, strftime

from FTP_connection.transfer import *
from XML.CreateXML import CreateXML
from XML.PreviewHTML import PreviewHTML
from collecting_data.collect_data_from_sites import CollectDataFromSites
from collecting_data.collect_data_oyo import CollectDataFromInput
from imgs_processing.DownloadImgsAndReplaceLinks import DownloadImgsAndReplaceLinks


def PrintDescriptions(full_product):
    print('PRINTING SCRAPPED DESCRIPTIONS...')
    print(full_product["descriptions"][0])
    print('-' * 15)
    print(full_product["descriptions"][1])
    print('-' * 15)
    print(full_product["descriptions"][2])
    print('-' * 15)


if __name__ == '__main__':
    """ HARD CODE ALERT """
    products = """51993781	Etui HUAWEI do P40 Pro czarne	6901443366033	9999	HUAWEI	Matrix	""".split('\n')

    send_via_FTP = True
    print_descriptions = False
    yes_to_all = True
    download_desc_images = False
    """ HARD CODE ALERT """

    # define an XML file to write products data inside
    root = xml.Element('Products')
    tree = None
    declined = []
    marked = []
    for product in products:
        # (1) gather all necessary data On Your Own (OYO)
        full_product = CollectDataFromInput(product.split('\t'))
        print(f"=============== {full_product['name']} ===============")

        # (2) gather all necessary data from given page(s)
        CollectDataFromSites(full_product)

        # (3) preview description
        preview_result = PreviewHTML(full_product, yes_to_all)
        if preview_result == -1:
            declined.append(full_product['sku'])
            continue
        elif preview_result == 1:
            marked.append(full_product['sku'])

        # (4) download imgs from description and replace links
        if download_desc_images:
            DownloadImgsAndReplaceLinks(full_product)

        # (5) create XML out of collected data
        tree = CreateXML(root, full_product)

        if print_descriptions:
            PrintDescriptions(full_product)

    if send_via_FTP and tree is not None:
        xml_file_name = f'Products_{strftime("%Y%m%d%H%M%S", gmtime())}.xml'

        with open(f'bin\\{xml_file_name}', 'wb') as file:
            tree.write(file)

        folders = [folder for folder in os.listdir('bin') if
                   not folder.endswith('.xml') and len(folder.split(' - ')) == 2]

        for folder in folders:
            f = folder.split(' - ')
            FTP = MakeFTPConnection()
            SendDescriptionImgsViaFTP(FTP, f[0], f[1])  # send description images via FTP
            SendProductsImgsViaFTP(FTP, folder)  # send product images via FTP
            SendXMLViaFTP(FTP, xml_file_name)  # send XML via FTP
            CloseFTPConnection(FTP)

    if marked:
        print(f'Marked by user: ')
        [print(f"{i}. {ele}") for i, ele in enumerate(marked)]

    if declined:
        print(f'Declined by user: ')
        [print(f"{i}. {ele}") for i, ele in enumerate(declined)]
    else:
        print('All products were added')
