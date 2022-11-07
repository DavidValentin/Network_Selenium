from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

import json

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'client': 'ALL'}

# Login
web = 'https://es-la.facebook.com/login/?next=%2Fmarketplace%2F'
path = "/Users/dfval/Downloads/Driver/chromedriver_108.0.5359.22"

chrome_options = Options()
chrome_options.add_experimental_option('w3c', False)
driver = webdriver.Chrome(path, desired_capabilities=caps, options=chrome_options)
driver.get(web)
driver.maximize_window()

# Login Username
time.sleep(2)
username = driver.find_element_by_xpath("//input[@autocomplete='username']")
username.send_keys("fg890382@outlook.com")

# Login Password
time.sleep(3)
password = driver.find_element_by_xpath("//input[@autocomplete='current-password']")
password.send_keys("s8RDVuBjHjWpRUr")

# Login Click Button
login_button = driver.find_element_by_xpath("//button[@id='loginbutton']")
login_button.click()
time.sleep(5)

# driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps)

# Link de la categoria
yoururl = "https://www.facebook.com/marketplace/category/exercise-fitness"
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(yoururl)

# Scrolling
time.sleep(5)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
# time.sleep(5)
# html = driver.find_element_by_tag_name('html')
# html.send_keys(Keys.END)
# html = driver.find_element_by_tag_name('html')
# html.send_keys(Keys.END)
# time.sleep(5)

f = open('client.txt', 'w')

for entry in driver.get_log('client'):
    # s = entry['message']
    # json_acceptable_string = s.replace("'", "\"")
    # d = json.loads(json_acceptable_string)
    # print(d)
    f.write(str(entry))
    # print(entry)

f.close()

# Cerrar ventanas
driver.switch_to.window(driver.window_handles[1])
# driver.get(new_url)
driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.quit()
