import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
backendData = ["tesrlkj!", "69272e04841a9be87a6d9ae6", "kalle", "testi@testi.fi","testaaja"]
MuokkaaIdt = ["Username",backendData[1],"Name","Email","Password"]
newbackendData = ["tester",backendData[1], "kalle", "testi@testi.fi","testaaja"]
labels = ["Username:", "Email:", "Nimi:", "Salasana:"]
navElememts = ['Kuvat', 'Etusivu',"Omasivu", 'KirjauduUlos', 'homeImage']
logininputs = ('email', 'password')
def textToUse(data):
    #generate login credentials
    return [f"{data[3]}",f"{data[4]}"]
def modifyinputs(data):
    # modify user data on Omat sivut page
    Muokkaa = driver.find_element(By.XPATH, "//button[normalize-space()='Muokkaa tietoja']")
    Muokkaa.click() 
    time.sleep(5)
    # check presence of input labels
    checkLabels(labels)
    # generate input elements
    inputElements = generateInputs(MuokkaaIdt)
    # modify user data
    for i in range(len(MuokkaaIdt)):
        if MuokkaaIdt[i] == backendData[1]:
            continue
        inputElements[MuokkaaIdt[i]].clear()
        inputElements[MuokkaaIdt[i]].send_keys(data[i])
    SaveNappi = driver.find_element(By.XPATH, "//button[normalize-space()='Päivitä']")
    SaveNappi.click()

    time.sleep(5)
def textstofind(data):
    # generate texts to find on Omat sivut page
    texts = [f"Tervetuloa, {data[0]}", f"ID: {data[1]}",f"Name: {data[2]}",f"Email: {data[3]}","Omat kuvat"]
    return texts
def generateInputs(collection):
    # generate input elements based on given collection of IDs
    parts = {}
    for item in collection:
       if item == backendData[1]:
           continue
       parts[item] = (By.ID, item)
    return addtoDict(parts)
def addtoDict(parts):
    elements = {}
    for part_name, locator in parts.items():
        try:
            element = driver.find_element(*locator)
            elements[part_name] = element
        except:
            print(f"Element {part_name} not found")
    return elements
def checkLabels(labels):
    # check presence of given labels on the page
    source = driver.page_source
    for label in labels:
        if label not in source:
            print(f"Label '{label}' NOT FOUND!!!!")
        else:
            print(f"Label '{label}' found")
    return labels
def checkIfElementPresent(parts):
    elements = {}
    for part_name, locator in parts.items():
        try:
            element = driver.find_element(*locator)
            elements[part_name] = element
        except:
            print(f"Element {part_name} not found")
    return elements
def countImages():
    Images = driver.find_elements(By.ID, 'AnswerCards')
    if len(Images) == 0:
        print("No images found on pictures page")
    answers = driver.find_elements(By.ID, 'answer-box')
    if len(answers) != len(Images):
        print("something wrong with answers or images, their counts do not match")
    return len(Images)
url = 'http://localhost:3000/'
driver = webdriver.Chrome()
driver.get(url)
webdriver_wait = WebDriverWait(driver, 10)


#find navigation to login page
kirjaudu = webdriver_wait.until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Kirjaudu'))
)
kirjaudu.click()
time.sleep(2)


# login to the account
button = driver.find_element(By.ID, 'loginBtn')
inputElements = generateInputs(logininputs)
# generate user login credentials
loginCredentials = textToUse(backendData)
inputElements[logininputs[0]].send_keys(loginCredentials[0])
inputElements[logininputs[1]].send_keys(loginCredentials[1])
button.click()
time.sleep(1)
driver.refresh()
time.sleep(2)
#navigate to Omat sivut this verifies login success
etusivu = driver.find_element(By.PARTIAL_LINK_TEXT, 'Etusivu')
etusivu.click()
omatSivutlink = driver.find_element(By.ID, 'Omasivu')
omatSivutlink.click()
print("Testing Omat sivut page, verigying navigation bar elements:")
# verify elements on Omat sivut page
webdriver_wait.until(    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Kirjaudu ulos')))
NavElements = generateInputs(navElememts)
if len(NavElements) != 5: print("Not all navigation bar elements found after login")
else: print("All navigation bar elements found after login")
print("Verifying texts on Omat sivut page:")
# verify user data on Omat sivut page
checkLabels(textstofind(backendData))
print("Modifying user data on Omat sivut page:")
# check modify user elements and modify data
modifyinputs(newbackendData)
time.sleep(1)
print("Verifying modified texts on Omat sivut page:")
# verify changes
source = driver.page_source
checkLabels(textstofind(newbackendData))
print("Reverting changes to original data:")
# revert changes to original data   
modifyinputs(backendData)
time.sleep(5)
print("testing picture upload functionality:")
count = countImages()
print(f"Current picture count: {count}")
etusivu.click()
time.sleep(1)
print("uploading a picture")
#test if picture count goes up when uploading a new picture
upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "testimage.png"))
uploadfile = driver.find_element(By.ID, 'file-input')
uploadfile.send_keys(upload_file)
sendfile = driver.find_element(By.ID, 'homeButton')
sendfile.click()
time.sleep(5)
omasivu = driver.find_element(By.ID, 'Omasivu')
omasivu.click()
time.sleep(5)
newcount = countImages()
print(f"New picture count: {newcount}")
if newcount != count + 1:
    print("Picture upload failed, picture count did not increase") 
else:
    print("Picture upload worked, picture count increased")
driver.close()
