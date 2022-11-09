from seleniumwire import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://devtools.glitch.me/network/getstarted.html')
driver.maximize_window()

time.sleep(3)

for request in driver.requests:
    if 'getstarted.json' in request.url:
        print(
            request.url,
            request.response.status_code,
            request.response.headers
        )