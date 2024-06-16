import requests
from bs4 import BeautifulSoup
from os import system

r = requests.get("https://repo.anaconda.com/archive/")
soup = BeautifulSoup(r.content, "html.parser")

# system("rm -rf archive.txt")
with open("archive.txt", "r+") as a:
    lines = a.readlines()
    for line in enumerate(lines, start=1):
        print(line)
        if "Linux" in line:
            print(line.strip())
