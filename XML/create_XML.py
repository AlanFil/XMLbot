"""
adding element with attribute "base" equal to "True":
    xml.SubElement(imgs_el, 'image', attrib={'base': 'True'}).text = img
"""
import xml.etree.ElementTree as xml


def create_XML(root, full_product):
    params = xml.Element('Product')
    root.append(params)

    for key in full_product.keys():
        if key == 'imgs' and key == 'link' and key == 'product_folder_name_in':
            continue
        if isinstance(full_product[key], list):
            continue
        xml.SubElement(params, key).text = full_product[key]

    xml.SubElement(params, 'description').text = full_product['descriptions'][0]
    xml.SubElement(params, 'short_description').text = full_product['descriptions'][1]
    xml.SubElement(params, 'tech_description').text = full_product['descriptions'][2]

    imgs_el = xml.Element('images')
    params.append(imgs_el)
    for i, img in enumerate(full_product['imgs']):
        if i == 0:
            xml.SubElement(imgs_el, 'image').text = img
        else:
            xml.SubElement(imgs_el, 'image').text = img

    tree = xml.ElementTree(root)

    return tree
