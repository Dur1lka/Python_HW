import pytest
from selenium import webdriver
from sause_page import LoginPage
from sause_page import MainPage
from sause_page import Basket
from sause_page import DeliveryInf

@pytest.fixture()
def test_sause():
    driver=webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(20)
    driver.maximize_window()
    LoginPage.login_page()
    MainPage.backpack()
    MainPage.shirt()
    MainPage.onesie()
    Basket.basket()
    Basket.checkout()
    DeliveryInf.first_name()
    DeliveryInf.last_name()
    DeliveryInf.postal_code()
    DeliveryInf.btn_cont()
    DeliveryInf.total_price()
    total_price=DeliveryInf.total_price()
    assert total_price==58.29
    driver.quit()