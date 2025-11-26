from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def _page_(self, driver):
     self.driver = driver
     driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
     driver.implicitly_wait(20)
     driver.maximize_window()

    def field_delay(self, driver):
      input=driver.find_element(By.CSS_SELECTOR, '#delay')
      input.send_keys('45')
    
    def btns(self, driver):
      btn_7=driver.find_element(By.XPATH, '//span[text()="7"]').click()
      btn_plus=driver.find_element(By.XPATH, '//span[text()= "+"]').click()
      btn_8=driver.find_element(By.XPATH, '//span[text()= "8"]').click()
      btn_equals=driver.find_element(By.XPATH, '//span[text()= "="]').click()
      waiter=WebDriverWait(driver,50)
      waiter.until (EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))
    
    def result(self,driver):
      result=driver.find_element(By.CSS_SELECTOR, 'div.screen').text
      print(result)


