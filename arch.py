import requests
from subprocess import run
from bs4 import BeautifulSoup
from os import system, path, getcwd
from tqdm import tqdm
from urllib.parse import urljoin
import shutil
import time

url = "https://repo.anaconda.com/archive/"

response = requests.get(url)
#print(response)

def install_anaconda(url):
    local_filename = url.split('/')[-1]
    file_path = path.join(getcwd(), local_filename)
    with requests.get(download_link, stream=True) as r:
        total_size = int(r.headers.get('content-length', 0))
        chunk_size = 1024*1024
        with open(file_path, 'wb') as f:
            with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc=local_filename) as pbar:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
    run(["bash", f"{local_filename}"])
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