from subprocess import getoutput, run
from os import system, path
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import shutil


required_apps = ["code", "brave-browser", "gnome-tweaks",
                 "gnome-shell-extensions", "conda"]



def notinstalled(app):

    # Installing brave-browser

    if "brave" in app:
        methods = {
            '1': "sudo apt -y install curl && sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg && echo 'deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main' | sudo tee /etc/apt/sources.list.d/brave-browser-release.list > /dev/null && sudo apt update && sudo apt -y install brave-browser",
            '2': "sudo snap install brave"
        }

        method = input(
            "Brave browser has 2 installation candidates\n[1] apt (repository)\t[2] snap\ndefault option[1]: ") or '1'

        try:
            system(methods.get(method, "Invalid option selected"))
        except Exception as e:
            print(f"Unable to install Brave browser: {e}\n")
            pass

    # Installing VS-code

    if "code" in app:
        methods = {
            '1': "sudo apt -y install wget gpg && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg && sudo sh -c 'echo \"deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list' && rm -f packages.microsoft.gpg && sudo apt install apt-transport-https && sudo apt update && sudo apt -y install code",
            '2': "sudo snap install code --classic"
        }

        method = input(
            "VS code has 2 installation candidates\n[1] apt (repository)\t[2] snap\ndefault option[1]: ") or '1'

        try:
            system(methods.get(method, "Invalid option selected"))
        except Exception as e:
            print(f"Could not install VS-Code: {e}\n")

    # Installing gnome-tweaks and gnome-extensions

    if "tweaks" in app:
        try:
            system("sudo apt -y install gnome-tweaks")

        except:
            print("Could not install gnome-tweaks...\n")
            pass

    if "extensions" in app:
        try:
            system("sudo apt -y install gnome-shell-extensions")

        except:
            print("Could not install gnome-extensions \n")
            pass

        print("Installing gnome-extensions-cli: \n")

    if "conda" in app:
        url = "https://repo.anaconda.com/archive/"
        response = requests.get(url)
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
            ## Downloading Anaconda
            local_filename = download_link.split('/')[-1]
            with requests.get(url, stream=True) as r:
                with open(local_filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
        



    # check what are installed and do a bit changes after windows
    print("\nCompleted")


def ubuntu23_04():
    app_list = str(run(["apt", "list", "--installed"], capture_output=True, text=True))
    existing_apps = None
    try:
        existing_apps = str(run([f"{app} -h"]))
    except:
        pass
    for app in required_apps:
        if app in app_list or existing_apps:
            print(f"Skipping... as {app} is already installed")
        else:
            notinstalled(app)


ubuntu23_04()
