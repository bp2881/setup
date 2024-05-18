import requests
from bs4 import BeautifulSoup
from os import system

r = requests.get("https://repo.anaconda.com/archive/")
content = BeautifulSoup(r.content, "html.parser")
s = content.find('div', class_='entry-content')

system("rm -rf archive.txt")
with open("archive.txt", "w+") as a:
    a.write(str(content))
