from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/KAIGERR-Windows-Computer-16-inch-Display/dp/B0DS232QYY")

# Wait for the price element to load
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
try:
    price_whole = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))).text
    price_fraction = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction"))).text
    print(f"The price is {price_whole}.{price_fraction}")
except Exception as e:
    print("Price not found:", e)

# Close the driver
driver.quit()