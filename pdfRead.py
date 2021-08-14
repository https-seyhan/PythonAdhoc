import PyPDF2
import os
os.chdir('/home/saul/Business')

def Read(startPage, endPage):
    global text
    text = []
    cleanText = ""
    pdfFileObj = open('usaassangejudgement.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #PDF Reader
  
    while startPage <= endPage:
        pageObj = pdfReader.getPage(startPage)
        text += pageObj.extractText()
        startPage += 1
    pdfFileObj.close()
    
    for myWord in text:
        if myWord != '\n':
            cleanText += myWord
    text = cleanText.split()
    print(text)
Read(0,0)
