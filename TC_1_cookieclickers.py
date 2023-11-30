from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the "English" language element to be clickable
try:
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'English')]"))
    ).click()
except Exception as e:
    print(f"Error clicking on language: {e}")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Wait for the big cookie to be present
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, cookie_id))
    )
except Exception as e:
    print(f"Error waiting for big cookie: {e}")

while True:
    try:
        cookie = driver.find_element(By.ID, cookie_id)
        cookie.click()
        
        # Get the current number of cookies
        cookies_count = int(driver.find_element(By.ID, cookies_id).text.split(" ")[0].replace(",", ""))
        
        for i in range(4):
            product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

            if not product_price.isdigit():
                continue

            product_price = int(product_price)

            if cookies_count >= product_price:
                product = driver.find_element(By.ID, product_prefix + str(i))
                product.click()
                break
    except Exception as e:
        print(f"Error during interaction: {e}")
