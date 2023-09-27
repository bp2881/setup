from os import system, environ, path
from subprocess import getoutput
import sys
from pathlib import Path


# file name to be executed or current file name with full path

# checking priv.
if not 'SUDO_UID' in environ.keys():
    print("this program requires super user priv.")
    sys.exit(1)


def check_brave_installed():
    try:
        # Run the dpkg command and redirect its output to /dev/null
        output = getoutput("dpkg --get-selections")

        # Check if "brave" is in the output
        if "brave-browser" or "brave" in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def check_gnometweaks_installed():
    try:
        # Run the dpkg command and redirect its output to /dev/null
        output = getoutput("dpkg --get-selections")

        # Check if "tweaks" is in the output
        if "gnome-tweaks" in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def check_vscode_installed():
    try:
        # Run the dpkg command and redirect its output to /dev/null
        output = getoutput("dpkg --get-selections")

        # Check if "code" is in the output
        if "code" in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def check_gnome_extension_installed():
    try:
        # Run the dpkg command and redirect its output to /dev/null
        output = getoutput("dpkg --get-selections")

        # Check if "extensions" is in the output
        if "gnome-shell-extensions" in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def check_pipx_installed():
    try:
        # Run the dpkg command and redirect its output to /dev/null
        output = getoutput("dpkg --get-selections")

        # Check if "pipx" is in the output
        if "pipx" in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def ubuntu23_04():

    # install brave
    print("Installing brave: \n")

    if not (check_brave_installed()):

        try:
            system("sudo apt install curl")
            system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")  # type: ignore
            system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
            system("sudo apt update && sudo apt install brave-browser")

        except:
            print("Could not install brave \n")
            pass

    else:
        print("Brave browser is already installed \n")

    # install vscode
    print("Installing Vs Code: \n")

    if not (check_vscode_installed()):

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

    else:
        print("Vs Code is already installed \n")

    # install tweaks and extensions

    print("Installing gnome-tweaks && gnome-extensions: \n")
    if not (check_gnometweaks_installed()):
        try:
            system("sudo apt install gnome-tweaks")
        except:
            print("Could not install gnome-tweaks \n")
            pass
    else:
        print("Gnome-tweaks is already installed \n")

    if not (check_gnome_extension_installed()):
        try:
            system("sudo apt install gnome-shell-extensions")
        except:
            print("Could not install gnome-extensions \n")
            pass
    else:
        print("Gnome-extensions is already installed \n")
    # moving  themes and icons
    print("Moving icons and themes: \n")
    # system("mv /media/pranav/Ventoy/extra/McMojave-circle-blue ~/.icons/McMojave-circle-blue")
    # system("mv /media/pranav/Ventoy/extra/WhiteSur-Dark ~/.themes/WhiteSur-Dark")

    """
    ALways do this at the end
    """
    # gnome extension & pipx
    print("Installing pipx: \n")
    if not (check_pipx_installed()):
        try:
            system("sudo apt update && sudo apt install pipx")
            print("Adding pipx to path \n")
            system("pipx ensurepath")
            # before rebooting adding file to startup

            try:
                print("running this \n")

            except Exception as e:
                print(e)

        except:
            print("Couldn't install pipx \n")

            pass
    else:
        print("pipx is alreaddy installed \n")
        system(f'reboot')

    print("Installing gnome-extensions-cli: \n")
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
        system(
            "gext install user-theme@gnome-shell-extensions.gcampax.github.com")

        # enabling extensions

        system("gext enable dash-to-dock@micxgx.gmail.com")
        system("gext enable gnomebedtime@ionutbortis.gmail.com")
        system("gext enable no-overview@fthx")
        system(
            "gext enable notification-banner-reloaded@marcinjakubowski.github.com")
        system("gext enable unlockDialogBackground@sun.wxg@gmail.com")
        system("gext enable unredirect@vaina.lt")
        system(
            "gext enable user-theme@gnome-shell-extensions.gcampax.github.com")

    except:
        print("Couldn't install extensions \n")

    # remove app from startup
    system("sudo rm -rf /etc/systemd/system/ScriptService.service")

    # check what are installed and do a bit changes after windows
    print("Completed")


ubuntu23_04()
