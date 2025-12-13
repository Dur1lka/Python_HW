from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

button=driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

sleep(5)