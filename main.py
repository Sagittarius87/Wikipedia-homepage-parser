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

# Поиск всех видимых на главной станице абзацев статей
def get_all_paragraphs(get_article_text):
    all_paragraphs_text = ''
    for p in get_article_text:
        all_paragraphs_text = all_paragraphs_text + '\n' + p.text
    return all_paragraphs_text

# Создание экземпляра класса, содержащего данные из полученного html кода страницы, и поиск нужных элементов
def get_data(html):
    print('get_data start')
    soup_of_html = BeautifulSoup(html, 'lxml')
    
    selected_article = soup_of_html.find('div', id='main-tfa').find('div').text
    print(selected_article)
    selected_article_title = soup_of_html.find('div', id='main-tfa').find('h2').find('span', class_='mw-headline').find('a').text
    print(selected_article_title)
    get_selected_article_text = soup_of_html.find('div', id='main-tfa').find_all('p')
    print(get_all_paragraphs(get_selected_article_text))
    number_of_selected_articles = soup_of_html.find('div', id='main-tfa').find('span', class_='mw-ui-button mw-ui-quiet').text
    print(number_of_selected_articles.split(' ')[1])

    print('------------------------------')

    good_article = soup_of_html.find('div', id='main-tga').find('div').text 
    print(good_article)
    good_article_title = soup_of_html.find('div', id='main-tga').find('h2').find('span', class_='mw-headline').find('a').text
    print(good_article_title)
    get_good_article_text = soup_of_html.find('div', id='main-tga').find_all('p')
    print(get_all_paragraphs(get_good_article_text))



    return selected_article

# Основная функция, отправляющая запрос и разбирающая полученные данные из html кода
def main():
    print('main start')
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'
    get_data(get_html(url))


# Проверка значения __name__ при запуске исходного файла как основной программы и запуск функции main() в случае True
if __name__ == '__main__':
    main()