import os
import platform
import subprocess

# Determine the Operating System
os_type = platform.system()

# Define the OS-specific commands
commands = {
    'Windows': ['cmd.exe', '/c', 'dir'],
    'Linux': ['ls', '-l'],
    'Darwin': ['ls', '-l']  # Darwin is the system name for macOS
}

# Fetch the appropriate command based on the OS
command_to_run = commands.get(os_type)

# Execute the command
if command_to_run:
    result = subprocess.run(command_to_run, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
else:
    print(f"Unsupported operating system: {os_type}")
