from subprocess import getoutput
from os import system, path
import time


required_apps = ["code", "brave-browser", "gnome-tweaks",
                 "gnome-shell-extensions", "pipx"]


def desktop_app():

    # Define the name of the desktop entry and the command to run the script
    desktop_entry = "temp.desktop"

    command = f"""x-terminal-emulator -e sudo python3 "{path.dirname(__file__)}/{path.basename(__file__)}" """

    # Define the contents of the desktop entry file
    desktop_entry_content = f"""[Desktop Entry]
    Type=Application
    Name=My Startup Script
    Exec={command}
    X-GNOME-Autostart-enabled=true
    """

    # Define the path to the autostart directory
    autostart_dir = path.expanduser("~/.config/autostart")

    # Create the desktop entry file
    desktop_entry_path = path.join(autostart_dir, desktop_entry)
    with open(desktop_entry_path, "w") as file:
        file.write(desktop_entry_content)

    print(f"Desktop entry created: {desktop_entry_path}")


def notinstalled(app):

    # Installing brave-browser
    
    if "brave" in app:
        methods = {
        '1': "sudo apt install -y curl && sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg && echo 'deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main' | sudo tee /etc/apt/sources.list.d/brave-browser-release.list > /dev/null && sudo apt update && sudo apt install -y brave-browser",
        '2': "sudo snap install brave"
        }

        method = input("Brave browser has 2 installation candidates\n[1] apt (repository)\t[2] snap\ndefault option[1]: ") or '1'

        try:
            system(methods.get(method, "Invalid option selected"))
        except Exception as e:
            print(f"Unable to install Brave browser: {e}\n")
            pass

    # Installing VS-code

    if "code" in app:
        methods = {
        '1': "sudo apt install wget gpg && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg && sudo sh -c 'echo \"deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list' && rm -f packages.microsoft.gpg && sudo apt install apt-transport-https && sudo apt update && sudo apt install code",
        '2': "sudo snap install code --classic"
        }

        method = input("VS code has 2 installation candidates\n[1] apt (repository)\t[2] snap\ndefault option[1]: ") or '1'

        try:
            system(methods.get(method, "Invalid option selected"))
        except Exception as e:
            print(f"Could not install VS-Code: {e}\n")


    # Installing gnome-tweaks and gnome-extensions

    if "tweaks" in app:
        try:
            system("sudo apt install gnome-tweaks")

        except:
            print("Could not install gnome-tweaks...\n")
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
    Always do this at the end
    """

    # Installing pipx
    if "pipx" in app:

        print("Installing pipx: \n")
        try:
            system("sudo apt update -y && sudo apt install pipx -y")
            print("Adding pipx to path \n")
            system("pipx ensurepath")
            # before rebooting adding file to startup
            
            desktop_app()

            try:
                print("\nRebooting in 5 seconds")
                time.sleep(5)
                system("reboot")

            except Exception as e:
                print(e)

        except:
            print("Couldn't install pipx \n")
            pass

        print("Installing gnome-extensions-cli: \n")

    # try installing extensions


        # remove app from startup
        system(f"sudo rm -rf {desktop_app}")

    # check what are installed and do a bit changes after windows
    print("Completed")


def ubuntu23_04():
    i = 0

    while i < len(required_apps):
        if required_apps[i] in getoutput("dpkg --get-selections"):
            print(f"Skipping as {required_apps[i]} is already installed")
        else:
            notinstalled(f"{required_apps[i]}")
        i += 1
    
    if "pipx" in getoutput("dpkg --get-selections"):
        system("pipx install gnome-extensions-cli --system-site-packages")


ubuntu23_04()