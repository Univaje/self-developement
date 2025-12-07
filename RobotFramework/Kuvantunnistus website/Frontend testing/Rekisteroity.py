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

url = 'http://localhost:3000/register'

driver = webdriver.Chrome()

driver.get(url)

webdriver_wait = WebDriverWait(driver, 10)
# test finding navigation links
navElements = testNavibarElements()

webdriver_wait.until(
    EC.presence_of_element_located((By.ID, 'registerBtn'))
)
parts = { 
                'Otsikko': (By.TAG_NAME, 'h2'),
                'Käyttäjänimi': (By.XPATH, "//label[@for='usernameInput']"),
                'Sähköposti': (By.XPATH, "//label[@for='emailInput']"),
                'Nimi': (By.XPATH, "//label[@for='nameInput']"),
                'Salasana': (By.XPATH, "//label[@for='passwordInput']")                
            }
pageTexts =addtoDict(parts)

imputparts = {
                'KäyttäjänimiInput': (By.ID, 'usernameInput'),
                'SähköpostiInput': (By.ID, 'emailInput'),
                'NimiInput': (By.ID, 'nameInput'),
                'SalasanaInput': (By.ID, 'passwordInput'),
                'registerBtn': (By.ID, 'registerBtn')
            }
inputElements = addtoDict(imputparts)
for key, element in inputElements.items():
    number = random.randint(1,1000)
    if key == 'SähköpostiInput':
        element.send_keys('tester'+ str(number) + '@gmail.com', Keys.ENTER)
    else:
        element.send_keys('tester n. ' + str(number), Keys.ENTER)
#test fuctoinality of registration button
time.sleep(5)
urlAfter = driver.current_url
if urlAfter == url:
    print("Registration seems to have failed, still on the same page")
    

time.sleep(10)  # Wait for the page to load

driver.quit()