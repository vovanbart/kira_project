### Проект
### Создать папку с проектом
- Запустить консоль: найди командную строку в меню пуск
- Далее с помощью `cd` и `ls` войти в эту папку
- `cd ..` возврат на папку обрано
- `cd <name>` переход в папку с именем name, пример `cd project`
- `ls` выводит содержимое данной папки
### Запустить виртуальное окружение
- `python -m venv venv`
- `venv\Scripts\activate`
### Установка Django
- `pip install Django`
### Создание проекта
- `django-admin startproject Blog`
- `python manage.py startapp blogs`
### Проверка, что все сработало как надо
- `python manage.py runserver`
Заходишь на http://127.0.0.1:8000 и проверяешь что проект запущен
### Далее меняешь setting.py как в github
### Создаешь blogs/models.py и заполняешь его как в git
- `python manage.py makemigrations`
- `python manage.py migrate`
### Создаешь blogs/admin.py и заполняешь
- `python manage.py createsuperuser` тут можешь указать любое имя и пароль, почту указывать необязательно
- `python manage.py runserver` после этого можешь перейти на http://127.0.0.1:8000/admin ввести данные пользователя и создать пару записей
### Заполнение проекта
### Переносишь весь код из файлов blogs/forms.py, blogs/views.py, blogs/urls.py, Blog/urls.py, создаешь папку templates в папке blogs и переносишь файлы base.html, index.html, post_form.html, register.html
### Переходишь в командную строку и нажимаешь ctrl+C и снова пишешь `python manage.py runserver`
### Проверяешь, что все работает

