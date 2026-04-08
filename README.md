# Excursium — автоматизация тестирования

## Описание проекта

Автотесты для сайта туристической компании Excursium. Проект выполнен в рамках стажировки Skillfactory.

## Технологии

- Python 3.11
- Selenium
- pytest
- Page Object Model (POM)
- Firefox + GeckoDriver

## Установка и запуск

git clone https://github.com/AntonMoroz91/excursium-tests.git
cd excursium-tests
pip install -r requirements.txt
pytest tests/ -v

## Структура проекта

- excursium-tests/
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
    - test_login.py
    - test_registration.py
    - test_filter.py
    - test_calculator.py
  - bug_reports/
    - bugs.md
  - reports/
    - report.md
  - screenshots/
    - TC-10_calculator.png
  - conftest.py
  - requirements.txt
  - test_data.py
  - .gitignore
  - README.md

## Документация

- Тест-кейсы: https://docs.google.com/spreadsheets/d/1wbXu3Wm7YJyac49O-SqbYAPl4ac8Gqhn3IbAI4_f26M/edit?usp=sharing
- Баг-репорты: bug_reports/bugs.md
- Отчёт о тестировании: reports/report.md

## Автор

Антон Мороз
Студент Skillfactory
Курс «Тестировщик-автоматизатор на Python (QAP)»
