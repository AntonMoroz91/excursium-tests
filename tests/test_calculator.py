import time
from pages.calculator_page import CalculatorPage

def test_calculator_price_changes(browser):
    browser.get("https://excursium.com/ekskursiya-dlya-shkolnikov/sin-rossii-ekskursiya-v-gzhel")
    time.sleep(3)

    calc = CalculatorPage(browser)

    old_price = calc.get_price_text()
    print(f"Цена до: {old_price}")

    calc.select_25_34()
    time.sleep(2)

    new_price = calc.get_price_text()
    print(f"Цена после: {new_price}")

    assert old_price != new_price, "Цена не изменилась после выбора группы 25-34"

    browser.save_screenshot("screenshots/TC-10_calculator.png")
