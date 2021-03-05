import xml.etree.ElementTree as xml


def create_XML(product, descriptions, weight, pickup_store):
    root = xml.Element('Products')
    params = xml.Element('Product')
    root.append(params)

    xml.SubElement(params, "name").text = product[1]
    xml.SubElement(params, 'description').text = descriptions[0]
    xml.SubElement(params, 'short_description').text = descriptions[1]
    xml.SubElement(params, 'tech_description').text = descriptions[2]
    xml.SubElement(params, 'sku').text = product[2]
    xml.SubElement(params, 'weight').text = str(weight)
    xml.SubElement(params, 'status').text = "2"  # Nieaktywny
    xml.SubElement(params, 'url_key').text = product[1].replace('+', 'plus')
    xml.SubElement(params, 'manufacturer').text = '246'
    xml.SubElement(params, 'manufacturer_code').text = product[0]
    xml.SubElement(params, 'pickup_store').text = ','.join(pickup_store)  # comma separated

    xml.SubElement(params, 'price').text = "9999.99"  # conts
    xml.SubElement(params, 'tax_class_id').text = "0"  # conts - Brak

    xml.SubElement(params, 'rule').text = "61"  # 61 - SAM_AKC
    xml.SubElement(params, 'supplier').text = "4"  # 4 - Matrix

    imgs = xml.Element('images')
    params.append(imgs)
    xml.SubElement(imgs, 'image', attrib={'base': 'True'}).text = "8806090973369-1.png"
    xml.SubElement(imgs, 'image').text = "8806090973369-2.png"

    tree = xml.ElementTree(root)

    with open('results.xml', 'wb') as files:
        tree.write(files)


if __name__ == '__main__':
    pr = 'EP-TA800NBEGEU	Ładowarka sieciowa SAMSUNG EP-TA800 25W czarna	8806090973369	9999	SAM_AKC	Matrix	https://www.samsung.com/pl/mobile-accessories/wall-charger-for-super-fast-charging-25w-black-ep-ta800nbegeu/'.split('\t')
    desc = ['long', 'short', 'tech']
    create_XML(pr, desc, 1, pickup_store=['1', '5', '6', '12', '13', '14', '15', '16', '17', '18', '19', '20', '23'])
