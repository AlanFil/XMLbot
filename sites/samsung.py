import requests
from scrapy import Selector
import re
from imgs_processing.ImgRefractor import prod_img
from tqdm import tqdm


def description(sel):
    print('Zbieranie danych z opisu')
    benefit = sel.xpath('//*[@id="benefit"]/*').extract()
    benefit = [ele.replace('\n', '').replace('\t', '') for ele in benefit if not ele.startswith('<input')]

    for i in tqdm(range(len(benefit))):
        size = 'big'
        if 'class="product-summary__list-item"' in benefit[i]:
            # should implement description element of 3 elems in row here
            benefit[i] = ''
            continue

        if 'class="swiper-wrapper"' in benefit[i]:
            # should implement description element of slider here
            benefit[i] = ''
            continue

        if 'three-column-carousel' in benefit[i] or 'feature-benefit-full-bleed' in benefit[i] or \
                'feature-benefit-text-only' in benefit[i] or 'video' in benefit[i]:
            benefit[i] = ''
            continue

        for ele in re.findall(r'<input.*?>', benefit[i]):
            benefit[i] = benefit[i].replace(ele, '')
        for ele in re.findall(r'<button.*?</button>', benefit[i]):
            benefit[i] = benefit[i].replace(ele, '')

        if re.findall(r'<div class="feature-benefit__img-wrap">.*?</div>', benefit[i]):
            ele = re.findall(r'<div class="feature-benefit__img-wrap">.*?</div></div>', benefit[i])

            src = [y for y in re.findall(r'src=".*?"', ele[0]) if 'LazyLoad' not in y][0]
            benefit[i] = benefit[i].replace(ele[0], f'<img {src}>')

        for ele in re.findall(r'<div.*?>', benefit[i]):
            if 'align' in ele:
                size = 'small'
                benefit[i] = benefit[i].replace(ele, '<div class="two-col-asymmetrically">', 1)
            elif 'feature-benefit ' in ele:
                size = 'big'
                benefit[i] = benefit[i].replace(ele, '<div>', 1)
                benefit[i] = benefit[i].replace('<h2', '<h1').replace('</h2>', '</h1>')

            elif 'text-wrap' in ele:
                benefit[i] = benefit[i].replace(ele, '<div class="right-side">', 1) if i % 2 == 0 \
                    else benefit[i].replace(ele, '<div class="left-side">', 1)

        for ele in re.findall(r'<h1.*?>', benefit[i]):
            benefit[i] = benefit[i].replace(ele, '<h1 class="important-header" style="text-align: center;">')

        for ele in re.findall(r'<h2.*?>', benefit[i]):
            benefit[i] = benefit[i].replace(ele, '<h2 class="important-header">')

        for ele in re.findall(r'<h3.*?>', benefit[i]):
            if size == 'small':
                benefit[i] = benefit[i].replace(ele, '<h3 style="font-weight: bold; font-size:large;">')
            benefit[i] = benefit[i].replace(ele, '<h3 style="text-align: center; font-weight: bold; font-size:large;">')
            benefit[i] = benefit[i].replace('</h3>', '</h3><br/>')

        for ele in re.findall(r'<p.*?>', benefit[i]):
            benefit[i] = benefit[i].replace(ele, '<p>')

        if '<p>*' in benefit[i]:
            benefit[i] = benefit[i].replace('<p>*', '<p style="font-size: small;">*')

        for ele in re.findall(r'<div class="feature-benefit__disclaimer-wrap">.*?</div>', benefit[i]):
            benefit[i] = benefit[i].replace(ele, '')

        # for ele in re.findall(r'class="feature-benefit__desc-wrap"', benefit[i]):
        #     benefit[i] = benefit[i].replace(ele, 'style="font-size: small"')

        for ele in re.findall(r'<div class="feature-benefit__text">', benefit[i]):
            benefit[i] = benefit[i].replace(ele, '<div>')

    return '<div class="product-description-section">' + ''.join(benefit) + '</div>'


def short_desc(sel):
    short_desc_raw = sel.xpath('//ul[@class="dot-list"]/li')
    short = [f'<li>{"".join(ele.xpath(".//text()").extract()).strip()}</li>' for ele in short_desc_raw]
    short = '<ul>' + ''.join(short) + '</ul>'

    return short


def tech_desc(sel):
    tech = ['<table id="plan_b" class="data-table"><tbody>']
    elements = sel.xpath('//*[@id="specs"]//*[@class="spec-highlight__detail"]')
    for ele in elements:
        category = ele.xpath('.//h4[contains(@class, "_title")]//text()').extract()
        tech.append(f'<tr class="specs_category"><td colspan="2">{"".join(category)}</td></tr>')

        items = ele.xpath('.//*[contains(@class, "_item")]')
        for item in items:
            title = item.xpath('.//*[contains(@class, "_title")]//text()').extract()
            value = item.xpath('.//*[contains(@class, "_value")]//text()').extract()
            element = f'<tr><td class="c_left">{"".join(title)}</td>' \
                      f'<td class="c_left">{"".join(value)}</td></tr>'
            tech.append(element)
    tech.append('</tbody></table>')
    tech = ''.join(tech)

    return tech


def product_imgs(link, product_folder_name_in, ean):
    sel = Selector(text=requests.get(link).content)
    imgs_links = []
    for img in sel.xpath('//div[contains(@class, "pd-header-gallery")]//img/@data-desktop-src').extract():
        new_link = img.replace('//', 'https://').replace('$LazyLoad_Home', '').replace('$684_547', '')
        imgs_links.append(new_link)

    imgs_links = list(dict.fromkeys(imgs_links))  # remove duplicates
    imgs_names = []
    for i, img_link in enumerate(imgs_links):
        if i == 0:
            file_type = prod_img(product_folder_name_in, img_link, f'{ean}-{i}-base', crop=False)
            imgs_names.append(f'{ean}-{i}-base.{file_type}')
        else:
            file_type = prod_img(product_folder_name_in, img_link, f'{ean}-{i}', crop=False)
            imgs_names.append(f'{ean}-{i}.{file_type}')

    return imgs_names


def samsung_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


def samsung_manage(full_product):
    full_product['manufacturer'] = '246'
    full_product['pickup_store'] = '1,5,6,12,13,14,15,16,17,18,19,20,23'
    full_product['descriptions'] = samsung_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])
