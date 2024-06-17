import requests
from bs4 import BeautifulSoup
from os import system
from urllib.parse import urljoin
import shutil
import time

url = "https://repo.anaconda.com/archive/"

response = requests.get(url)
#print(response)

def install_anaconda(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    reference_link = None
    for link in soup.find_all('a'):
        if "Linux-x86_64.sh" in link.text:
            reference_link = link.get('href')
            break

    if reference_link:
        download_link = urljoin(url, reference_link)
        install_anaconda(download_link)