
required_apps = ["code", "brave-browser", "gnome-tweaks",
                 "gnome-shell-extensions", "conda"]

with open("m.txt", "r") as h:
    content = h.read().lower()
    for app in required_apps:
        if app in content:
            print(app)