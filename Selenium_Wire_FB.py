from seleniumwire import webdriver
# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web = 'https://es-la.facebook.com/login/?next=%2Fmarketplace%2F'
path = "/Users/dfval/Downloads/chromedriver"

driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

# Login Username
time.sleep(2)
username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
username.send_keys("fg890382@outlook.com")

# Login Password
time.sleep(3)
password = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
password.send_keys("s8RDVuBjHjWpRUr")

# Login Click Button
login_button = driver.find_element(By.XPATH, "//button[@id='loginbutton']")
login_button.click()
time.sleep(5)

# Link de la categoria
yoururl = "https://www.facebook.com/marketplace/category/exercise-fitness"
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(yoururl)

# Scrolling
time.sleep(5)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(5)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(5)

for request in driver.requests:
    if 'graphql/' in request.url and len(request.body) > 6000:
        print(
            # request.url,
            request.body,
            request.headers
        )