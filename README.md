# moodle_tests

[![Build Status](https://app.travis-ci.com/grsln/moodle_tests.svg?branch=main)](https://app.travis-ci.com/grsln/moodle_tests)

**Цель**: протестировать функционал модуля сайта https://qacoursemoodle.innopolis.university

Проект **moodle_tests** содержит проверки авторизации, изменения профиля пользователя и создания курсов.

### Начало работы

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

_test_auth.py_

* проверка авторизации с валидными данными
* проверка авторизации с невалидными данными
  * пустой логин
  * пустой пароль
* проверка авторизации с неверным паролем

**Тестирование редактирования профиля пользователя**

_test_user_page.py_

* проверка изменения обязательных полей
* проверка заполнения обязательных полей пустой строкой
* проверка длинных имен

**Тестирование создания курсов**

_test_course_page.py_

* проверка создания курса
