# Webpage to Markdown Converter

This is a python script that takes in a webpage url and outputs a markdown file. It also has an option to download and save images from the webpage.

## Prerequisites

To run this script, you need to have the following prerequisites:

- Python 3: This is the programming language used for the script. You can check if you have Python 3 installed by running this command in your terminal: `python --version`. If you see something like `Python 3.x.x`, then you have Python 3 installed. If not, you can download and install Python 3 from [here].
- Requests: This is a Python module that allows you to send HTTP requests and get the HTML content of webpages. You can check if you have requests installed by running this command in your terminal: `pip show requests`. If you see some information about the requests module, then you have requests installed. If not, you can install requests by running this command in your terminal: `pip install requests`.
- Html2markdown: This is a Python module that converts HTML to markdown using BeautifulSoup and html.parser. You can check if you have html2markdown installed by running this command in your terminal: `pip show html2markdown`. If you see some information about the html2markdown module, then you have html2markdown installed. If not, you can install html2markdown by running this command in your terminal: `pip install html2markdown`.
- BeautifulSoup: This is a Python module that parses HTML and XML documents and extracts data from them. You can check if you have BeautifulSoup installed by running this command in your terminal: `pip show beautifulsoup4`. If you see some information about the beautifulsoup4 module, then you have BeautifulSoup installed. If not, you can install BeautifulSoup by running this command in your terminal: `pip install beautifulsoup4`.
- Wheel: This is a Python package that supports binary distributions and faster installations. You can check if you have wheel installed by running this command in your terminal: `pip show wheel`. If you see some information about the wheel package, then you have wheel installed. If not, you can install wheel by running this command in your terminal: `pip install wheel`.

## Usage

To use this script, follow these steps:

- Download or clone this repository to your local machine.
- Open a terminal and navigate to the folder where the main.py file is located.
- Run the script with the url of the webpage you want to convert as an argument. You can also use the `-i` or `--images` flag to enable downloading images from the webpage. For example, if you want to convert https://www.smoothlineinks.com/about-us and include images, you can run this command: `python main.py https://www.smoothlineinks.com/about-us -i`. This will create a markdown file called about-us.md and a folder called about-us_images in your project folder.
- Enjoy your markdown file and images.

## License

This project is licensed under the MIT License