import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture()
@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректную работу калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    driver=webdriver.Chrome()
    with allure.step("Открытие страницы кулькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(20)
    driver.maximize_window()
    with allure.step("Заполнить поле на странице"):
        CalculatorPage.field_delay()
    with allure.step("Нажать на соотвествующие кнопки на странице"):
        CalculatorPage.btns()
    with allure.step("Покажет результат"):
        CalculatorPage.result()
    result=CalculatorPage.result()
    with allure.step("Проверит соответствие результатов"):
        assert result=="15"
    CalculatorPage.driver.quit()