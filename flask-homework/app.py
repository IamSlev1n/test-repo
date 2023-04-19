from flask import Flask, request, abort, redirect,render_template, session
import logging
import random
from key import secret_key


app = Flask(__name__, template_folder='templates')
app.secret_key = secret_key


@app.route('/hello')
def hello():
    logging.info('Here is logging info')
    return 'Hello, world!'


@app.route('/users')
def users():
    username = session.get('username')
    if not username:
        return redirect('/login')
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
    # Повертаємо зформований і перемішаний список імен
    return render_template('users.html', names=names[0:count], username=username)


@app.route('/users/<int:user_id>')
def get_user(user_id):
    username = session.get('username')
    if not username:
        return redirect('/login')
    # Перевіряємо чи ділиться айді користувача на 2 без залишку (тобто кратне 2)
    if user_id % 2 == 0:
        # Якщо так - повертаємо відформатований рядок у темплейті
        return render_template('users_id.html', user_id=user_id, username=username)
    else:
        # Якщо ні - повертаємо статус 404 Page not found
        return abort(404)


@app.route('/books')
def get_books():
    username = session.get('username')
    if not username:
        return redirect('/login')
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
    # Повертаємо список в темлейті, кожним рядком котрого буде назва книги зі списку
    # Довжина списку це значення переданого параметру count (якщо він є),
    # або рандомне число від 1 до довжини списку
    return render_template('books.html', books=books[:count], count=count, username=username)


@app.route('/books/<title>')
def get_book(title):
    username = session.get('username')
    if not username:
        return redirect('/login')
    # Переводимо першу літеру рядка у верхній регістр
    new_title = title.capitalize()
    return render_template('books_title.html', new_title=new_title, username=username)


@app.route('/params')
def params():
    username = session.get('username')
    if not username:
        return redirect('/login')
    # Отримуємо query parameters з запиту
    params_dict = request.args.to_dict()
    # Якщо параметри були пустими ...
    if not params_dict:
        names = ['Dmitro', 'Oleh', 'Andriy', 'Olga', 'Natalya', 'Sergiy']
        ages = random.randint(18, 55)
        cities = ['Kyiv', 'Lviv', 'Odessa', 'Chernigiv', 'Brovary', 'Kharkiv']
        # ... генеруємо рандомні параметри
        params_dict = {
            'name': random.choice(names),
            'age': ages,
            'city': random.choice(cities)
        }
    return render_template('params.html', params_dict=params_dict, username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = session.get('username')
    if username:
        return render_template('current_user.html', username=username)
    # За замовчуванням отримуємо GET при переході на ендпоінт
    if request.method == 'GET':
        return render_template('login.html')
    # А якщо запит POST (тобто клікнута кнопка sumbit)
    elif request.method == 'POST':
        # Беремо данні з полів логіну і паролю
        username = request.form.get('username')
        password = request.form.get('password')
        # І якщо обидва поля були не пустими ...
        if username and password:
            # ... робимо редірект на головну сторінку записавши username в сессію ...
            session['username'] = username
            return redirect('/')
        # ... а якщо хоч одне поле було пустим ...
        else:
            # Сповіщуємо про помилку і надаємо статус-код 400
            return render_template('login.html', error="Відсутній логін або пароль", username=username), 400


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
    username = session.get('username')
    if not username:
        return redirect('/login')
    # Бібліотека посилань для головної сторінки
    links = [
        {'url': '/login', 'text': 'Login'},
        {'url': '/users', 'text': 'Users'},
        {'url': '/books', 'text': 'Books'},
        {'url': '/params', 'text': 'Params'}
    ]
    # Виводимо посилання списком у темлейті
    return render_template('homepage.html', links=links, username=username)


@app.route('/logout')
def logout():
    # Функція що при кліку по кнопці Log out стирає ім`я користувача з сесії ...
    session.pop('username', None)
    # ...і робить редірект на сторінку авторизації
    return redirect('/login')


app.run()
