# moodle_tests

[![Build Status](https://app.travis-ci.com/grsln/moodle_tests.svg?branch=main)](https://app.travis-ci.com/grsln/moodle_tests)

**Цель**: протестировать функционал модуля сайта https://qacoursemoodle.innopolis.university

Проект **moodle_tests** содержит проверки авторизации, изменения профиля пользователя и создания курсов.

### Начало работы

Процесс установки описан для Ubuntu

Создание и переход в директорию на локальном компьютере

```
mkdir moodle_test && cd moodle_tests
```

Клонирование файлов из удаленного репозитория
```
git clone https://github.com/grsln/moodle_tests
```

Создание и активация виртуального окружения

```
python3 -m venv venv
source venv/bin/activate
```

Установка зависимостей

```
pip install -r requirements.txt
```

Для создания отчетов по тестированию необходимо установить Allure(+Java)

```
# install Java
sudo apt update
sudo apt install default-jre -y
sudo apt install default-jdk -y
javac -version

# install allure
curl -o allure-2.13.8.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz
sudo tar -zxvf allure-2.13.8.tgz -C /opt/
sudo ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure
allure --version
```

### Запуск тестов

Запуск тестов с созданием отчетов

```
pytest --alluredir=allure_reports
```

Для просмотра результатов тестирования (отчеты Allure) необходимо выполнить

```
allure serve allure_reports
```

### Тесты

**Тестирование авторизации**

Запуск в файле [_test/auth/test_auth.py_](https://github.com/grsln/moodle_tests/blob/main/tests/auth/test_auth.py)

__тест-кейсы__: [на форму авторизации](https://docs.google.com/spreadsheets/d/1rftMQABAk7yvVuYu2hfgfOJXMNjlXUwZIAuwGGlStFw/edit#gid=0&range=A1:C1)

* проверка авторизации с валидными данными
* проверка авторизации с невалидными данными
  * пустой логин
  * пустой пароль
* проверка авторизации с неверным паролем

**Тестирование редактирования профиля пользователя**

Запуск в файле [_test/profile_page/test_user_page.py_](https://github.com/grsln/moodle_tests/blob/main/tests/profile_page/test_user_page.py)

__тест-кейсы__: [на форму редактирования профиля пользователя](https://docs.google.com/spreadsheets/d/1rftMQABAk7yvVuYu2hfgfOJXMNjlXUwZIAuwGGlStFw/edit#gid=1583827046&range=A1)

* проверка изменения обязательных полей
* проверка заполнения обязательных полей пустой строкой
* проверка длинных имен

**Тестирование создания курсов**

Запуск в файле [_test/course_page/test_course_page.py_](https://github.com/grsln/moodle_tests/blob/main/tests/course_page/test_course_page.py)

__тест-кейсы__: [на форму создания курса](https://docs.google.com/spreadsheets/d/1rftMQABAk7yvVuYu2hfgfOJXMNjlXUwZIAuwGGlStFw/edit#gid=91230819&range=A1:C1)

* проверка создания курса(+удаление курса после проверки)

### Отчеты Allure

При каждом _push_ и _pull request_ в Github c помощью **Travis CI** происходит запуск тестов и публикация отчетов на Github Pages
https://grsln.github.io/moodle_tests/
