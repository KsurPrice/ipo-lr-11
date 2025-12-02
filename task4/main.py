import json   # Импортируем модуль json для чтения данных из файла data.json

def main():
    # Загружаем новости из файла data.json
    with open("data.json", "r", encoding="utf-8") as f:
        news = json.load(f)

    # Формируем HTML‑страницу
    html_content = """
    <html>
    <head>
        <title>Hacker News Parser</title> <!-- Заголовок страницы -->
        <style>
            /* Красивый фон: градиент от фиолетового к синему */
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(to right, #8e2de2, #4a00e0); 
                margin: 0; 
                padding: 20px;
                color: #fff; /* Белый текст для контраста */
            }
            h1 { 
                text-align: center; 
                color: #ffffff; 
            }
            table { 
                width: 90%; 
                margin: auto; 
                border-collapse: collapse; 
                box-shadow: 0 0 10px rgba(0,0,0,0.3);
                background: #ffffff; /* Белый фон таблицы */
                color: #000; /* Чёрный текст внутри таблицы */
            }
            th, td { 
                border: 1px solid #666; 
                padding: 10px; 
                text-align: left; 
            }
            th { 
                background: #d1c4e9; /* Светло-фиолетовый фон заголовков */
                font-weight: bold; 
            }
            tr:nth-child(even) { 
                background: #f3e5f5; /* Чередование строк */
            }
            a { 
                color: #0066cc; 
                text-decoration: none; 
            }
            a:hover { 
                text-decoration: underline; 
            }
        </style>
    </head>
    <body>
        <h1>Новости с Hacker News</h1> <!-- Заголовок внутри страницы -->
        <table>
            <tr><th>ID</th><th>Title</th><th>Comments</th><th>Link</th></tr>
    """

    # Добавляем строки таблицы для каждой новости
    for item in news:
        html_content += f"<tr><td>{item['id']}</td><td>{item['title']}</td><td>{item['comments']}</td><td><a href='{item['link']}'>Источник</a></td></tr>"

    # Завершаем HTML
    html_content += """
        </table>
    </body>
    </html>
    """

    # Записываем результат в файл index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML-страница создана: index.html")

if __name__ == "__main__":
    main()
