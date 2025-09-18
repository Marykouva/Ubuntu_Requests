import requests
import os
from urllib.parse import urlparse

def main():
    print("Ubuntu To The World!!Image Fetcher")
    print("Here we go Ubuntu Lovers!!!\n")

    # Asks user image URL
    url = input(" Please enter image URL: ")

    try:
        # Create non-existent folder
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetches the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If URL has no filename, create one
            filename = "downloaded_image.jpg"

        # Saves image
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f" Successfully fetched: {filename}")
        print(f" Saved to: {filepath}")
        print("\n Ayekoo Ubuntu Community.")

    except requests.exceptions.RequestException as e:
        print(f" Connection error: {e}")
    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    main()
