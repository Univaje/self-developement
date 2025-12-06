from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.google.com'

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)

button_element = driver.find_element(By.ID, 'W0wltc')
button_element.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
)

time.sleep(5)  # Wait for the search box to appear
input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.clear() # Clear any pre-filled text
input_element.send_keys('Selenium WebDriver' + Keys.ENTER)

webdriver_wait = WebDriverWait(driver, 10)
webdriver_wait.until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Selenium WebDriver'))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Selenium WebDriver') # Find link by partial text
"""links = driver.find_elements(By.TAG_NAME, 'a') # Find all links on the page"""
link.click()

time.sleep(10)  # Wait for the page to load

driver.quit()