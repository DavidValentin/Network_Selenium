import json
from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

# make chrome log requests
capabilities = DesiredCapabilities.CHROME
capabilities["loggingPrefs"] = {"performance": "ALL"}  # newer: goog:loggingPrefs
driver = webdriver.Chrome(
    desired_capabilities=capabilities, executable_path="/Users/dfval/Downloads/chromedriver"
)

# fetch a site that does xhr requests
driver.get("https://www.geeksforgeeks.org/")
sleep(5)  # wait for the requests to take place

# extract requests from logs
logs_raw = driver.get_log("browser")
logs = [json.loads(lr["message"])["message"] for lr in logs_raw]


def log_filter(log_):
    return (
        # is an actual response
        log_["method"] == "Network.responseReceived"
        # and json
        and "json" in log_["params"]["response"]["mimeType"]
    )


for log in filter(log_filter, logs):
    request_id = log["params"]["requestId"]
    resp_url = log["params"]["response"]["url"]
    print(f"Caught {resp_url}")
    print(driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id}))