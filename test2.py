from os import system

methods = {
    '1': "sudo apt install -y curl && sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg && echo 'deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main' | sudo tee /etc/apt/sources.list.d/brave-browser-release.list > /dev/null && sudo apt update && sudo apt install -y brave-browser",
    '2': "echo 'Add commands for repository installation method here'"
}

method = input("Brave browser has 2 installation candidates\n[1] apt (repository)\t[2] Add commands here\ndefault option[1]: ") or '1'

try:
    system(methods.get(method, "Invalid option selected"))
except Exception as e:
    print(f"Unable to install Brave browser: {e}\n")
    pass
