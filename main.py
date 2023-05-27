from pydoc import classname
from unittest.main import main
import requests
from bs4 import BeautifulSoup


# Парсер главной страницы википедии
# https://ru.wikipedia.org/wiki/Заглавная_страница


# Отправка запроса для получения html кода главной страницы
def get_html(url):
    print('get_html start')
    #headers = {
    #'User-Agent': 'My User Agent 1.0',
    #'From': 'Jarik-87@yandex.ru'  
    #}
    #http_proxy  = "http://10.10.1.10:3128"
    #https_proxy = "https://10.10.1.11:1080"
    #ftp_proxy   = "ftp://10.10.1.10:3128"
    #proxies = {
    #          "http"  : http_proxy,
    #          "https" : https_proxy,
    #          "ftp"   : ftp_proxy
    #        }   
    #resp = requests.get(url, headers=headers, proxies=proxies)
    resp = requests.get(url)
    return resp.text

# Поиск всех видимых на главной станице абзацев статей
def get_all_paragraphs(get_article_text):
    all_paragraphs_text = ''
    for p in get_article_text:
        all_paragraphs_text = all_paragraphs_text + '\n' + p.text
    return all_paragraphs_text

# Получение текстовых данных из списков
def get_all_list(geted_list):
        result_list  = ''
        for element_of_list in geted_list:
            result_list = result_list + element_of_list.text + '\n'
        return result_list

# Извлечения колличества статей из найденной строки
def get_number_of_aricles(line_with_number):
    return line_with_number.split(' ')[1]

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
    print(get_number_of_aricles(number_of_selected_articles))

    print('------------------------------')

    good_article = soup_of_html.find('div', id='main-tga').find('div').text 
    print(good_article)
    good_article_title = soup_of_html.find('div', id='main-tga').find('h2').find('span', class_='mw-headline').find('a').text
    print(good_article_title)
    get_good_article_text = soup_of_html.find('div', id='main-tga').find_all('p')
    print(get_all_paragraphs(get_good_article_text))
    number_of_good_articles = soup_of_html.find('div', id='main-tga').find('span', class_='mw-ui-button mw-ui-quiet').text
    print(get_number_of_aricles(number_of_good_articles))

    print('------------------------------')

    last_favorites_list_title = soup_of_html.find('div', id='main-tfl').find_all('span')[0].text
    print(last_favorites_list_title)
    last_favorites_list = soup_of_html.find('div', id='main-tfl').find_all('h2')[0].text.lstrip()
    print(last_favorites_list)
    previous_favorites_list_title = soup_of_html.find('div', id='main-tfl').find_all('span')[1].text
    print(previous_favorites_list_title)
    previous_favorites_list = soup_of_html.find('div', id='main-tfl').find_all('h2')[1].text.lstrip()
    print(previous_favorites_list)
    
    print('------------------------------')

    image_of_day_title = soup_of_html.find('div', id='main-potd').find('span', id='Изображение_дня').text
    print(image_of_day_title)
    image_of_day_alt = soup_of_html.find('div', id='main-potd').find('img').get('alt')
    print(image_of_day_alt)
    image_of_day_src = soup_of_html.find('div', id='main-potd').find('img').get('src')
    print(image_of_day_src)

    print('------------------------------')

    from_new_materials_title = soup_of_html.find('div', id='main-dyk').find('div').text
    print(from_new_materials_title)
    do_you_know_title = soup_of_html.find('div', id='main-dyk').find('span', id='Знаете_ли_вы?').text
    print(do_you_know_title)
    do_you_know_list = soup_of_html.find('div', id='main-dyk').find_all('ul') #[0].text
    
    final_list_of_do_you_know = get_all_list(do_you_know_list)
    final_list_of_do_you_know = final_list_of_do_you_know.replace('Обсудить', '').replace('Предложения', '').replace('Архив', '').replace('Просмотр шаблона', '').rstrip()
    print(final_list_of_do_you_know)

    print('------------------------------')

    current_events_title = soup_of_html.find('span', id='Текущие_события').text
    print(current_events_title)
    current_topics_title = soup_of_html.find('div', class_='hlist').find('dl').find('dt').text
    print(current_topics_title)
    current_topics_list = soup_of_html.find('div', class_='hlist').find('dl').find_all('dd')
    final_list_of_current_topics = get_all_list(current_topics_list)
    final_list_of_current_topics = final_list_of_current_topics.replace(' | Недавно умершие', '')
    print(final_list_of_current_topics)
    curret_events_list = soup_of_html.find('div', id='main-cur').find('ul').find_all('li')
    final_list_of_current_events = get_all_list(curret_events_list)
    print(final_list_of_current_events)   

    print('------------------------------')

    on_this_day_title = soup_of_html.find('div', id='main-itd').find('div').text
    print(on_this_day_title)
    current_day_date = soup_of_html.find('div', id='main-itd').find('h2').find_all('span')[1].text
    print(current_day_date)
    of_this_day_list = soup_of_html.find('div', id='main-itd').find('ul').find_all('li')
    final_list_on_of_this_day = get_all_list(of_this_day_list)
    print(final_list_on_of_this_day)
    


    return selected_article

# Основная функция, отправляющая запрос и разбирающая полученные данные из html кода
def main():
    print('main start')
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'
    get_data(get_html(url))


# Проверка значения __name__ при запуске исходного файла как основной программы и запуск функции main() в случае True
if __name__ == '__main__':
    main()