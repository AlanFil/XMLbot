import urllib.request
import requests
from scrapy import Selector
from keyboard import wait


def samsung(link):
    sel = Selector(text=requests.get(link).content)

    # with urllib.request.urlopen(link) as response:
    #     html = response.read().decode('utf-8')

    benefit = sel.xpath('//*[@id="benefit"]/*').extract()
    benefit = [ele for ele in benefit if not ele.startswith('<input')]

    for i, ele in enumerate(benefit):
        print(f'{i}. {ele}')
        wait('Enter')


if __name__ == '__main__':
    # link = 'https://www.samsung.com/pl/lifestyle-tvs/the-sero/ls05t-43-inch-the-sero-4k-smart-tv-navy-blue-qe43ls05tauxxh/'
    samsung('')
