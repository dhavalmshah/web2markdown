# Import the required modules
import requests
import html2markdown
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description="Convert a webpage to markdown")
parser.add_argument("url", type=str, help="The url of the webpage to convert")
parser.add_argument("-i", "--images", action="store_true", help="Include images in the markdown file")
args = parser.parse_args()

# Get the HTML content of the webpage
response = requests.get(args.url)
html = response.text

# Convert the HTML to markdown
markdown = html2markdown.convert(html)

# Save the markdown to a file
filename = args.url.split("/")[-1] + ".md"
with open(filename, "w") as f:
    f.write(markdown)

# Print a success message
print(f"Successfully converted {args.url} to {filename}")

# If images are enabled, download and save them to a folder
if args.images:
    # Import BeautifulSoup and os modules
    from bs4 import BeautifulSoup
    import os

    # Create a folder for images
    folder = args.url.split("/")[-1] + "_images"
    os.mkdir(folder)

    # Parse the HTML content and find all image tags
    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img")

    # Loop through each image tag and download the image
    for image in images:
        # Get the image source url
        src = image["src"]

        # If the image source is relative, append it to the base url
        if not src.startswith("http"):
            src = args.url + src

        # Get the image name from the source url
        name = src.split("/")[-1]

        # Download the image content
        img_response = requests.get(src)
        img_data = img_response.content

        # Save the image to the folder
        img_path = os.path.join(folder, name)
        with open(img_path, "wb") as f:
            f.write(img_data)

        # Print a message for each image downloaded
        print(f"Downloaded {src} to {img_path}")
