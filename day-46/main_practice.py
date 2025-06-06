import requests
from bs4 import BeautifulSoup
#####################
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
#Request the web context
web = requests.get(url="https://www.billboard.com/charts/hot-100/", headers=header)
web_context = web.text
# print(web_context)
#BeautifulSoup engage
soup = BeautifulSoup(web_context, features="html.parser")
##Using CSS selector
# title_tag = soup.select("ul li h3")
# print(title_tag)

title_tag = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# print(title_tag)
# for title in title_tag:
#     title_context = title.getText()
#     print(title_context.strip())

# with open(file="./practice.txt", mode="w") as playlist:
#     for title in title_tag:
#         title_context = title.getText()
#         playlist.write(title_context.strip() + "\n")