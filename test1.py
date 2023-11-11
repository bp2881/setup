import os
import sys

# Define the name of the desktop entry and the command to run the script
desktop_entry = "temp.desktop"
# Replace with the actual path to your Python script
command = """x-terminal-emulator -e sudo python3 "/home/pranav/Downloads/side project/test2.py" """

# Define the contents of the desktop entry file
desktop_entry_content = f"""[Desktop Entry]
Type=Application
Name=My Startup Script
Exec={command}
X-GNOME-Autostart-enabled=true
"""

# Define the path to the autostart directory
autostart_dir = os.path.expanduser("~/.config/autostart")

# Create the desktop entry file
desktop_entry_path = os.path.join(autostart_dir, desktop_entry)
with open(desktop_entry_path, "w") as file:
    file.write(desktop_entry_content)

print(f"Desktop entry created: {desktop_entry_path}")
