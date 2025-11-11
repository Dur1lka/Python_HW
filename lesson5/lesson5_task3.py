from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

field=driver.find_element(By.CSS_SELECTOR, "input[type='number']")
field.send_keys("Sky")
sleep(5)

field.clear()
sleep(5)

field.send_keys("Pro")
sleep(5)

driver.quit()