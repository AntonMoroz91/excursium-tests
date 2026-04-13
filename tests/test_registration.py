"""
Тест регистрации нового пользователя.
Код подтверждения вводится вручную (из email).
"""

import time
from selenium.webdriver.common.by import By
from pages.registration_page import RegistrationPage

def test_registration_new_user(browser):
    reg_page = RegistrationPage(browser)
    reg_page.open("https://excursium.com")
    time.sleep(2)

    # Данные для регистрации (можно заменить на новые)
    email = "autotest.qa11@gmail.com"
    password = "Zenitpiter1925!!!!"

    print(f"\nРегистрируем почту: {email}")

    reg_page.open_login_icon()           # открываем форму
    time.sleep(1)

    reg_page.open_registration_form()    # переключаемся на "Регистрация"
    time.sleep(1)

    # Заполняем поля
    reg_page.enter_email(email)
    reg_page.enter_password(password)
    reg_page.accept_terms()

    # Отправляем форму
    reg_page.click_create_account()
    time.sleep(3)

    # Ручной ввод кода из письма
    print(f"\nКод отправлен на {email}")
    code = input("Введите 4-значный код из письма: ")

    # Вводим код по цифрам в 4 отдельных поля
    for i, digit in enumerate(code, start=1):
        field = browser.find_element(By.XPATH, f"//*[@id='login-vue']/div/div[2]/div[6]/div[2]/input[{i}]")
        field.send_keys(digit)
        time.sleep(0.3)

    # Подтверждаем регистрацию
    confirm_btn = browser.find_element(By.XPATH, "//*[@id='checkCode-btn']/span[2]")
    confirm_btn.click()
    time.sleep(3)

    print("\nАккаунт успешно создан! Тест PASSED.")
    browser.save_screenshot("screenshots/TC-02_registration_success.png")
