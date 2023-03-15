// создание div в котором будут лежать кнопки

const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.textAlign = 'center'

// переменная с рандомным числом для второй кнопки

let i = Math.floor((Math.random() * 1000)+1);


//создаем первую кнопку
['Додати в друзі'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-success';
    button.innerText = `${buttonName}`
    button.style.margin = '5px'
    myDiv.appendChild(button);
});

//создаем счетчик после первой кнопки
[''].map(spanName => {
    let span_counter = document.createElement('span');
    span_counter.innerText = `${spanName}${i}` ;
    span_counter.style.margin = '5px'
    span_counter.style.color = 'white';
    span_counter.style.background = '#2ecc71';
    span_counter.style.padding = '25px 80px'
    span_counter.disabled = true;
    myDiv.appendChild(span_counter);
});

//создаем вторую, третью и четвертую кнопки
['Написати повідомлення', 'Запропонувати роботу', 'Здати ДЗ'].map(buttonName => {
    let button_next = document.createElement('button');
    button_next.className = 'btn btn-success';
    button_next.innerText = `${buttonName}` ;
    button_next.style.margin = '5px'
    myDiv.appendChild(button_next);
});

//вставляем див с кнопками в нужный элемент на странице
document.getElementsByClassName('footer')[0].appendChild(myDiv);

// выбор первой кнопки, изменение ее значения и изменения значения счетчика
const btn = document.getElementsByTagName('button')[0];
//отслеживание события "клик" по первой кнопке
btn.onclick = (event) => {
    //изменение текста в первой кнопке при нажатии на нее
    event.target.innerText = `Очікується підтвердження`;
    //отключение первой кнопки после клика по ней
    event.target.style.background = 'gray';
    event.target.disabled = true;
    //увеличение счетчика на +1 при нажатии на первую кнопку
    document.getElementsByTagName('span')[0].innerText = `${++i}`;
};

//выбираем вторую кнопку чтобы менять ее фон по клику
const btn2 = document.getElementsByTagName('button')[1];

//переменная которая будет "флагом" для смены цвета по клику
let isDefault_flag = true;

//отслеживание события "клик" по второй кнопке
btn2.onclick = (event) => {
    //переводим переменную в противоположное значение
    isDefault_flag = !isDefault_flag
    //меняем цвет с дефолтного на красный при изменении значения переменной isDefault
    btn2.style.background = isDefault_flag ? '' : 'red';
};

//выбираем третью кнопку чтобы отслеживать клики на нее и менять видимость первой кнопки по клику на третью кнопку
const btn3 = document.getElementsByTagName('button')[2];
//переменная которая будет "флагом" для смены видимости первой кнопки по клику на третью кнопку
let isVisible_flag = true

//отслеживание события "клик" по третьей кнопке
btn3.onclick = (event) => {
    //переводим переменную в противоположное значение
    isVisible_flag = !isVisible_flag
    //меняем видимость первой кнопки с помощью style.display = 'none' либо возвращаем к дефолтному значению при повторном клике
    btn.style.display = isVisible_flag ? '' : 'none';
}


//выбираем четвертую кнопку
const btn4 = document.getElementsByTagName('button')[3];
//отслеживание события "клик" по четвертой кнопке
btn4.onclick = (event) => {
    //создаем переменную с обращением к телу нашей таблицы
    const tbody = document.getElementsByTagName('tbody')[0];
    //создаем новую строку
    const newRow = document.createElement('tr');
    //создаем новую ячейку
    const newCell = document.createElement('td')
    //обьединяем 4 ячейки в одну чтобы не сломать структуру нашей таблицы
    newCell.setAttribute('colspan', '4')
    //добавляем текст в ячейку
    newCell.textContent = 'Ця домашка ще не перевірена :)'
    //в созданную строку добавляем созданную обьединенную ячейку с текстом
    newRow.appendChild(newCell)
    //новую строку (в которой уже содержится наша ячейка) добавляем в тело нашей таблицы
    tbody.appendChild(newRow)
}

