from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os
from requests.exceptions import ConnectTimeout, ConnectionError, SSLError, HTTPError
import re

def google(topic, num_results):
    urls = []
    for url in search(topic, num_results=num_results):
        urls.append(url)
    return urls

def preprocess(text):
    # Preprocess the text by removing non-alphanumeric characters and converting to lowercase
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = text.lower()
    return text

def extract_info(url):
    # Make a request to the URL and get the content
    response = requests.get(url)
    content = response.content

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(content, "html.parser")

    # Extract the relevant information from the webpage
    title = soup.find("title").text
    text = soup.find_all("p")
    text_str = "\n".join([p.text for p in text])
    preprocessed_text_str = preprocess(text_str)
    return title, text_str, preprocessed_text_str

while True:
    topic = input("Enter your search query: ")
    if topic == "quit":
        break
    num_results = 20
    urls = google(topic, num_results)
    # Create the textfiles folder if it doesn't exist
    os.makedirs("textfiles", exist_ok=True)
    ignored_domain = input("Enter the domain to be ignored (e.g. example.com): ")
    for idx, url in enumerate(urls):
        domain = url.split('/')[2]
        if domain == ignored_domain:
            print(f"Ignoring {url}")
            continue
        title, text, preprocessed_text = extract_info(url)
        print(f"Title ({idx+1}): {title}\n")
        try:
            with open(f"textfiles/{title.replace('|','_').replace(':','_').replace(';','_').replace('?','_')}.txt", "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n\n")
                f.write("Original text:\n\n")
                f.write(text + "\n\n")
                f.write("Preprocessed text:\n\n")
                f.write(preprocessed_text + "\n")
            print("Saved file.\n")
        except UnicodeEncodeError as ue:
            print(f"UnicodeEncodeError occurred: {ue}")
            print(f"Skipping {title}")
        except ConnectionError as ce:
            print(f"ConnectionError occurred: {ce}")
            print(f"Skipping {title}")
        except ConnectTimeout as ct:
            print(f"ConnectTimeout occurred: {ct}")
            print(f"Skipping {title}")
        except OSError as oe:
            if oe.errno != 2:
                print(f"OSError occurred: {oe}")
                print(f"Skipping {title}")
            else:
                print(f"{title} file does not exist.")
        except AttributeError as ae:
            print(f"AttributeError occurred: {ae}")
            print(f"Skipping {title}")
        except HTTPError as he:
            print(f"HTTPError occurred: {he}")
            print(f"Skipping {title}")
        except SSLError as se:
            print(f"SSLError occurred: {se}")
            print(f"Skipping {title}")
         # Remove the file if it is not a .txt

