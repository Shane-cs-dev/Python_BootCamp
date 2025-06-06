from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Configure Chrome setting
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

def check_for_upgrade():
    try:
        money = driver.find_element(By.ID, "money")
        available_cookie = int(money.text.replace(",", "")) #Current available cookie and remove commas
        upgrade_item = driver.find_elements(By.CSS_SELECTOR, "#store b")

        for items in reversed(upgrade_item):
            item_text = items.text
            if "-" in item_text:
                upgrade_price = int(item_text.split("-")[1].replace(",", ""))
                print(upgrade_price)
                if available_cookie >= upgrade_price:
                    items.click()
            else:
                print("There's item without '-'")
    except Exception as e:
        print(e)

while True:
    money = driver.find_element(By.ID, "money")
    available_cookie = int(money.text.replace(",", ""))  # Current available cookie and remove commas
    if available_cookie < 300:
        for n in range(150):
            cookie = driver.find_element(By.ID, "cookie")
            cookie.click()
    elif available_cookie > 300:
        for n in range(500):
            cookie = driver.find_element(By.ID, "cookie")
            cookie.click()
    elif available_cookie > 1000:
        for n in range(1000):
            cookie = driver.find_element(By.ID, "cookie")
            cookie.click()
    time.sleep(5)
    check_for_upgrade()

# driver.quit()