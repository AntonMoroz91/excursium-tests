# Excursium — автоматизация тестирования

## Описание проекта
Автотесты для сайта туристической компании Excursium. Проект выполнен в рамках стажировки Skillfactory.

## Технологии
- Python 3.11
- Selenium
- pytest
- Faker
- Page Object Model (POM)
- Firefox + GeckoDriver

## Установка и запуск
    git clone <ссылка_на_твой_репозиторий>
    cd excursium_project
    pip install -r requirements.txt
    pytest -v

## Структура проекта

excursium_project/
  - pages/
    - __init__.py
    - base_page.py
    - main_page.py
    - login_page.py
    - registration_page.py
    - filter_page.py
    - calculator_page.py
  - tests/
    - __init__.py
    - test_demo.py
    - test_login.py
    - test_registration.py
    - test_filter.py
    - test_calculator.py
  - bug_reports/
    - bugs.md
  - reports/
    - report.md
  - screenshots/
  - conftest.py
  - requirements.txt
  - test_data.py
  - .gitignore
  - README.md

## Документация
    Тест-кейсы (Google Sheets) : https://docs.google.com/spreadsheets/d/1wbXu3Wm7YJyac49O-SqbYAPl4ac8Gqhn3IbAI4_f26M/edit?usp=sharing
    Баг-репорты               : bug_reports/bugs.md
    Отчёт о тестировании      : reports/report.md

## Автор
    Антон Мороз
    Студент Skillfactory
    Курс «Тестировщик-автоматизатор на Python (QAP)»