from subprocess import run
from ubuntu import notinstalled

required_apps = ["code", "brave-browser", "gnome-tweaks",
                 "gnome-shell-extensions", "conda"]

app_list = str(run(["apt", "list", "--installed"], capture_output=True, text=True))

for app in required_apps:
    if app == "code":
        code_installed = None
        try:
            code_installed = str(run([f"{app} -h"]))
        except:
            pass
        if code_installed != None:
            notinstalled(app)

    elif app in app_list and app != "code":
        print(f"Skipping... as {app} is already installed")

    else:
        notinstalled(app)
