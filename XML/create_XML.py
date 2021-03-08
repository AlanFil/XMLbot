import xml.etree.ElementTree as xml


def create_XML(root, product_folder_name, product, descriptions, weight, manufacturer, pickup_store, imgs,
               ceneo_link='',
               search_keywords='',
               additional_description='', additional_description_from='', additional_description_to='',
               search_priority='', price_negotiation_hide='', question_form_show='', rule='', supplier='',
               export_ceneo='1', product_info_tabs_categories=None):
    if product_info_tabs_categories is None:
        product_info_tabs_categories = []

    params = xml.Element('Product')
    root.append(params)

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

    return tree