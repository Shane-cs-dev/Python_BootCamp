from bs4 import BeautifulSoup

#Open file in location disk
with open(file="../bs4-start/website.html", mode="r") as web_html:
    file_content = web_html.read() #Read the file in plain text
    print(file_content)

soup = BeautifulSoup(file_content, "html.parser")
# print(soup.prettify())
all_anchor_tag = soup.find_all(name="a")
print(soup.find_all(name="a"))

# print(all_anchor_tag)
# for tag in all_anchor_tag:
#     text = tag.getText()
#     print(text)
#     link = tag.get("href")
#     print(link)

# company_url = soup.select(selector=".heading") #Can use cs selector
# print(company_url)