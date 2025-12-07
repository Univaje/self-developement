import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def countImages():
    Images = driver.find_elements(By.ID, 'AnswerCards')
    if len(Images) == 0:
        print("No images found on pictures page")
    answers = driver.find_elements(By.CLASS_NAME, 'answer-box')
    if len(answers) != len(Images):
        print("something wrong with answers or images, their counts do not match")
    return len(Images)

url = 'http://localhost:3000/'
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

driver = webdriver.Chrome()

driver.get(url)

webdriver_wait = WebDriverWait(driver, 10)

webdriver_wait.until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Kirjaudu'))
)
# test finding navigation links
NavElements = testNavibarElements()
# test finding main page elements
parts = { 
                'UpoladNappi': (By.ID, 'homeButton'),
                'ValitseKuvaNappi': (By.ID, 'file-input')
            }

pageElements = addtoDict(parts)

if len(NavElements) != 5:
    print("Not all navigation bar elements found")
elif len(pageElements) != 2:
    print("Not all main page elements found")

#Test navigation links
NavElements['Kuvat'].click()
time.sleep(1)
baselineUrl = driver.current_url
NavElements['Homekuva'].click()
time.sleep(1)
currentUrl = driver.current_url
if currentUrl == baselineUrl:
    print(f"Home image link failed. Expected URL: {baselineUrl}, but got: {currentUrl}")
for key, element in NavElements.items():
    element.click()
    time.sleep(1)
    if key == 'Etusivu':
        expected_url = url
    elif key == 'Kuvat':
        expected_url = url + 'pictures'
    elif key == 'Kirjaudu':
        expected_url = url + 'login'
    elif key == 'Rekisteröidy':
        expected_url = url + 'register'
    elif key == 'Homekuva':
        
        expected_url = url
    else:
        expected_url = ''
    current_url = driver.current_url
    if current_url != expected_url:
        print(f"Navigation to {key} failed. Expected URL: {expected_url}, but got: {current_url}")

# test upload image
time.sleep(2)
upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "testimage.png"))
uploadfile = driver.find_element(By.ID, 'file-input')
uploadfile.send_keys(upload_file)
sendfile = driver.find_element(By.ID, 'homeButton')
sendfile.click()
time.sleep(2)  # wait for upload to process
kirjaudu = driver.find_element(By.ID,'loginBtn')
if kirjaudu is not None:
    print("Works correctly, upload requires login when not logged in")







time.sleep(10)  # Wait for the page to load

driver.quit()