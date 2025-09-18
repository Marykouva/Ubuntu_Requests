import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        # Check the URL response without downloading full content
        head_resp = requests.head(url, timeout=10)
        content_type = head_resp.headers.get('Content-Type', '')
        if 'image' not in content_type:
            print(f" Skipped: {url} is not an image.")
            return

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        # Check for duplicates
        filepath = os.path.join("Fetched_Images", filename)
        counter = 1
        while os.path.exists(filepath):
            name, ext = os.path.splitext(filename)
            filepath = os.path.join("Fetched_Images", f"{name}_{counter}{ext}")
            counter += 1

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f" Successfully fetched: {filename}")
        print(f" Saved to: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f" Connection error for {url}: {e}")
    except Exception as e:
        print(f" Error with {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory
    os.makedirs("Fetched_Images", exist_ok=True)

    # Get multiple URLs from user
    urls = input("Enter image URLs separated by commas: ").split(',')

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
