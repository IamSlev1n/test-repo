from flask import Flask, request, abort, redirect, render_template_string
import logging
import random


app = Flask(__name__)


@app.route('/hello')
def hello():
    logging.info('Here is logging info')
    return 'Hello, world!'


@app.route('/users')
def users():
    names = ['Dmitro', 'Oleh', 'Andriy', 'Olga', 'Natalya', 'Sergiy']
    # Записуємо в змінну значення параметру count
    count = request.args.get('count')
    if count is not None:
        # ... перевіряємо чи воно числове ...
        try:
            count = int(count)
        # ... якщо значення не числове ...
        except ValueError:
            # ... видаємо помилку
            return 'В параметр "count" має бути передане число', 400
    else:
        # Генеруємо рандомне число від 1 до довжини списку імен
        count = random.randint(1, len(names))
    # Якщо значення параметру count 0 чи "негативне" видаємо помилку
    if count <= 0:
        return 'В параметр "count" має бути передане "позитивне" значення'
    # Перемішуємо список імен
    random.shuffle(names)
    # Повертаємо поєднані комою всі імена з сформованого і перемішаного списку
    return ', '.join(names[0:count])


@app.route('/users/<int:user_id>')
def get_user(user_id):
    # Перевіряємо чи ділиться айді користувача на 2 без залишку (тобто кратне 2)
    if user_id % 2 == 0:
        # Якщо так - повертаємо відформатований рядок
        return f'Це користувач з id {user_id}'
    else:
        # Якщо ні - повертаємо статус 404 Page not found
        return abort(404)


@app.route('/books')
def get_books():
    books = [
        'Harry Potter: Philosopher\'s Stone',
        'Harry Potter: Chamber of Secrets',
        'Harry Potter: Prisoner of Azkaban',
        'Harry Potter: Goblet of Fire',
        'Harry Potter: Order of the Phoenix',
        'Harry Potter: Half-Blood Prince',
        'Harry Potter: Deathly Hallows'
    ]
    # Записуємо в змінну значення параметру count
    count = request.args.get('count')
    # Якщо маємо значення параметру count ...
    if count is not None:
        # ... перевіряємо чи воно числове ...
        try:
            count = int(count)
        # ... якщо значення не числове ...
        except ValueError:
            # ... видаємо помилку
            return 'В параметр "count" має бути передане число', 400
    # Якщо значення параметру немає то лічильником буде рандомне число від 1 до довжини списку книг
    else:
        count = random.randint(1, len(books))
    # Якщо значення параметру count 0 чи "негативне" видаємо помилку
    if count <= 0:
        return 'В параметр "count" має бути передане "позитивне" значення'
    # Перемішуємо список книг
    random.shuffle(books)
    # Повертаємо список кожним рядком котрого буде назва книги зі списку
    # Довжина списку це значення переданого параметру count (якщо він є),
    # або рандомне число від 1 до довжини списку
    return '<ul>' + ''.join([f'<li>{book}</li>' for book in books[:count]]) + '</ul>'


@app.route('/books/<title>')
def get_book(title):
    # Переводимо першу літеру рядка у верхній регістр
    new_title = title.capitalize()
    return new_title


@app.route('/params')
def params():
    # Отримуємо query parameters з запиту
    params_dict = request.args.to_dict()
    # Генеруємо HTML таблицю з query parameters
    html = "<table>"
    # Генеруємо хедер таблиці
    html += "<tr><th>parameter</th><th>value</th></tr>"
    # Робимо цикл для перебору ключів і значень параметрів
    for key, value in params_dict.items():
        # додаємо до нашої таблиці ключі і значення у відповідні місця
        html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    html += "</table>"
    # Повертаємо згенеровану HTML таблицю
    return html


@app.route('/login', methods=['GET', 'POST'])
def login():
    # За замовчуванням отримуємо GET при переході на ендпоінт
    if request.method == 'GET':
        # Форма для вводу логіну і паролю
        form = '''<form method="post" style="text-align:center;margin-top:20%">
                <input type="text" name="username" placeholder="Username"><br><br>
                <input type="password" name="password" placeholder="Password"><br><br>
                <input type="submit" value="Submit">
            </form>'''
        # Яку ми повертаємо на GET запит
        return form
    # А якщо запит POST (тобто клікнута кнопка sumbit)
    elif request.method == 'POST':
        # Беремо данні з полів логіну і паролю
        username = request.form.get('username')
        password = request.form.get('password')
        # І якщо обидва поля були не пустими ...
        if username and password:
            # ... робимо редірект на іншу сторінку ...
            return redirect('/users')
        # ... а якщо хоч одне поле було пустим ...
        else:
            # Сповіщуємо про помилку і надаємо статус-код 400
            abort(400, 'Відсутній логін або пароль')


@app.errorhandler(404)
def page_not_found(e):
    return '''<div style="
                          width:100%;
                          height:100%;
                          background:black;
                          color:red;
                          font-size:100px;
                          text-align:center;
                          padding-top:20%
                          ">
                          Page not found
              </div>'''


@app.errorhandler(500)
def internal_server_error(e):
    return '''<div style="
                          width:100%;
                          height:100%;
                          background:red;
                          color:black;
                          font-size:100px;
                          text-align:center;
                          padding-top:20%
                          ">
                          Internal server error
              </div>'''


@app.route('/', methods=['GET'])
def home_page():
    links = [
        {'url': '/login', 'text': 'Login'},
        {'url': '/users', 'text': 'Users'},
        {'url': '/books', 'text': 'Books'},
        {'url': '/params', 'text': 'Params'}
    ]
    html = render_template_string('''
           <ul>
           {% for link in links %}
                <li style="color:black"><a href="{{ link.url }}">{{ link.text }}</a></li>
           {% endfor %} 
           </ul> 
    ''', links=links)
    return html


app.run()
