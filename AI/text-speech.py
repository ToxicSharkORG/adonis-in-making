import pyttsx3
import os

def changedir(): 
    file_dir = os.path.dirname(os.path.realpath(__file__))
    print(file_dir)
    print(os.getcwd(), ": original directory")
    os.chdir(file_dir)
    print("now running in", os.getcwd())

changedir()

# initialize the speech engine
engine = pyttsx3.init()

# get input text from the user
while True:
    filename = input("Enter the file name: ")
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # set the engine properties
    engine.setProperty('rate', 150)    # setting the speech rate
    engine.setProperty('volume', 1)    # setting the volume level

    # convert text to speech
    engine.say(text)
    engine.runAndWait()
