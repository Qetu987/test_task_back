# read me 


## Installing

:shipit: [read](./install.md) for install project

<br>

## О проекте

В проекте 2 таблицы: ***Servis***, ***Subservice*** со связями один ко многим
<br>

на главном роуте ("[localhost/](http://127.0.0.1:8000/)") находится выпадающее меню в котором необходимо выбрать сревис, отображение сервиса модифицированно, добаленно кол-во подсервисов и общая сумма все подсервисов каждого сервиса.
<br>

Вибрав сервис и нажав на соответствующую кнопку, страница перезагружается и отображаются данные сервиса, подсервисы представленные в виде списка элементов в столбец
<br>

проект разделен на 2 директории: 
- главное "ядро" системы, где в настройках необходимо указать второстипенные директории
- main где описаны все модели, вью и собраны все шаблоны со статическими файлами
<br>

## Основные файлы
- [model.py](./main/models.py) содержит описание всех моделей проекта
- [admin.py](./main/admin.py) содержит описание моделей для админ панели, в ней указываются какие поля отображаются, по каким возможно производить поиск, фильтр и тд
- [urls.py](./test_task_core/urls.py) содержит описание всех роутов проекта
- [views.py](./main/views.py) содержит описание всех вью проекта, именно там происходит выборка из базы, сортировка, преображение данных и обработка get запроса

## Шаблонизация
Шаблонизация даного проекта происходит с помощью junja, весь код разметки разбит на части:
- шаблоны
- части сайта

Шаблоны имеют 2 фала:
- начальный, который содержит все первоначальные теги
- вызываемый, а котором описано, из каких частей состоит сйт

Части сайта дилятся на 2 части:
- выпадающее меню
- элементы подсервисов

## Админ панель
я не удалял базу, чтоб не было необходимости применять миграции и заново заполнять данные
<br>
<br>
для доступа в админ панель:
<br>
<br>
логин: ***admin***
<br>
пароль: ***admin***