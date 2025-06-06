from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_options = webdriver.ChromeOptions()#Allow you to configure Chrome setting before scraping
chrome_options.add_experimental_option("detach", True)#Allow you to stay on the website

#Launch Chrome with options
driver = webdriver.Chrome(options=chrome_options)

#Colect data
driver.get(url="https://secure-retreat-92358.herokuapp.com/")
#Find element by CSS selector and XPATH
# article = driver.find_element(By.XPATH, value="//*[@id='articlecount']/ul/li[2]/a[1]").text
# article = driver.find_element(By.CSS_SELECTOR, value="#articlecount li:nth-of-type(2) a")
# print(article.text)

#Find element by Link Test
# reference_desk = driver.find_element(By.LINK_TEXT, value="中文")
# reference_desk.click()

#Find search bar and search things
# search_bar = driver.find_element(By.NAME, value="search")
# search_bar.send_keys("Python", Keys.ENTER)

#Finish the challenge
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_up_button = driver.find_element(By.CSS_SELECTOR, ".btn-block")
first_name.send_keys("Shane")
last_name.send_keys("Hsieh")
email.send_keys("shane.hsieh@icloud.com")
sign_up_button.click()





driver.quit()