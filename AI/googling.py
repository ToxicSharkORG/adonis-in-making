from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os
from requests.exceptions import ConnectTimeout, ConnectionError, SSLError, HTTPError

def google(topic, num_results):
    urls = []
    for url in search(topic, num_results=num_results):
        urls.append(url)
    return urls

def extract_info(url):
    # Make a request to the URL and get the content
    response = requests.get(url)
    content = response.content

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(content, "html.parser")

    # Extract the relevant information from the webpage
    title = soup.find("title").text
    text = soup.find_all("p")
    return title, text

while True:
    topic = input("Enter your search query: ")
    if topic == "quit":
        break
    num_results = 6
    urls = google(topic, num_results)
    # Create the textfiles folder if it doesn't exist
    os.makedirs("textfiles/Unsupervised", exist_ok=True)
    ignored_domain = input("Enter the domain to be ignored (e.g. example.com): ")
    for idx, url in enumerate(urls):
        domain = url.split('/')[2]
        if domain == ignored_domain:
            print(f"Ignoring {url}")
            continue
        title, text = extract_info(url)
        print(f"Title ({idx+1}): {title}\n")
        try:
            with open(f"textfiles/unsupervised/{title.replace('|','_').replace(':','_').replace(';','_').replace('?','_')}.txt", "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n\n")
                for p in text:
                    print(p.text)
                    f.write(p.text + "\n")
                print("\n")
                f.write("\n")
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
        # Remove the file if it is not a .txt file
        if not title.endswith(".txt"):
            try:
                file_path = f"textfiles/{title.replace('|','_').replace(':','_').replace(';','_').replace('?','_')}"
                os.remove(file_path)
                print(f"Removed {file_path} file.")
            except OSError as oe:
                print(f"OSError occurred: {oe}")
                print(f"Skipping {title}")
