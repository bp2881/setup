import ctypes
import os
import subprocess
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        return False


def run_as_admin():
    if is_admin():
        return True

    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if not is_admin():
    run_as_admin()
    sys.exit()


def pin_to_taskbar(app_name, app_path):
    try:
        # Get the user's APPDATA folder
        appdata_folder = os.environ['APPDATA']

        # Create a shortcut file (.lnk) in the APPDATA folder
        shortcut_path = os.path.join(appdata_folder, f"{app_name}.lnk")
        create_shortcut_command = f'rundll32.exe shell32.dll,Control_RunDLL desk.cpl,,1'

        subprocess.run(create_shortcut_command, shell=True)

        # Wait for a moment to ensure the shortcut creation has completed
        subprocess.run(['timeout', '/t', '2'], shell=True)

        # Move the shortcut to the Taskbar folder
        taskbar_folder = os.path.join(
            appdata_folder, 'Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\TaskBar')
        os.rename(shortcut_path, os.path.join(
            taskbar_folder, f"{app_name}.lnk"))

        print(f"{app_name} has been pinned to the taskbar.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
app_name = "Notepad"
app_path = os.path.join(os.environ["SystemRoot"], "notepad.exe")

pin_to_taskbar(app_name, app_path)
