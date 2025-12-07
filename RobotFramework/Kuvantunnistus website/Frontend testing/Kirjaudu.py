from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
def addtoDict(parts):
    elements = {}
    for part_name, locator in parts.items():
        try:
            element = driver.find_element(*locator)
            elements[part_name] = element
        except:
            print(f"Element {part_name} not found")
    return elements

def testNavibarElements():
    parts =  { 
                'Kirjaudu': (By.PARTIAL_LINK_TEXT, 'Kirjaudu'),
                'Kuvat': (By.PARTIAL_LINK_TEXT, 'Kuvat'),
                'Etusivu': (By.PARTIAL_LINK_TEXT, 'Etusivu'),
                'Rekisteröidy': (By.PARTIAL_LINK_TEXT, 'Rekisteröidy'),
                'Homekuva': (By.ID, 'homeImage'),
    }
    return addtoDict(parts)

url = 'http://localhost:3000/login'


driver = webdriver.Chrome()

driver.get(url)

webdriver_wait = WebDriverWait(driver, 10)
# test finding navigation links
navElements = testNavibarElements()

textstofind = ["Sähköposti:", "Salasana:","Ei käyttäjää vielä?","Rekisteröidy"]
textToUse =["testi@testi.fi","testaaja"]
source = driver.page_source

for text in textstofind:
    if text not in source:
        print(f"Text '{text}' not found on the page")
    else:
        print(f"Text '{text}' found on the page")

collection = {
                'SähköpostiInput': (By.XPATH, "//input[@type='email']"),
                'SalasanaInput': (By.XPATH, "//input[@type='password']"),
            }
inputElements = addtoDict(collection)
for key, element in inputElements.items():
    print(f"Element '{key}' found: {element is not None}")

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Rekisteröidy')
if link is None:
    print("Rekisteröidy link not found")
button = driver.find_element(By.ID, 'loginBtn')
if button is None:
    print("Login button not found")

inputElements['SähköpostiInput'].send_keys(textToUse[0])
inputElements['SalasanaInput'].send_keys(textToUse[1])
button.click()
time.sleep(5)
# After login, check if navigation bar elements are still present
driver.refresh()
logoutLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Kirjaudu ulos')
if logoutLink is None:
    print("Logout link not found after login")




