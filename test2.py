from os import system

from pathlib import Path


# file name to be executed or current file name with full path
file_name = f"{Path(__file__).absolute()}"
File_object = open(
    r"/", "a")
File_object.write(
    f"""[Unit] \nDescription=Custom Script, Will Be Deleted \n[Service] \nExecStart=sudo /usr/bin/python3 "{file_name}" \n[Install] \nWantedBy=default.target""")
system("sudo systemctl unmask ScriptService.service")
system("sudo systemctl enable ScriptService")
