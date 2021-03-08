def collect_data(i):
    """ HARD CODE ALERT """
    if i == 1:
        full_product = {
            'product_in': ['PIERWSZY', 'TEN PIERWSZY', '8806090973369', '9999',
                           'SAM_AKC', 'Matrix',
                           'https://www.samsung.com/pl/mobile-accessories/wall-charger-for-super-fast-charging-25w-black-ep-ta800nbegeu/'],
            'descriptions_in': ['long1', 'short1', 'tech1'],
            'weight_in': 1,
            'manufacturer_in': '246',
            'ceneo_link_in': '',
            'pickup_store_in': ['1', '5', '6', '12', '13', '14', '15', '16', '17', '18', '19', '20', '23'],
            'imgs_in': ['1234567891111-1.jpg', '1234567891112-2.png'],
            'brand_in': 'Samsung',
        }
        full_product['product_folder_name_in'] = full_product['brand_in'] + ' - ' + full_product['product_in'][0]
    else:
        full_product = {
            'product_in': ['DRUGI', 'TEN DRUGI', '8806090973369', '9999',
                           'SAM_AKC', 'Matrix',
                           'https://www.samsung.com/pl/mobile-accessories/wall-charger-for-super-fast-charging-25w-black-ep-ta800nbegeu/'],
            'descriptions_in': ['long2', 'short2', 'tech2'],
            'weight_in': 2,
            'manufacturer_in': '246',
            'ceneo_link_in': '',
            'pickup_store_in': ['1', '5', '6', '12', '13', '14', '15', '16', '17', '18', '19', '20', '23'],
            'imgs_in': ['1111123456789-1.png'],
            'brand_in': 'Samsung',
        }
        full_product['product_folder_name_in'] = full_product['brand_in'] + ' - ' + full_product['product_in'][0]

    """ HARD CODE ALERT """
    return full_product
