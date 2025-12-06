from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def checkbox_uncheck_all(driver):
    checkboxes = driver.find_elements(By.CSS_SELECTOR,"[aria-pressed='true']")
    for checkbox in checkboxes:
        value = checkbox.get_attribute("data-id")
        slider = checkbox.find_element(By.XPATH, "following-sibling::span[contains(@class,'fc-slider-el')]")
        if not slider.is_displayed():
            continue  # skip hidden
        if checkbox.is_selected():
            slider.click()

url = 'https://orteil.dashnet.org/cookieclicker/'

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)

webdriver_wait = WebDriverWait(driver, 10)

managebutton = driver.find_element(By.CSS_SELECTOR,"[aria-label='Manage options']")
managebutton.click()
checkbox_uncheck_all(driver)

vendorbutton = driver.find_element(By.CSS_SELECTOR,"[aria-label='Vendor preferences']")
vendorbutton.click()
checkbox_uncheck_all(driver)

confirmbutton = driver.find_element(By.CSS_SELECTOR,"[aria-label='Confirm choices']")
driver.execute_script("arguments[0].click();", confirmbutton)

language = driver.find_element(By.ID, 'langSelect-EN')
language.click()



time.sleep(10)  # Wait for the page to load
driver.quit()


