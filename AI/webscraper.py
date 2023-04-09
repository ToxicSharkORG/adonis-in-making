import requests
from bs4 import BeautifulSoup
def scrape(url, output_file):
    # Make a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the main text content of the page (in the <div> with id "mw-content-text")
    content_div = soup.find("div", {"id": "mw-content-text"})

    # Extract all the text from the content div
    text = content_div.get_text()

    # Write the text to a file
    with open(output_file, "w") as file:
        file.write(text)

#usage : scrape("link", "file name")

def scrape_multiple(urls, output_files):
    for i in range(len(urls)):
        url = urls[i]
        output_file = output_files[i]
        # Make a GET request to the URL
        response = requests.get(url)

        # Create a BeautifulSoup object from the response content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the main text content of the page (in the <div> with id "mw-content-text")
        content_div = soup.find("div", {"id": "mw-content-text"})

        # Extract all the text from the content div
        text = content_div.get_text()

        # Write the text to a file
        with open(output_file, "w") as file:
            file.write(text)

