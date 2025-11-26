import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture()
def test_calculator():
    driver=webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(20)
    driver.maximize_window()
    CalculatorPage.field_delay()
    CalculatorPage.btns()
    CalculatorPage.result()
    result=CalculatorPage.result()
    assert result=="15"
    CalculatorPage.driver.quit()
