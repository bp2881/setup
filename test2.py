from subprocess import getoutput
from os import system, path


installed_list = ["hello", "code", "brave-browser", "gnome-tweaks",
                  "gnome-shell-extensions", "pipx", "asdf"]


def ubuntu23_04():
    i = 0

    while i < len(installed_list):
        if installed_list[i] in getoutput("dpkg --get-selections"):
            print(f"Skipping as {installed_list[i]} is already installed")
        else:
            notinstalled(f"{installed_list[i]}")
        i += 1


def notinstalled(app):

    # Installing brave-browser

    if "brave" in app:
        try:
            system("sudo apt install curl")
            system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
            system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
            system("sudo apt update && sudo apt install brave-browser")

        except:
            print("Unable to install brave...\n")
            pass

    # Installing VS-code

    if "code" in app:
        try:
            system("sudo apt-get install wget gpg")
            system(
                "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg")
            system(
                "sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg")
            system(
                """sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'""")
            system("rm -f packages.microsoft.gpg")
            system("sudo apt install apt-transport-https")
            system("sudo apt update && sudo apt install code")

        except:
            print("Could not install Vs-code \n")
            pass

    # Installing gnome-tweaks and gnome-extensions

    if "tweaks" in app:
        try:
            system("sudo apt install gnome-tweaks")

        except:
            print("Could not install gnome-tweaks \n")
            pass

    if "extensions" in app:
        try:
            system("sudo apt install gnome-shell-extensions")

        except:
            print("Could not install gnome-extensions \n")
            pass

    # moving  themes and icons
    print("Moving icons and themes: \n")
    # system("sudo mv /media/pranav/Ventoy/extra/McMojave-circle-blue ~/.icons/McMojave-circle-blue")
    # system("sudo mv /media/pranav/Ventoy/extra/WhiteSur-Dark ~/.themes/WhiteSur-Dark")

    """
    ALways do this at the end
    """

    # Installing pipx
    if "pipx" in app:

        print("Installing pipx: \n")
        try:
            system("sudo apt update -y && sudo apt install pipx -y")
            print("Adding pipx to path \n")
            system("pipx ensurepath")
        # before rebooting adding file to startup

            try:
                system("reboot")

            except Exception as e:
                print(e)

        except:
            print("Couldn't install pipx \n")
            pass

        print("Installing gnome-extensions-cli: \n")

    if "pipx" not in app:
        try:
            system("pipx install gnome-extensions-cli --system-site-packages")

        except:
            print("Couldn't install gnome-extension-cli \n")
            pass

    # try installing extensions
        print("Installing extensions: \n")
        try:
            system("gext install dash-to-dock@micxgx.gmail.com")
            system("gext install gnomebedtime@ionutbortis.gmail.com")
            system("gext install no-overview@fthx")
            system(
                "gext install notification-banner-reloaded@marcinjakubowski.github.com")
            system("gext install unlockDialogBackground@sun.wxg@gmail.com")
            system("gext install unredirect@vaina.lt")
            system("gext install user-theme@gnome-shell-extensions.gcampax.github.com")

        # enabling extensions

            system("gext enable dash-to-dock@micxgx.gmail.com")
            system("gext enable gnomebedtime@ionutbortis.gmail.com")
            system("gext enable no-overview@fthx")
            system(
                "gext enable notification-banner-reloaded@marcinjakubowski.github.com")
            system("gext enable unlockDialogBackground@sun.wxg@gmail.com")
            system("gext enable unredirect@vaina.lt")
            system("gext enable user-theme@gnome-shell-extensions.gcampax.github.com")

        except:
            with open("helo.txt", "w+") as de:
                de.write("Couldn't install extensions")
            print("Couldn't install extensions \n")

        # remove app from startup
        system("sudo rm -rf /etc/systemd/system/ScriptService.service")

    # check what are installed and do a bit changes after windows
    print("Completed")


ubuntu23_04()
