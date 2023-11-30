from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input_locator = (By.CLASS_NAME, "gLFyf")

    def open(self):
        self.driver.get("https://google.com")
        self.driver.maximize_window()

    def search_for(self, query):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_input_locator)
        )
        input_element.clear()
        input_element.send_keys(query + Keys.ENTER)

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.link_locator = (By.PARTIAL_LINK_TEXT, "Darth Vader")

    def click_result_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.link_locator)
        )
        link.click()

class DarthVaderPage:
    def __init__(self, driver):
        self.driver = driver

    def is_on_page(self):
        return EC.title_contains("Darth Vader")(self.driver)

# Test script using POM
service = webdriver.chrome.service.Service(executable_path="drivers/chromedriver")
driver = webdriver.Chrome(service=service)

# Create instances of page classes
google_page = GoogleHomePage(driver)
search_results_page = SearchResultsPage(driver)
darth_vader_page = DarthVaderPage(driver)

# Test steps
google_page.open()
google_page.search_for("Darth Vader")

search_results_page.click_result_link()

# Validate that we are on the correct page
if darth_vader_page.is_on_page():
    print("Successfully navigated to the correct page.")
else:
    print("Unexpected page.")

# Close the browser window and quit the WebDriver
driver.quit()
