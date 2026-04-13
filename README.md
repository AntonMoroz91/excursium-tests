Excursium — автоматизация тестирования
=======================================

О проекте
---------
Автотесты для сайта туристической компании Excursium.
Проект выполнен в рамках стажировки Skillfactory (курс «Тестировщик-автоматизатор на Python»).

Основная цель — проверить работоспособность ключевых функций фронт-сайта:
- лендинг,
- регистрация и авторизация,
- фильтрация экскурсий,
- онлайн-калькулятор цены.

Технологии
----------
- Python 3.11
- Selenium
- pytest
- Page Object Model (POM)
- Google Chrome + ChromeDriver
- Faker (для генерации тестовых данных при необходимости)

Установка и запуск
------------------
- git clone https://github.com/AntonMoroz91/excursium-tests.git
- cd excursium-tests
- pip install -r requirements.txt
- pytest tests/ -v

Важно
-----
Перед запуском test_login.py создайте в корне файл `registered_user.json`:

```json
{
  "email": "ваш_email@example.com",
  "password": "ваш_пароль"
}
```

Структура проекта
-----------------
- excursium-tests/
  - pages/
    - `__init__.py`
    - base_page.py
    - login_page.py
    - registration_page.py
    - filter_page.py
    - calculator_page.py
  - tests/
    - `__init__.py`
    - test_login.py
    - test_registration.py
    - test_filter.py
    - test_calculator.py
  - bug_reports/
    - bugs.md
  - reports/
    - report.md
  - screenshots/
    - TC-04_login_success.png
    - TC-06_filter_moscow.png
    - TC-10_calculator.png
  - conftest.py
  - requirements.txt
  - test_data.py
  - .gitignore
  - README.md

Автотесты
---------
- test_registration.py → Регистрация (код вводится вручную) → ✅ PASSED
- test_login.py → Авторизация пользователя → ✅ PASSED
- test_filter.py → Фильтрация экскурсий → ✅ PASSED
- test_calculator.py → Калькулятор (группа 25-34) → ✅ PASSED

Документация
------------
- Тест-кейсы (15 шт.) → https://docs.google.com/spreadsheets/d/1wbXu3Wm7YJyac49O-SqbYAPl4ac8Gqhn3IbAI4_f26M/edit?usp=sharing
- Баг-репорты (2 шт.) → bug_reports/bugs.md
- Отчёт о тестировании → reports/report.md

Автор
-----
   ✦   Антон Мороз
   ✦   Студент Skillfactory
   ✦   Курс «Тестировщик-автоматизатор на Python (QAP)»
   ✦   GitHub: https://github.com/AntonMoroz91
