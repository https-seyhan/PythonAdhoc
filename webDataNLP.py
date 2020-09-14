import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load("en_core_web_sm")
import urllib.request

class webData():
    def __init__(self):
        textWords = []
        self.__textAnalysis()

    def __textAnalysis(self):
        webData = urllib.request.urlopen('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt').read()
        doc = nlp(str(webData))
        for token in doc:
                if not token.is_stop:
                    print(token.text, token.pos_, token.dep_)

if __name__ == "__main__":
    print("Web Called")
    webText = webData()