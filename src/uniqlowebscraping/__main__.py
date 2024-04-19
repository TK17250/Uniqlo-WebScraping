from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up
df = pd.DataFrame(columns=["Name", "Price", "page"]) # Create a dataframe
driver = webdriver.Chrome() # Using bowser
link_to_item = [] # List of links to items

num_items = 5 # Number of items
driver.get("https://www.uniqlo.com/th/en/men/tops/tops-collections") # Go to the website

print("\n==================== Start scraping ====================\n")
items = driver.find_elements(By.XPATH, "//article[@class='fr-grid-item w4']") # Find all items


i = 0 # Counter
# while True:
#     items = driver.find_elements(By.XPATH, "//article[@class='fr-grid-item w4']") # Find all items
#     load_more = driver.find_element(By.CSS_SELECTOR, "div.fr-load-more")
#     load_more.click()
#     print(items)

#     if not load_more:
#         break

for item in items:
    item_page = item.find_element(By.TAG_NAME, "a").get_attribute("href")
    link_to_item.append(item_page)
    i += 1
    driver.implicitly_wait(10)

    if i >= num_items:
        driver.quit()
        break

    # name = item.find_element(By.TAG_NAME, "h2").text # Find a name

    # # Find a price
    # Boxprice = item.find_elements(By.CSS_SELECTOR, "span.price-original span.fr-price-currency")
    # for textPrice in Boxprice:
    #     price = textPrice.find_element(By.TAG_NAME, "span").text

    # Go to item page
    # driver.get(f"https://uniqlo.com/{item_page}")

    # https://uniqlo.com/https://www.uniqlo.com/th/en/products/E464857-000

    # item_in_page = driver.find_element(By.TAG_NAME, "body")

    # name = item_in_page.find_element(By.CSS_SELECTOR, "span.title span.fr-no-uppercase").text # Find a name
    
    # # Find a price
    # Boxprice = item_in_page.find_elements(By.CSS_SELECTOR, "span.fr-price-currency span.xN1x05O0jJUkQaFHARtFH")
    # price = Boxprice.find_element(By.TAG_NAME, "span").text

    # data_test = item.get_attribute("data-test")
    # new_row = {"Name": name, "Price": price, "page": item_page}
    # df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # driver.back()

print(link_to_item)