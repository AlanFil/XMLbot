"""
for i, ele in enumerate(desc):
    print(f'{i}. {ele}')

use: separate_by_tag(tag, txt)
eg.: separate_by_tag('span', desc[i])
"""
import requests
from scrapy import Selector

from src.globals import func_name
from src.imgs_processing.SaveImages import save_images


def Description(sel):
    desc_raw = sel.xpath('//*[@id="tab-description"]/*')

    desc = []
    for ele in desc_raw:
        to_skip = ele.extract().lower()
        to_skip2 = ''.join(ele.xpath('.//text()').extract()).lower().strip()
        to_skip3 = ''.join(ele.xpath('.//img').extract()).lower().strip()
        if '>opis' in to_skip or 'english version' in to_skip:
            continue
        if to_skip2 == '' and to_skip3 == '':
            continue

        title = ''.join(ele.xpath('.//h1//text()').extract())
        if title != '':
            desc.append(f'<div><h1 class="important-header" style="text-align: center;">{title}</h1></div>')

        if len(ele.xpath('.//div[contains(@class, "vc_col-sm-4")]')) == 3 or len(ele.xpath('.//div[contains(@class, "vc_col-sm-4")]')) == 6:
            elem_imgs = []
            elem_texts = []
            for element in ele.xpath('.//div[contains(@class, "vc_col-sm-4")]'):
                elem_imgs.append(''.join(element.xpath('.//img/@src').extract()))
                elem_texts_raw = element.xpath('.//div[contains(@id, "text-block")]//text()').extract()
                elem_texts_raw = [etr for etr in elem_texts_raw if etr.strip() != '']
                elem_texts.append('<br/>'.join(elem_texts_raw))

            desc.append(f"""<div class="three-in-row flex--row">
                                <ul>
                                <li><img src="{elem_imgs[0]}"/><span>{elem_texts[0]}</span></li>
                                <li><img src="{elem_imgs[1]}"/><span>{elem_texts[1]}</span></li>
                                <li><img src="{elem_imgs[2]}"/><span>{elem_texts[2]}</span></li>
                                </ul>
                            </div>""")
            if len(ele.xpath('.//div[contains(@class, "vc_col-sm-4")]')) == 6:
                desc.append(f"""<div class="three-in-row flex--row">
                                <ul>
                                <li><img src="{elem_imgs[3]}"/><span>{elem_texts[3]}</span></li>
                                <li><img src="{elem_imgs[4]}"/><span>{elem_texts[4]}</span></li>
                                <li><img src="{elem_imgs[5]}"/><span>{elem_texts[5]}</span></li>
                                </ul>
                            </div>""")
            continue

        if len(ele.xpath('.//img').extract()) == 2:
            try:
                header1, header2 = ele.xpath('.//div[contains(@id, "text-block")]').extract()
                img1, img2 = ele.xpath('.//img/@src').extract()

                desc.append(f"""<div class="two-col-asymmetrically">
                                <div class="left-side">{header1}</div>
                                <div class="right-side">{header2}</div>
                                </div>""")
                desc.append(f"""<div class="two-col-asymmetrically">
                                <img alt="" src="{img1}" />
                                <img alt="" src="{img2}" />
                                </div>""")
                continue
            except ValueError:
                pass

        content = '<br/><br/>'.join(ele.xpath('.//p//text()').extract()) + '<br/>' + '<br/>'.join(ele.xpath('.//ul').extract())
        try:
            img = ele.xpath('.//img/@src').extract()[0]
        except IndexError:
            img = ''

        if ele.xpath('.//p[contains(@class, "6")]'):
            desc.append(f"""<div class="two-col-asymmetrically"><div class="right-side"><p>{content}</p></div>
            <img alt="{title}" src="{img}" /></div>""")
        else:
            desc.append(f'<div><p style="text-align: center;">{content}</p></div>')
            if img != '':
                desc.append(f'<div style="text-align: center;"><img alt="{title}" src="{img}" /></div>')

    return '<div class="product-description-section">' + ''.join(desc) + '</div>'


def ShortDesc(sel):
    short_raw = sel.xpath('')

    short = []
    for i in range(len(short_raw)):
        pass

    return '<ul>' + ''.join(short) + '</ul>'


def TechDesc(sel):
    tech_raw = sel.xpath('')

    tech = []
    for i in range(len(tech_raw)):
        pass

    return '<table id="plan_b" class="data-table"><tbody>' + ''.join(tech) + '</tbody></table>'


def ProductImgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = [img for img in sel.xpath('//figure[contains(@class, "product-gallery")]//a/@href').extract()]

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


def SwissDescriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = Description(sel)
    # short = ShortDesc(sel)
    # tech = TechDesc(sel)

    return [desc, '', '']


@func_name
def swiss_manage(full_product):
    full_product['manufacturer'] = '7179'
    full_product['pickup_store'] = '1'
    full_product['descriptions'] = SwissDescriptions(full_product['link'])
    full_product['imgs'] = ProductImgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])

# full_product = {'descriptions': ['<p></p>', '', ''], 'name': 'Wyciskarka BM202 x JJ', 'sku': '2021062401', 'weight': '1', 'status': '2', 'manufacturer': '7179', 'url_key': 'Wyciskarka BM202 x JJ', 'manufacturer_code': 'BM202 x JJ', 'link_ceneo': '', 'pickup_store': '1', 'search_keywords': '', 'search_priority': '', 'price_negotiation_hide': '0', 'question_form_show': '0', 'price': '9999.99', 'tax_class_id': '0', 'rule': '0', 'supplier': '0', 'export_ceneo': '1', 'product_info_tabs_categories': '', 'imgs': [], 'link': 'https://4swiss.pl/produkt/wyciskarka-bm202xjj/', 'product_folder_name_in': '4swiss - BM202xJJ', 'attribute_set_id': '4', 'forceSmallImg': False}
# link = full_product['link']
# sel = Selector(text=requests.get(link).content)
