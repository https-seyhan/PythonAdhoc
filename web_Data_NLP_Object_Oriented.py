import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load("en_core_web_sm") # SpaCy NLP corpus
import urllib.request
# Create Object that reads data of a web page and remove stop words and tokenize words.
# The web page used is https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

class webData():
    
    def __init__(self):
        self.webText = []
        self.__textAnalysis()
        self.__printWords()

    def __textAnalysis(self):
        webData = urllib.request.urlopen('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt').read()
        doc = nlp(str(webData))
    
        for token in doc:
                if not token.is_stop:
                    #print(token.text, token.pos_, token.dep_)
                    self.webText.append(token.text)
    def __printWords(self):
        print("Words ", self.webText)

if __name__ == "__main__":
    webText = webData()
