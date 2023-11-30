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

# Open Google's homepage and maximize the browser window
driver.get("https://google.com")
driver.maximize_window()

# Wait for up to 10 seconds for the search input element to be present
input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# Clear any existing text in the input field and type the search query and press Enter
input_element.clear()
input_element.send_keys("Darth Vader" + Keys.ENTER)

# Wait for up to 10 seconds for a search result link containing "Darth Vader" to be present
link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Darth Vader"))
)

link.click()

driver.quit()
