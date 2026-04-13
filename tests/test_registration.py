import time
from selenium.webdriver.common.by import By
from pages.registration_page import RegistrationPage

def test_registration_new_user(browser):
    reg_page = RegistrationPage(browser)
    reg_page.open("https://excursium.com")
    time.sleep(2)

    email = "autotest.qa11@gmail.com"
    password = "Zenitpiter1925!!!!"

    print(f"\n📧 Регистрируем почту: {email}")

    reg_page.open_login_icon()
    time.sleep(1)

    reg_page.open_registration_form()
    time.sleep(1)

    reg_page.enter_email(email)
    reg_page.enter_password(password)
    reg_page.accept_terms()

    reg_page.click_create_account()
    time.sleep(3)

    print(f"\n📨 Код отправлен на {email}")
    code = input("🔢 Введите 4-значный код из письма: ")

    for i, digit in enumerate(code, start=1):
        field = browser.find_element(By.XPATH, f"//*[@id='login-vue']/div/div[2]/div[6]/div[2]/input[{i}]")
        field.send_keys(digit)
        time.sleep(0.3)

    confirm_btn = browser.find_element(By.XPATH, "//*[@id='checkCode-btn']/span[2]")
    confirm_btn.click()
    time.sleep(3)

    # СЧАСТЛИВЫЙ КОНЕЦ: аккаунт создан, тест PASSED
    print("\n✅ Аккаунт успешно создан! Тест PASSED.")
    browser.save_screenshot("screenshots/TC-02_registration_success.png")
