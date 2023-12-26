"""
started on 15 september 2023
Potential name - GraphySync (20/09/23)
# first version would be basic code with no major flaws
"""

from os import system
import distro
import platform
import importlib

# Checking platform

if platform.system() == "Linux":

    if distro.like().lower() == "arch":
        print("Sorry, still under development \n\n")
        importlib.import_module("arch")

    if distro.like().lower() == "debian":
        importlib.import_module("ubuntu")
        exit()

if platform.system() == "Windows":
    importlib.import_module("windows.py")

print(distro.id(), distro.version(), distro.name())
