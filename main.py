from pydoc import classname
from unittest.main import main
import requests
from bs4 import BeautifulSoup

def get_html(url):
    print('get_html start')
    resp = requests.get(url)
    return resp.text


def get_data(html):
    print('get_data start')
    soup_of_html = BeautifulSoup(html, 'lxml')

    
    div_main_box_subtitle = soup_of_html.find('div', id='main-tfa').find('div').text
    h2_main_header_main_box_header = soup_of_html.find('div', id='main-tfa').find('h2').find('span', class_='mw-headline').find('a').text
    p = soup_of_html.find('div', id='main-tfa').find('p').text
    
    print('---')
    print(div_main_box_subtitle)
    print(h2_main_header_main_box_header)
    print(p)
    print('---')
    
    return div_main_box_subtitle

def main():
    print('main start')
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()