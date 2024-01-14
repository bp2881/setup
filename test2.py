from os import system

print("Installing extensions: \n")
extensions = [
    "dash-to-dock@micxgx.gmail.com",
    "gnomebedtime@ionutbortis.gmail.com",
    "no-overview@fthx",
    "notification-banner-reloaded@marcinjakubowski.github.com",
    "unlockDialogBackground@sun.wxg@gmail.com",
    "unredirect@vaina.lt",
    "user-theme@gnome-shell-extensions.gcampax.github.com"
]

try:
    for extension in extensions:
        system(f"gnome-extensions install {extension}")
        system(f"gnome-extensions enable {extension}")
except Exception as e:
    print(f"Unable to install/enable extensions: {e}\n")
    pass