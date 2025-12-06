from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

url = 'http://localhost:3000/pictures'

def countImages():
    Images = driver.find_elements(By.ID, 'AnswerCards')
    if len(Images) == 0:
        print("No images found on pictures page")
    answers = driver.find_elements(By.CLASS_NAME, 'answer-box')
    if len(answers) != len(Images):
        print("something wrong with answers or images, their counts do not match")
    return len(Images)

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)


webdriver_wait = WebDriverWait(driver, 10)
# test finding navigation links
navElements = testNavibarElements()

webdriver_wait.until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Etusivu'))
)
Etusivulink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Etusivu')
time.sleep(5)
countImages()
  