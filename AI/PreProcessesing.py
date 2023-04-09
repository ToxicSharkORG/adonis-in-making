import nltk
from nltk import sent_tokenize as ST
from nltk import word_tokenize as WT
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords as SW
import os
file_dir = os.path.dirname(os.path.realpath(__file__))
print(file_dir)
print(os.getcwd(), ": original directory")
os.chdir(file_dir)
print("now running in", os.getcwd())
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

def processfile(filename):
    lemma = WordNetLemmatizer()
    stop = SW.words("english")
    #Read the file and take in text
    with open(filename, "r", encoding= "utf-8") as f:
        ttext = f.read()
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