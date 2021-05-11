import re

import requests
from scrapy import Selector

from globals import func_name
from imgs_processing.save_images import save_images


def description(sel):
    benefit = sel.xpath('//*[@id="benefit"]/*').extract()
    benefit = [ele.replace('\n', '').replace('\t', '') for ele in benefit if not ele.startswith('<input')]

    for i in range(len(benefit)):
        direction = 'right' if i % 2 == 0 else 'left'
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

        benefit[i] = benefit[i].replace('<section', '<div').replace('</section', '</div')

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

        if re.findall(r'<div class="feature-benefit-half-text.*?</div>', benefit[i]):
            benefit[i] = benefit[i].replace(re.search(r'<div class="feature-benefit-half-text.*?>', benefit[i]).group(), '<div class="two-col-asymmetrically">')
            benefit[i] = benefit[i].replace('feature-benefit-half-text__content', f'{direction}-side')

            links = re.findall(r'data-desktop-src=".*?"', benefit[i])
            link = links[-1].replace('data-desktop-', '')

            benefit[i] = benefit[i].replace(re.search('<figure class="feature-benefit-half-text__figure">.*?</figure>', benefit[i]).group(), f'<img {link}/>')

        if re.findall(r'<div class="two-column.*?</div>', benefit[i]):
            benefit[i] = benefit[i].replace(re.search(r'<div class="two-column.*?>', benefit[i]).group(), '<div>')
            benefit[i] = benefit[i].replace('two-column__column', f'two-col-asymmetrically')
            benefit[i] = benefit[i].replace('two-column__content', f'{direction}-side')

            links = re.findall(r'data-desktop-src=".*?"', benefit[i])
            link = links[-1].replace('data-desktop-', '')

            benefit[i] = benefit[i].replace(re.search('<figure class="two-column__figure">.*?</figure>', benefit[i]).group(), f'<img {link}/>')

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

    imgs_names = save_images(imgs_links, product_folder_name_in, ean)

    return imgs_names


def samsung_descriptions(link):
    sel = Selector(text=requests.get(link).content)

    desc = description(sel)
    short = short_desc(sel)
    tech = tech_desc(sel)

    return [desc, short, tech]


@func_name
def samsung_manage(full_product):
    full_product['manufacturer'] = '246'
    full_product['pickup_store'] = '1,5,6,12,13,14,15,16,17,18,19,20,23'
    full_product['descriptions'] = samsung_descriptions(full_product['link'])
    full_product['imgs'] = product_imgs(full_product['link'], full_product['product_folder_name_in'], full_product['sku'])
