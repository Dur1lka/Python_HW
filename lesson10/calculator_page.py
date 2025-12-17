import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Страница калькулятора")
@allure.feature("READ")
@allure.description("Заполнение полей и нажимание кнопко на странцие калькулятора")
@allure.severity("blocker")
class CalculatorPage:
    def _page_(self, driver):
     self.driver = driver
     with allure.step("Перейти на сайт калькулятора"):
       driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
     with allure.step("Подождать 20 секунд"):
       driver.implicitly_wait(20)
     with allure.step("Раскрыть окно полностью"):
         driver.maximize_window()

    def field_delay(self, driver):
      with allure.step("Найти элемент на странице"):
        input=driver.find_element(By.CSS_SELECTOR, '#delay')
      with allure.step("Ввести значение 45"):
        input.send_keys('45')
    
    def btns(self, driver):
      with allure.step("Найти элемент на странице и нажать"):
        btn_7=driver.find_element(By.XPATH, '//span[text()="7"]').click()
      with allure.step("Найти элемент на странице и нажать"):
        btn_plus=driver.find_element(By.XPATH, '//span[text()= "+"]').click()
      with allure.step("Найти элемент на странице и нажать"):
        btn_8=driver.find_element(By.XPATH, '//span[text()= "8"]').click()
      with allure.step("Найти элемент на странице и нажать"):
        btn_equals=driver.find_element(By.XPATH, '//span[text()= "="]').click()
      waiter=WebDriverWait(driver,50)
      with allure.step("Подождать пока не появится элемент"):
        waiter.until (EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))
    
    def result(self,driver):
      with allure.step("Найти элемент на странице"):
        result=driver.find_element(By.CSS_SELECTOR, 'div.screen').text
      with allure.step("Напечатай результат"):
        print(result)