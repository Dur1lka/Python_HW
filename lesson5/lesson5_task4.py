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

driver.get("http://the-internet.herokuapp.com/login")

username=driver.find_element(By.CSS_SELECTOR, "input#username")
username.send_keys("tomsmith")
sleep(3)

password=driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")
sleep(3)

button=driver.find_element(By.CSS_SELECTOR, "button.radius").click()
flash = driver.find_element(By.CSS_SELECTOR, "div#flash")
print(flash.text)
sleep(5)

driver.quit()