import requests
import json
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
headers = {"User-Agent": "Mozilla/5.0"}
Response = requests.get(url, headers=headers)
soup = BeautifulSoup(Response.content, "html.parser")
# print(soup.prettify)

titles = soup.find_all("span", class_="titleline")
scores = soup.find_all("span", class_="score")
users = soup.find_all("a", class_="hnuser")
ages = soup.find_all("span", class_="age")

length = min(len(titles), len(scores), len(users), len(ages))
articles = []

for i in range(length):
    titleLink = titles[i].find("a")
    ageLink = ages[i].find("a")
    title = titleLink.text
    score = scores[i].text
    user = users[i].text
    age = ageLink.text

    article = {"index": i + 1, "title": title, "score": score, "user": user, "age": age}
    articles.append(article)

# for article in articles:
#     print(article)

json_object = json.dumps(articles, indent=4)

with open("articles.json", "w") as outputfile:
    outputfile.write(json_object)
