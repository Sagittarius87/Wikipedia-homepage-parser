from pydoc import classname
from unittest.main import main
import requests
from bs4 import BeautifulSoup


# Парсер главной страницы википедии
# https://ru.wikipedia.org/wiki/Заглавная_страница


# Отправка запроса для получения html кода главной страницы
def get_html(url):
    print('get_html start')
    resp = requests.get(url)
    return resp.text

# Создание экземпляра класса, содержащего данные из полученного html кода страницы, и поиск нужных элементов
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

# Основная функция, отправляющая запрос и разбирающая полученные данные из html кода
def main():
    print('main start')
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'
    print(get_data(get_html(url)))


# Проверка значения __name__ при запуске исходного файла как основной программы и запуск функции main() в случае True
if __name__ == '__main__':
    main()