from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import time

# Pasamos el link a analizar
yoururl = "https://devtools.glitch.me/network/getstarted.html"

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps)

driver.get(yoururl)
time.sleep(10) # wait for all the data to arrive.

for entry in driver.get_log('performance'):
    print(entry)
