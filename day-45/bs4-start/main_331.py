from bs4 import BeautifulSoup
import requests
#################
titles = []
links = []
scores = []
#################
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
web_page = response.text
# print(web_page)
soup = BeautifulSoup(web_page, "html.parser")
article_tag = soup.find_all(name="a",class_="storylink")

for tag in article_tag:
    text = tag.getText()#get the title
    titles.append(text)
    link = tag.get("href")
    links.append(link)

    # print(f"{text}\n{link}\n")

points = soup.find_all(name="span", class_="score")
# for score in points:
#     point = score.getText()
#     point = point.split()[0]
#     scores.append(point)
    # print(point)
#Same as list comprehensive
scores_list = [int(score.getText().split()[0]) for score in points]
scores = scores_list

# print(titles)
# print(links)
# print(scores_list)

# with open(file="web_page.txt", mode="a") as record:
#     for title, link, score in zip(titles, links, scores):
#         record.write(f"{title}\n{link}\n{score} points\n\n")

# scores = list(map(int, scores))
highest_score = max(scores)
highest_score_index = scores.index(highest_score)
# print(f"The highest score is {highest_score} and the index is {highest_score_index}")
print(f"The most review post of today is \n{titles[highest_score_index]}\n{links[highest_score_index]}\n{scores[highest_score_index]}")
