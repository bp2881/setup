import subprocess

required_apps = ["visual studio code", "brave"]


def get_installed_apps():
    try:
        result = subprocess.check_output(['winget', 'list'], text=True)
        installed_apps = [line.split('\t')[0].strip().lower()
                          for line in result.split('\n') if line.strip()]
        return installed_apps
    except subprocess.CalledProcessError:
        return None


def app_installed_status(app, installed_apps):
    if any(app.lower() in installed_app for installed_app in installed_apps):
        print(f"{app} is already installed.")
    else:
        install_app(app)


def install_app(app):
    try:
        subprocess.run(["winget", "install", "--source", "winget", f"{app}"])

    except:
        print(f"Unable to install {app}")


installed_apps_list = get_installed_apps()

if installed_apps_list:
    print("Installed Apps:")
    for app in required_apps:
        app_installed_status(app, installed_apps_list)
else:
    print("Failed to retrieve the list of installed apps.")
