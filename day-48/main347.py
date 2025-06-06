from selenium import webdriver
from selenium.webdriver.common.by import By



WEB = "https://www.python.org/"
#Create Chrome option object
chrome_options = webdriver.ChromeOptions()#Allow you to configure Webdriver setting before launching the browser
chrome_options.add_experimental_option("detach", value=True)#Ensure Chrome Browser stay open

#Launch Chrome with options
driver = webdriver.Chrome(options=chrome_options)

#Collecting data
driver.get(url=WEB)
event_time = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last time")
event_name =driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

#Utilize enumerate
event = {i: {"time": time.text, "name": name.text} for i, (time, name) in enumerate(zip(event_time, event_name))}
print(event)


