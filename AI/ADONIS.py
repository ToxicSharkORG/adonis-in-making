'''import nltk
import requests
import numpy
from nltk import sent_tokenize as ST
from nltk import word_tokenize as WT
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords as SW
from bs4 import BeautifulSoup
import time
import datetime
nltk.download("all")

def preprocess(text):
    lemma = WordNetLemmatizer()
    stop = SW.words("english")

    # Lowercase the text
    ttext = text.lower()

    # Tokenize the text into sentences
    z = ST(ttext)

    tokened_sentences = []
    # Tokenize each sentence into words
    for sentence in z:
        a = WT(sentence)
        tokened_sentences.append(a)

    filtered_sentences = []
    # Lemmatize each word and remove stop words
    for sentence in tokened_sentences:
        filtered = [lemma.lemmatize(word) for word in sentence if word not in stop]
        filtered_sentences.append(filtered)

    return filtered_sentences

#usage : preprocess(text)

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

#usage : declare a list of urls with [] and output files with [] and then just, scrape_multiple(urls, file names)(in "")

# Get the current time
current_time = datetime.datetime.now()

# Print the current time
print("The current time is:", current_time.strftime("%I:%M:%S %p"))
'''
import nltk
import requests
import numpy
from nltk import sent_tokenize as ST
from nltk import word_tokenize as WT
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords as SW
from bs4 import BeautifulSoup
import time
import datetime
import os
   
nltk.download("all")

def preprocess(text):
    lemma = WordNetLemmatizer()
    stop = SW.words("english")

    # Lowercase the text
    ttext = text.lower()

    # Tokenize the text into sentences
    z = ST(ttext)

    tokened_sentences = []
    # Tokenize each sentence into words
    for sentence in z:
        a = WT(sentence)
        tokened_sentences.append(a)

    filtered_sentences = []
    # Lemmatize each word and remove stop words
    for sentence in tokened_sentences:
        filtered = [lemma.lemmatize(word) for word in sentence if word not in stop]
        filtered_sentences.append(filtered)

    return filtered_sentences

#usage : preprocess(text)

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

#usage : declare a list of urls with [] and output files with [] and then just, scrape_multiple(urls, file names)(in "")

# Get the current time
current_time = datetime.datetime.now()

# Print the current time
print("The current time is:", current_time.strftime("%I:%M:%S %p"))
