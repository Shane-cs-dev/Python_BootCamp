import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_content = response.text
# print(web_content)

soup = BeautifulSoup(web_content, "html.parser")
title_tag = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in title_tag]
new_movies_list = movies[::-1]#[start:stop:step]
print(movies)

with open(file="movie_list.txt", mode="w") as movielist:
    for ori_movie, movie in zip(movies, new_movies_list):
        movielist.write(f"{movie}\n")


