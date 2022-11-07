from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = 'https://getbootstrap.com/'
path = "/Users/dfval/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

time.sleep(3)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)