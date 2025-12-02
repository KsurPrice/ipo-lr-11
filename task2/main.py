import requests                 # Импортируем библиотеку requests для загрузки HTML-страницы
from bs4 import BeautifulSoup   # Импортируем BeautifulSoup для парсинга HTML

def fetch_news():
    """
    Функция парсит сайт Hacker News и возвращает список новостей.
    Каждая новость содержит: id, title, comments, link.
    """
    url = "https://news.ycombinator.com/"   # Адрес сайта Hacker News
    response = requests.get(url)            # Делаем HTTP-запрос и получаем HTML-страницу
    soup = BeautifulSoup(response.text, "html.parser")  # Создаём объект BeautifulSoup для разбора HTML

    titles = soup.select(".titleline a")    # Находим все заголовки новостей (селектор CSS)
    comments = soup.select(".subline a:last-child")  # Находим ссылки на комментарии (последний <a> в блоке subline)

    news_list = []                          # Создаём пустой список для хранения новостей
    for i, (title, comment) in enumerate(zip(titles, comments), start=1):  
        # Перебираем заголовки и комментарии одновременно, нумерация начинается с 1

        comment_text = comment.text         # Получаем текст ссылки на комментарии
        if "comment" in comment_text:       # Проверяем, есть ли слово "comment" (значит это ссылка на комментарии)
            count = comment_text.split()[0] # Берём число комментариев (первое слово в строке)
        else:
            count = "0"                     # Если комментариев нет, ставим 0

        news_list.append({                  # Добавляем словарь с данными новости в список
            "id": i,                        # Номер новости
            "title": title.text,            # Заголовок новости
            "comments": count,              # Количество комментариев
            "link": title["href"]           # Ссылка на саму новость
        })

    return news_list                        # Возвращаем список новостей

def main():
    print("Введите количество новостей для отображения:")  # Просим пользователя ввести число
    try:
        n = int(input("> "))                # Читаем ввод и преобразуем в число
    except ValueError:                      # Если введено не число
        print("Ошибка: нужно ввести число.")  # Сообщаем об ошибке
        return                              # Завершаем выполнение программы

    news = fetch_news()[:n]                 # Получаем список новостей и берём первые n штук

    print("\nРезультаты:")                  # Выводим заголовок для результатов
    for item in news:                       # Перебираем каждую новость
        print(f"{item['id']}. Title: {item['title']}; Comments: {item['comments']};")  
        # Форматированный вывод: номер, заголовок и количество комментариев

if __name__ == "__main__":                  # Проверяем, что файл запущен напрямую
    main()                                  # Запускаем функцию main()
