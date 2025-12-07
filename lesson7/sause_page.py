from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import FirefoxDriveManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()

class LoginPage:
    def login_page(self,driver):
        user_name=driver.find_element(By.CSS_SELECTOR, '#user-name')
        user_name=driver.send_keys('standard_user')

        password=driver.find_element(By.CSS_SELECTOR, '#password')
        password=driver.send_keys('secret_sauce')
        driver.implicitly_wait(4)

        login=driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        driver.implicitly_wait(4)

class MainPage:
    def backpack(self,driver):
        backpack=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
        backpack= driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        backpack.click()
    def shirt(self,driver):
        shirt=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
        shirt=driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt")
        shirt.click()
    def onesie(self,driver):
        onesie=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie")))
        onesie=driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie")
        onesie.click()

class Basket:
    def basket(self,driver):
        basket=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')))
        basket=driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
        basket.click()
    def checkout(self,driver):
        checkout=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        checkout=driver.find_element(By.CSS_SELECTOR, "#checkout")
        checkout.click()

class DeliveryInf:
    def first_name(self,driver):
        first_name=driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name=driver.send_keys("Евгений")
    def last_name(self,driver):
        last_name=driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name=driver.send_keys("Саханевич")
    def postal_code(self,driver):
        postal_code=driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code=driver.send_keys("456020")
    def btn_cont(self,driver):
        btn_cont=driver.find_element(By.CSS_SELECTOR, "#continue")
        btn_cont=driver.click()
    def total_price(self,driver):
        total_price=driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text
        total_price_value=float(total_price.split("$")[1])
        print(total_price)
