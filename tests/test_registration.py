import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from faker import Faker

fake = Faker()


def test_registration(browser):
    main_page = MainPage(browser)
    main_page.open("https://excursium.com")
    main_page.click(main_page.USER_ICON)
    time.sleep(2)

    # Клик по вкладке "Регистрация" внутри контейнера
    reg_tab = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[3]//button[contains(text(),'Регистрация')]"))
    )
    browser.execute_script("arguments[0].click();", reg_tab)
    time.sleep(2)

    reg_page = RegistrationPage(browser)
    email = fake.email()
    password = "Qwerty123"
    reg_page.register(email, password)
    time.sleep(3)

    assert "excursium" in browser.current_url