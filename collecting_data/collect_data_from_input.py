from collecting_data.set_attribute_set_ID import set_attribute_set_ID
from globals import timeit


def set_rule_ID(rule):
    rules = {
        '3MK': '60',
        '4CV': '62',
        'AARKE': '169',
        'AB_AGD': '124',
        'AB_RTV': '133',
        'AKG': '193',
        'ADLER': '166',
        'Aftershokz': '160',
        'AGD_MIELE_WOLNOSTOJACE': '55',
        'AGD_MIELE_ZABUDOWA': '44',
        'AGD_SAM_WOLNOSTOJACE': '51',
        'AGD_SAM_ZABUDOWA': '50',
        'AGD_SAM_ZAKAZ': '134',
        'AUDIO_EIC': '63',
        'AUDIO_HORN': '67',
        'AUTEL': '179',
        'BABYLISS': '151',
        'BEKO': '178',
        'BESTWAY': '191',
        'Blaupunkt': '185',
        'BOSCH': '177',
        'CityBlitz': '158',
        'CK_MEDIATOR': '127',
        'CORTLAND': '48',
        'CQE': '153',
        'DEFAULT': '180',
        'DJI': '121',
        'DRO': '187',
        'Dynacook': '162',
        'ELECTROLUX': '181',
        'Fiat 500': '164',
        'GARETT': '66',
        'GARMIN': '136',
        'GoPro': '161',
        'GRAEF': '141',
        'HUAWEI': '128',
        'JAMICON': '135',
        'KARCHER': '57',
        'KRYSIAK': '189',
        'LAPTOPY': '148',
        'LEGO': '154',
        'MAMIBOT': '142',
        'MICROSOFT': '123',
        'MODECOM': '113',
        'MONEUAL': '163',
        'MYPHONE': '188',
        'MY_ROBOT_CENTER': '149',
        'NINTENDO': '109',
        'Numatic': '186',
        'Orico': '159',
        'Overmax': '165',
        'PHILIPS': '171',
        'SAM_AKC': '61',
        'SAM_GUARD': '190',
        'SAM_KOMP': '118',
        'SAM_RTV': '69',
        'SAM_TAB': '54',
        'SAM_TEL': '59',
        'SANDISK / KINGSTON': '103',
        'SENCOR': '173',
        'SHARP': '131',
        'SHONA': '184',
        'SJCAM': '100',
        'SKYMASTER': '74',
        'SONY_ALL': '64',
        'SONY_GWARANCJE': '111',
        'SONY_MPI': '58',
        'SONY_PS': '56',
        'SONY_TEL': '53',
        'TCL': '170',
        'TECHLIFE': '175',
        'THOMSON': '172',
        'Thrustmaster': '156',
        'UCHWYTY_ELMAK': '39',
        'VENOM': '152',
        'WORTMANN': '140',
        'XBLITZ': '112',
        'XIAOMI': '157',
        'Yeticool': '176',
        'ZACO': '182',
        'ZENDURE': '174',
        '_OUTLET': '79',
        '__INNE': '183'
    }

    try:
        rule_ID = rules[rule]
    except KeyError:
        rule_ID = '0'

    return rule_ID


def set_supplier_ID(supplier):
    suppliers = {
        'AB': '2',
        'Morax': '3',
        'Matrix': '4',
        'SONY': '5',
        'Cortland': '6',
        'GALICJA': '7',
        'NAVIO': '8',
        'EIC': '9',
        'HORN': '10',
        'adansonia': '11',
        'Studio Hi-Fi': '12',
        'GARETT': '13',
        '(nie używany)': '14',
        'Lechpol': '15',
        '4CV': '16',
        'MIELE': '17',
        'AGED': '18',
        'NEONET': '19',
        'Hyper-Tel': '20',
        'skymaster': '21',
        'teka': '22',
        'dsv': '23',
        'ingram': '24',
        'afg': '25',
        'SATURN': '26',
        'Matrix .xls': '27',
        'redcon': '28',
        'ALSTOR': '29',
        'DJI': '30',
        'DRO': '31'
    }

    try:
        supplier_ID = suppliers[supplier]
    except KeyError:
        supplier_ID = '0'

    return supplier_ID


@timeit
def collect_data_from_input(product):
    """program rule and supplier ID given below"""

    full_product = {
        'descriptions': ['<p></p>', '', ''],
        'name': product[1],
        'sku': product[2].replace(' ', ''),
        'weight': '1',
        'status': '2',  # Nieaktywny, const
        'manufacturer': '0',  # 0 by default. It may be overwritten later
        'url_key': product[1].replace('+', 'plus'),
        'manufacturer_code': product[0],
        'link_ceneo': '',  # nothing by default. It may be overwritten later
        'pickup_store': '',  # nothing by default. It may be overwritten later
        'search_keywords': '',  # nothing by default. It may be overwritten later
        'search_priority': '',  # nothing by default. It may be overwritten later
        'price_negotiation_hide': '0',  # 0 by default. It may be overwritten later
        'question_form_show': '0',  # 0 by default. It may be overwritten later

        'price': '9999.99',  # 9999.99 by default. It may be overwritten later
        'tax_class_id': '0',  # Brak, const

        'rule': set_rule_ID(product[4]),  # 0 in default.
        'supplier': set_supplier_ID(product[5]),  # 0 in default.

        'export_ceneo': '1',  # 1 by default. It may be overwritten later

        'product_info_tabs_categories': '',  # nothing by default. It may be overwritten later

        'imgs': [],  # nothing by default. It may be overwritten later

        'link': product[6],
        # product folder will be changed by adding brand name on the left hand site
        'product_folder_name_in': ' - ' + ''.join(filter(str.isalnum, product[0])),

        'attribute_set_id': set_attribute_set_ID(product[1]),  # "Default" by default

        'forceSmallImg': False
    }

    return full_product
