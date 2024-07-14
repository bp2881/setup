from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import shutil
from os import getcwd, path
from tqdm import tqdm

url = "https://repo.anaconda.com/archive/"
response = get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    reference_link = None
    for link in soup.find_all('a'):
        if "Linux-x86_64.sh" in link.text:
            reference_link = link.get('href')
            break

    if reference_link:
        print("Downloading Anaconda... Please wait")
        download_link = urljoin(url, reference_link)

        # Downloading Anaconda
        local_filename = download_link.split('/')[-1]
        file_path = path.join(getcwd(), local_filename)
        
        with get(download_link, stream=True) as r:
            total_size = int(r.headers.get('content-length', 0))
            chunk_size = 1024*1024
            with open(file_path, 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc=local_filename) as pbar:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))

        print(f"Anaconda downloaded as {local_filename}")
    else:
        print("No download link found for Anaconda")
else:
    print("Failed to retrieve Anaconda archive page.")
