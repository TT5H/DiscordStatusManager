# Discord Status Manager

**Discord Status Manager** is a Python script that allows you to set and manage a custom Discord Rich Presence status. This script can be used to display custom activity details, images, and buttons directly on your Discord profile. It also includes the option to run automatically on Windows startup.

## Features

- **Custom Discord Rich Presence**: Easily customize your Discord status with specific activity details, images, and buttons.
- **Automatic Dependency Management**: The script automatically installs required Python packages if they are not already installed.
- **User-Friendly Setup**: Simple first-time setup that saves your Discord Client ID for future use.
- **Optional Windows Startup**: Option to run the script automatically when Windows starts.

## Requirements

- Python 3.6 or higher
- An active [Discord Developer Portal](https://discord.com/developers/applications) account with a Rich Presence application set up
- Internet connection for installing dependencies

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/TT5H/DiscordStatusManager.git
   cd DiscordStatusManager


## Run the Script

 - Execute the script using Python:

 - ```sh
    python app.py

 - During the first run, the script will prompt you to enter your Discord Client ID. You can obtain this from the Discord Developer Portal.

## Configuration

   The script will create a config.ini file to store your Discord Client ID.
     You can manually edit this file to change your client ID or update other configurations if necessary.



 ## Usage

  - First-Time Setup:
        On the first run, the script will ask for your Discord Client ID and whether you want the script to start automatically with Windows.
        Your settings will be saved for future use.

  - Subsequent Runs:
        The script will automatically load your saved configuration and update your Discord status accordingly.

  - Customizing the Rich Presence:
        To customize the activity details, images, and buttons, you can edit the base_activity dictionary in the app.py script.

## Advanced Customization

You can further customize the Discord Rich Presence by modifying the `base_activity` dictionary within `app.py`. Here are the key components you can adjust:

- **details**: A string representing the main activity details (e.g., "Playing a cool game").
- **state**: Additional information about the current state (e.g., "In the main menu").
- **assets**:
  - `large_image`: Name of the large image to display (uploaded via Discord Developer Portal).
  - `large_text`: Text that appears when hovering over the large image.
  - `small_image`: Name of the small image to display.
  - `small_text`: Text that appears when hovering over the small image.
- **party**:
  - `size`: A list representing the current party size and the maximum size.
- **buttons**: A list of dictionaries containing `label` and `url` keys, representing buttons that link to external sites.


## Troubleshooting

- **Error: `client_id` not found in configuration file**:
  - If you encounter this error, the script couldn't find your Discord Client ID in the `config.ini` file. You may need to re-run the script and enter your client ID again.

- **Failed to connect to Discord**:
  - Ensure that your Discord application is correctly set up in the Developer Portal and that the client ID is correctly entered.

- **Package installation issues**:
  - If the script fails to install necessary Python packages, manually install them using:
    ```sh
    pip install configparser discoIPC
    ```

## Contributing

Contributions are welcome! If you have suggestions for improving the script, feel free to submit a pull request or open an issue.
