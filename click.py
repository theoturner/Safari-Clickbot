from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import sys

if len(sys.argv) != 4:
    print("Usage: python3 click.py URL ELEMENT_ID NUM_CLICKS")
    sys.exit(1)

for i in range(0, int(sys.argv[3])):
    browser = webdriver.Safari()
    browser.get(sys.argv[1])
    try:
        myElem = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, sys.argv[2])))
        element = browser.find_element_by_id(sys.argv[2])
        element.click()
    except:
        pass
    browser.close()
