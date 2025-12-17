import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()

@allure.title("Страница интернет-магазина")
@allure.feature("READ")
@allure.description("Заполнение полей и нажимание кнопко на странцие интернет-магазина")
@allure.severity("blocker")
class LoginPage:
    def login_page(self,driver):
        with allure.step("Найти элемент на странице"):
            user_name=driver.find_element(By.CSS_SELECTOR, '#user-name')
        with allure.step("Отправить значение логина"):
            user_name=driver.send_keys('standard_user')
        with allure.step("Найти элемент на странице"):
            password=driver.find_element(By.CSS_SELECTOR, '#password')
        with allure.step("Отправить значение пароля"):
            password=driver.send_keys('secret_sauce')
        driver.implicitly_wait(4)
        with allure.step("Найти элемент на странице и нажать на него"):
            login=driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        driver.implicitly_wait(4)

class MainPage:
    def backpack(self,driver):
        with allure.step("Подождать пока кнопка не станет кликабельным"):
            backpack=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
        with allure.step("Найти элемент на странице"):
            backpack= driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        with allure.step("Нажать на кнопку"):
            backpack.click()
    def shirt(self,driver):
        with allure.step("Подождать пока кнопка не станет кликабельным"):
            shirt=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
        with allure.step("Найти элемент на странице"):
            shirt=driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt")
        with allure.step("Нажать на кнопку"):
            shirt.click()
    def onesie(self,driver):
        with allure.step("Подождать пока кнопка не станет кликабельным"):
            onesie=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie")))
        with allure.step("Найти элемент на странице"):
            onesie=driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie")
        with allure.step("Нажать на кнопку"):
            onesie.click()

class Basket:
    def basket(self,driver):
        with allure.step("Подождать пока кнопка не станет кликабельным"):
            basket=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')))
        with allure.step("Найти элемент на странице"):
            basket=driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
        with allure.step("Нажать на кнопку"):
            basket.click()
    def checkout(self,driver):
        with allure.step("Подождать пока кнопка не станет кликабельным"):
            checkout=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        with allure.step("Найти элемент на странице"):
            checkout=driver.find_element(By.CSS_SELECTOR, "#checkout")
        with allure.step("Нажать на кнопку"):
            checkout.click()

class DeliveryInf:
    def first_name(self,driver):
         with allure.step("Найти элемент на странице"):
             first_name=driver.find_element(By.CSS_SELECTOR, "#first-name")
         with allure.step("Отправить значение поля"):    
             first_name=driver.send_keys("Евгений")
    def last_name(self,driver):
        with allure.step("Найти элемент на странице"):
            last_name=driver.find_element(By.CSS_SELECTOR, "#last-name")
        with allure.step("Отправить значение поля"):  
            last_name=driver.send_keys("Саханевич")
    def postal_code(self,driver):
        with allure.step("Найти элемент на странице"):
            postal_code=driver.find_element(By.CSS_SELECTOR, "#postal-code")
        with allure.step("Отправить значение поля"):  
            postal_code=driver.send_keys("456020")
    def btn_cont(self,driver):
        with allure.step("Найти элемент на странице"):
            btn_cont=driver.find_element(By.CSS_SELECTOR, "#continue")
        with allure.step("Нажать на кнопку"):
            btn_cont=driver.click()
    def total_price(self,driver):
        with allure.step("Найти элемент на странице"):
            total_price=driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
        total_price_value=float(total_price.split("$")[1])
        with allure.step("Напечатает результат"):
            print(total_price)