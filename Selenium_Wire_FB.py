from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import json

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
time.sleep(10)

# Link de la categoria
# TODO 1 Keyla Mapear todas las URLs [arreglo con todas las URL a scrapear]
# TODO 1 Probar con API FETCH en Python
yoururl = "https://www.facebook.com/marketplace/category/exercise-fitness"
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(yoururl)

# TODO 2 Scroll Infinito
# Scrolling 1
time.sleep(5)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(5)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(5)

# Scrolling Infinito
last_height = driver.execute_script("return document.body.scrollHeight")
j = 1
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        last_height = new_height
        j = j + 1

    if j > 50:
        break


data_list = []
# TODO 3 Persistir esta data dividirlo por request (body, x-fb-lsd, referer, cookie)
for request in driver.requests:
    if 'graphql/' in request.url and len(request.body) > 3000:
        body = re.findall("b'([^']*)'", str(request.body))
        cookie = re.findall('cookie: ([^\n]*)', str(request.headers))
        xfblsd = re.findall('x-fb-lsd: ([^\n]*)', str(request.headers))
        referer = re.findall('referer: ([^\n]*)', str(request.headers))

        data = {'body': body, 'cookie': cookie, 'xfblsd': xfblsd, 'referer': referer}
        data_list.append(data)

print(data_list)

with open('data.json', 'w') as fp:
    json.dump(data_list, fp)

with open('data.json', 'r') as fp:
    data_list = json.load(fp)

