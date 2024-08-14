import os
import sys
import time
import configparser
import subprocess
import importlib

# Configuration file path
CONFIG_FILE = 'config.ini'

# Default activity template
base_activity = {
    'details': 'MENTION YOUR ACTIVITY DETAILS',
    'state': 'MENTION STATE INFO',
    'assets': {
        'large_image': 'IMAGE_NAME_ONLY',  # Image names should match those in the Discord Developer Portal
        'large_text': 'IMAGE_NAME_ONLY',
        'small_image': 'ICON_NAME_ONLY',
        'small_text': 'HOVER_TEXT'
    },
    'party': {
        'size': [1, 5]  # Represents the number of people in the "party" and the maximum size
    },
    'buttons': [
        {'label': 'Contact', 'url': 'https://example.com/contact'},  # Replace with your contact URL
        {'label': 'Help', 'url': 'https://example.com/help'}  # Replace with your help URL
    ]
}

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"Package '{package}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

# Ensure required packages are installed
install_and_import('configparser')
install_and_import('discoIPC')

def create_config():
    config = configparser.ConfigParser()

    print("It seems like this is your first time running the app. Let's set it up!")
    client_id = input("Enter your Discord Client ID: ")
    
    config['CLIENT'] = {'client_id': client_id}
    
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    
    print("Configuration saved!")

def load_config():
    if not os.path.exists(CONFIG_FILE):
        create_config()

    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_FILE)
        client_id = config['CLIENT']['client_id']
        return client_id
    except KeyError:
        print("Error: 'client_id' not found in configuration file.")
        create_config()
        return load_config()

class DiscordActivity:
    def __init__(self, client_id):
        self.client = ipc.DiscordIPC(client_id)
        self.activity = base_activity

    def connect(self):
        try:
            self.client.connect()
            print('\nStarting Discord Activity...\n')
            time.sleep(5)
            self.update_activity()
        except Exception as e:
            print(f"Failed to connect to Discord: {e}")
            sys.exit(1)

    def update_activity(self):
        try:
            self.client.update_activity(self.activity)
            while True:
                input('\nConnected! Press Ctrl+C to disconnect.')
        except KeyboardInterrupt:
            print('Disconnecting...\n')
            self.client.disconnect()
        except Exception as e:
            print(f"Failed to update activity: {e}")

def ask_for_autostart():
    while True:
        choice = input("Would you like to add this script to start automatically when Windows starts? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Please answer 'y' for yes or 'n' for no.")

def add_to_startup():
    startup_script = os.path.abspath(sys.argv[0])
    startup_name = "DiscordActivity"

    if sys.platform == "win32":
        try:
            import winreg as reg

            key = reg.HKEY_CURRENT_USER
            startup_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
            with reg.OpenKey(key, startup_key, 0, reg.KEY_SET_VALUE) as registry_key:
                reg.SetValueEx(registry_key, startup_name, 0, reg.REG_SZ, startup_script)

            print(f"Added {startup_script} to startup.")
        except Exception as e:
            print(f"Failed to add to startup: {e}")
    else:
        print("Startup automation is only supported on Windows. Please add the script manually to startup.")

def main():
    client_id = load_config()
    helper = DiscordActivity(client_id)
    
    if ask_for_autostart():
        add_to_startup()

    helper.connect()

if __name__ == '__main__':
    main()
