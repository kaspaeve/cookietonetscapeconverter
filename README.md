
# Cookie-to-Netscape Converter

This is a Python script that converts browser cookies (exported in JSON format) into the widely-used Netscape HTTP Cookie format. The resulting `cookies.txt` file can be used for tools like yt-dlp to bypass restrictions like age verification and login requirements.

## Features

- Converts `cookies.json` (exported from your browser) into `cookies.txt` in the Netscape format.
- Supports custom cookies file names and handles file existence checks to avoid overwriting without confirmation.
- Enables web automation, bypassing login screens, age-verifications, and more.

## Installation

1. Clone or download the repository to your local machine.
   
2. Make sure you have Python 3 installed. You can check this by running:

   ```bash
   python3 --version
   ```

   If not installed, follow the installation instructions on the official [Python website](https://www.python.org/downloads/).

3. No additional dependencies are required as the script uses built-in Python libraries.

## Usage

1. Navigate to the folder containing the script and your `cookies.json` file.
   
   ```bash
   cd /path/to/your/folder
   ```

2. Run the script:

   ```bash
   python3 convert.py
   ```

   - The script will prompt you for the file name (default is `cookies.json`).
   - If the specified file does not exist, it will display an error and exit.
   - If `cookies.txt` already exists, it will prompt whether you want to overwrite it or not. You can also retry by providing a new file name.

   Example:
   ```bash
   Enter the cookies file name (default: cookies.json): cookies.json
   'cookies.txt' already exists. Do you want to overwrite it? (y/n): y
   Finished processing cookies. 21 valid cookies written to 'cookies.txt'.
   ```

3. Your cookies will be saved in the `cookies.txt` file, ready for use.

### Options

- **--help**: Displays the help message with usage instructions.

## Example

To use a custom cookies file, specify its name when prompted:

```bash
Enter the cookies file name (default: cookies.json): custom_cookies.json
```

If no file name is provided, it will default to `cookies.json`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
