import allure
import pytest
from selenium import webdriver
from sause_page import LoginPage
from sause_page import MainPage
from sause_page import Basket
from sause_page import DeliveryInf

@pytest.fixture()
@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет корректную работу интернет-магазина")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_sause():
    driver=webdriver.Firefox()
    with allure.step("Открытие страницы кулькулятора"):
        driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(20)
    driver.maximize_window()
    with allure.step("Заполнить поля на странице"):
        LoginPage.login_page()
    with allure.step("Перейти на главную страницу"):
        MainPage.backpack()
    with allure.step("ВЫбрать нужный товар"):
        MainPage.shirt()
    with allure.step("ВЫбрать нужный товар"):
        MainPage.onesie()
    with allure.step("Переход на страницу корзины с выбранными товарами"):
        Basket.basket()
    Basket.checkout()
    with allure.step("Заполнить поле на странице"):
        DeliveryInf.first_name()
    with allure.step("Заполнить поле на странице"):
        DeliveryInf.last_name()
    with allure.step("Заполнить поле на странице"):
        DeliveryInf.postal_code()
    with allure.step("Нажать на кнопку"):
        DeliveryInf.btn_cont()
    with allure.step("Покажет итоговую стоимость товаров и информацию по доставке"):
        DeliveryInf.total_price()
    total_price=DeliveryInf.total_price()
    with allure.step("Проверит соответствие результатов"):
        assert total_price==58.29
    driver.quit()