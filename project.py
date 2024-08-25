from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

query = "gaming+laptop"
file = 0;
driver = webdriver.Chrome()

for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&{i}&crid=2EPXRD5XRP2ZS&sprefix=gaming+laptop%2Caps%2C201&ref=nb_sb_noss_1")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    # print(elems)
    # print(elems.text)

    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w+" , encoding="utf-8") as f:
            f.write(d)
            file+=1

    time.sleep(10)

driver.close()