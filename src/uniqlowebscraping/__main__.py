from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.DataFrame(columns=["Name", "Price"])
driver = webdriver.Edge() # Using bowser

driver.get("https://www.uniqlo.com/th/en/women/tops/tops-collections")

items = driver.find_elements(By.CSS_SELECTOR, ".fr-grid-item")
for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".description").text
    price = item.find_element(By.TAG_NAME, "span").text
    # image = item.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
    new_row = {"Name": name, "Price": price}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

print(df)