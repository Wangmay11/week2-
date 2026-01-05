import json
import random
import string
import os

FILE_NAME = "urls.json"

# Load existing data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        urls = json.load(file)
else:
    urls = {}

def generate_short_code(length=5):
    while True:
        code = "".join(random.choices(string.ascii_letters + string.digits, k=length))
        if code not in urls:
            return code

while True:
    print("\n--- URL Shortener ---")
    print("1. Shorten URL")
    print("2. Retrieve URL")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        long_url = input("Enter long URL: ")

        if long_url in urls.values():
            print("This URL is already shortened.")
        else:
            short_code = generate_short_code()
            urls[short_code] = long_url

            with open(FILE_NAME, "w") as file:
                json.dump(urls, file, indent=4)

            print("Short URL created:", short_code)

    elif choice == "2":
        short_code = input("Enter short code: ")

        if short_code in urls:
            print("Original URL:", urls[short_code])
        else:
            print("Short URL not found.")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
