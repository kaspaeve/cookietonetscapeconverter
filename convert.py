import json
import os
import sys

def print_help():
    print("""
Usage: python3 convert.py [options]

Welcome to the Cookie-to-Netscape Converter — your go-to tool for transforming browser cookies 
(exported in JSON format) into the Netscape HTTP Cookie format.

Why is this awesome?
- yt-dlp (the advanced YouTube downloader) needs cookies in the Netscape format to bypass age 
  restrictions, login screens, and other annoyances.
- With this script, you’ll easily convert your cookies to that format, ready for yt-dlp and other 
  automation tools.

Options:
    --help              Show this help message and exit
    <filename>          Specify the cookies file name (default: cookies.json)

Example:
    python3 convert.py        # Converts cookies.json into cookies.txt
    python3 convert.py custom_cookies.json  # Converts custom_cookies.json into cookies.txt

Once converted, your cookies will be saved as cookies.txt and ready for use in automation, scraping, 
and bypassing pesky pop-ups.
""")

if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

print("""
Welcome to the Cookie-to-Netscape Converter 1.0!

This script will take your browser's cookies.json file (exported from your browser) and convert it 
into the widely-used Netscape HTTP Cookie format. Once converted, you’ll have a cookies.txt file 
that can be used for web scraping, downloading videos, and bypassing age verifications and login screens.

Here’s the cool part: You’re about to take raw browser data and transform it into something that 
makes web automation feel like a breeze. All you need to do is press Enter to continue, or specify 
your custom cookies file name below.

Let's get started:
""")

filename = input("Example: cookies.json converts to Netscape cookies.txt\nEnter the cookies file name (default: cookies.json): ") or "cookies.json"

if not os.path.exists(filename):
    print(f"Error: '{filename}' does not exist.")
    exit(1)

output_file = 'cookies.txt'
if os.path.exists(output_file):
    while True:
        overwrite = input(f"'{output_file}' already exists. Do you want to overwrite it? (y/n): ").lower()
        if overwrite == 'y':
            break
        elif overwrite == 'n':
            while True:
                action = input("Press Enter to retry with a new file name or type 'e' to exit: ").lower()
                if action == '':
                    filename = input("Enter the new cookies file name (default: cookies.json): ") or "cookies.json"
                    
                    if os.path.exists(filename):
                        break
                    else:
                        print(f"Error: '{filename}' does not exist.")

                elif action == 'e':
                    print("Exiting without making changes.")
                    exit(0)
                else:
                    print("Invalid option. Press Enter to retry or type 'e' to exit.")
        else:
            print("Invalid option. Press Enter to retry or type 'n' to cancel overwriting.")

try:
    with open(filename, 'r') as f:
        data = json.loads(f.read())
except json.JSONDecodeError as e:
    print(f"Error: Failed to decode JSON from '{filename}'. Check the file format. ({e})")
    exit(1)

try:
    with open(output_file, 'w') as write:
        write.write("# Netscape HTTP Cookie File\n# https://curl.haxx.se/docs/http-cookies.html\n# This file was generated by libcurl! Edit at your own risk.\n\n")

        def boolToString(s):
            return "TRUE" if s else "FALSE"

        def checkTailMatch(s):
            return "TRUE" if s[0] == "." else "FALSE"

        cookies_written = 0
        for x in data:
            try:
                domain = x.get("Host raw", "")
                path = x.get("Path raw", "")
                secure = x.get("Send for raw", "").lower() == "true"
                name = x.get("Name raw", "")
                value = x.get("Content raw", "")

                if not domain or not path or not name or not value:
                    print(f"Warning: Skipping invalid cookie (missing fields): {x}")
                    continue

                if x.get("HTTP only raw") == "true":
                    write.write("#HttpOnly_")
                
                write.write(f"{domain}\t{checkTailMatch(domain)}\t{path}\t{boolToString(secure)}\t0\t{name}\t{value}\n")
                cookies_written += 1

            except KeyError as e:
                print(f"KeyError: Missing {e} in cookie data: {x}")

        print(f"Finished processing cookies. {cookies_written} valid cookies written to '{output_file}'.")

except IOError as e:
    print(f"Error: Failed to open or write to '{output_file}'. ({e})")
    exit(1)