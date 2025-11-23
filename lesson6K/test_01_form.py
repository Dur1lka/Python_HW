import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.EdgeOptions()
driver = webdriver.Edge()
driver.maximize_window()

@pytest.fixture
def test_01_form():
 driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.implicitly_wait(4)

first_name = driver.find_element(By.NAME, "[name='first-name']")
first_name.send_keys("Иван")
first_name.click()

last_name = driver.find_element(By.NAME, "[name='last-name']")
last_name.send_keys("Петров")
last_name.click()

address_input = driver.find_element(By.NAME, "[name='address']")
address_input.send_keys("Ленина, 55-3")
address_input.click()

email_address = driver.find_element (By.NAME, "[name='e-mail']")
email_address.send_keys("test@skypro.com")
email_address.click()

phone_number = driver.find_element(By.NAME, "[name='phone']")
phone_number.send_keys("+7985899998787")
phone_number.click()

city_name = driver.find_element(By.NAME, "[name='city']")
city_name.send_keys("Москва")
city_name.click()

country_name = driver.find_element(By.NAME, "[name='country']")
country_name.send_keys("Россия")
country_name.click()

job_position = driver.find_element(By.NAME, "[name='job-position']")
job_position.send_keys("QA")
job_position.click()

company_name = driver.find_element(By.NAME, "[name='company']")
company_name.send_keys("SkyPro")
company_name.click()

submit_button = driver.find_element(By.NAME, ".btn.btn-outline-primary")
submit_button.click()
zip_code = driver.find_element(By.NAME, "[name='zip-code']").value_of_css_property("background-color")

assert zip_code == "#f8d7da"
fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job", "company"]

for field in fields:
        taps = driver.find_element(By.NAME, "form-label").value_of_css_property("background-color")
assert taps == "#d1e7dd"

driver.quit()

