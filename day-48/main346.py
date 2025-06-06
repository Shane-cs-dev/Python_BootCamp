from selenium.webdriver.common.by import By
from selenium import webdriver


#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless=new")  # Run Chrome in headless mode
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://24h.pchome.com.tw/prod/DMBA0K-A900HLNJP")

price_xpath = driver.find_element(By.XPATH, "//*[@id='ProdBriefing']/div/div/div/div[2]/div[6]/div/div/div/div/div[1]").text
print(price_xpath.split("$")[1])

# driver.close()#Close the active tab
driver.quit()#Quit the browser
