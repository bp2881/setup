import os
import subprocess

required_apps = open("required_apps.txt", "r+")
required_apps = str(required_apps.read())

installed_apps = subprocess.check_output(
    ["winget", "list"], universal_newlines=True).lower()

if required_apps in installed_apps:
    print("a")
else:
    print(installed_apps)
