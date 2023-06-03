import requests
from bs4 import BeautifulSoup
import datetime


# Парсер главной страницы википедии
# https://ru.wikipedia.org/wiki/Заглавная_страница


# Отправка запроса для получения html кода главной страницы
def get_html(url):
    resp = requests.get(url)
    return resp.text

# Поиск всех видимых на главной станице абзацев статей
def get_all_paragraphs(get_article_text):
    all_paragraphs_text = ''
    for p in get_article_text:
        all_paragraphs_text = all_paragraphs_text + p.text
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

def save_to_file(found_data):
    with open('data found.csv', 'a', encoding='utf-8') as csv_file:
        current_date = datetime.date.today()
        csv_file.write(str(current_date))
        csv_file.write('\n')
        for list_element in found_data:
            for key in list_element:
                csv_file.write(f"{key}: {list_element.get(key)}\n")
            csv_file.write('\n')    

# Создание экземпляра класса, содержащего данные из полученного html кода страницы, и поиск нужных элементов
def get_data(html):
    soup_of_html = BeautifulSoup(html, 'lxml')
    
    selected_article = soup_of_html.find('div', id='main-tfa').find('div').text
    selected_article_title = soup_of_html.find('div', id='main-tfa').find('h2').find('span', class_='mw-headline').find('a').text
    selected_article_text = soup_of_html.find('div', id='main-tfa').find_all('p')
    final_text_of_selected_article = get_all_paragraphs(selected_article_text)
    number_of_selected_articles = soup_of_html.find('div', id='main-tfa').find('span', class_='mw-ui-button mw-ui-quiet').text
    final_number_of_selected_articles = get_number_of_aricles(number_of_selected_articles)
    selected_article_data = {
        'Загаловок раздела': selected_article,
        'Название избранной статьи': selected_article_title,
        'Тект избранной статьи': final_text_of_selected_article,
        'Колличество избранных статей': final_number_of_selected_articles
    }
    
    good_article = soup_of_html.find('div', id='main-tga').find('div').text 
    good_article_title = soup_of_html.find('div', id='main-tga').find('h2').find('span', class_='mw-headline').find('a').text
    good_article_text = soup_of_html.find('div', id='main-tga').find_all('p')
    final_text_of_good_article = get_all_paragraphs(good_article_text) 
    number_of_good_articles = soup_of_html.find('div', id='main-tga').find('span', class_='mw-ui-button mw-ui-quiet').text
    final_number_of_good_articles = number_of_good_articles.split(' ')[0] 
    good_article_data = {
        'Загаловок раздела': good_article,
        'Название хорошей статьи': good_article_title,
        'Текст хорошей статьи': final_text_of_good_article,
        'Колличество хороших статей': final_number_of_good_articles
    }
    
    last_favorites_list_title = soup_of_html.find('div', id='main-tfl').find_all('span')[0].text
    last_favorites_list = soup_of_html.find('div', id='main-tfl').find_all('h2')[0].text.lstrip()
    previous_favorites_list_title = soup_of_html.find('div', id='main-tfl').find_all('span')[1].text
    previous_favorites_list = soup_of_html.find('div', id='main-tfl').find_all('h2')[1].text.lstrip()
    favorites_list_data = {
        'Первый загаловок раздела': last_favorites_list_title,
        'Последний избранный список': last_favorites_list,
        'Второй заголовок раздела': previous_favorites_list_title,
        'Предыдущий избранный список': previous_favorites_list
    }
        
    image_of_day_title = soup_of_html.find('div', id='main-potd').find('span', id='Изображение_дня').text
    image_of_day_alt = soup_of_html.find('div', id='main-potd').find('img').get('alt')
    image_of_day_src = soup_of_html.find('div', id='main-potd').find('img').get('src')
    image_of_day_text = soup_of_html.find('div', id='main-potd').find('p').text
    image_of_day_data = {
        'Загаловок раздела': image_of_day_title,
        'Название изображения': image_of_day_alt,
        'Ссылка': image_of_day_src,
        'Описпние': image_of_day_text
    }
    
    from_new_materials_title = soup_of_html.find('div', id='main-dyk').find('div').text
    do_you_know_title = soup_of_html.find('div', id='main-dyk').find('span', id='Знаете_ли_вы?').text
    do_you_know_list = soup_of_html.find('div', id='main-dyk').find_all('ul')
    final_list_of_do_you_know = get_all_list(do_you_know_list)
    final_list_of_do_you_know = final_list_of_do_you_know.replace('Обсудить', '').replace('Предложения', '').replace('Архив', '').replace('Просмотр шаблона', '').rstrip()
    from_new_materials_data = {
        'Загаловок раздела': from_new_materials_title,
        'Подзагаловок': do_you_know_title,
        'Список материалов': final_list_of_do_you_know
    }
    
    current_events_title = soup_of_html.find('span', id='Текущие_события').text
    current_topics_title = soup_of_html.find('div', class_='hlist').find('dl').find('dt').text
    current_topics_list = soup_of_html.find('div', class_='hlist').find('dl').find_all('dd')
    final_list_of_current_topics = get_all_list(current_topics_list)
    final_list_of_current_topics = final_list_of_current_topics.replace(' | Недавно умершие', '')
    curret_events_list = soup_of_html.find('div', id='main-cur').find('ul').find_all('li')
    final_list_of_current_events = get_all_list(curret_events_list)
    current_events_data = {
        'Загаловок раздела': current_events_title,
        'Подзаголовок': current_topics_title,
        'Актуальные темы': final_list_of_current_topics,
        'Текущие события': final_list_of_current_events
    }
    
    on_this_day_title = soup_of_html.find('div', id='main-itd').find('div').text
    current_day_date = soup_of_html.find('div', id='main-itd').find('h2').find_all('span')[1].text
    on_this_day_list = soup_of_html.find('div', id='main-itd').find('ul').find_all('li')
    final_list_of_on_this_day = get_all_list(on_this_day_list)
    on_this_day_data = {
        'Загаловок раздела': on_this_day_title,
        'Текущая дата': current_day_date,
        'События за текущую дату': final_list_of_on_this_day
    }
    
    return [selected_article_data, good_article_data, favorites_list_data, image_of_day_data, from_new_materials_data, current_events_data, on_this_day_data]

# Основная функция, отправляющая запрос и разбирающая полученные данные из html кода
def main():
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'
    found_data = get_data(get_html(url))
    save_to_file(found_data)

    
# Проверка значения __name__ при запуске исходного файла как основной программы и запуск функции main() в случае True
if __name__ == '__main__':
    main()