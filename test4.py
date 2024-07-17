from os import remove
from subprocess import getoutput, run

app_list = str(run(["apt", "list", "--installed", ">", "m.txt"], capture_output=True, text=True))

"""required_apps = ["code", "brave-browser", "gnome-tweaks",
                 "gnome-shell-extensions", "conda"]

with open("m.txt", "r") as h:
    content = h.readlines()
remove("m.txt")

for line in content:
    for app in required_apps:
        d = False
        if app in line:
            if app == line[:len(app):]:
                print("Already Installed")
                with open("m.txt", "a") as h:
                    h.write(app)"""