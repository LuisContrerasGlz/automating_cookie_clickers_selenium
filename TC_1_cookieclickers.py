from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver with the specified executable path
service = Service(executable_path="drivers/chromedriver")
driver = webdriver.Chrome(service=service)

# Open page and maximize the browser window
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
driver.implicitly_wait(10)

lang_selector = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
lang_selector.click

driver.implicitly_wait(10)
