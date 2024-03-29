#Python GUI programming example. Create windows
import PySimpleGUI as sg # windows
import spacy #NLP
import en_core_web_sm
import os
os.chdir('/home/saul/pythontraining/NLP')

nlp = en_core_web_sm.load()

# GUI Application Class
class myApp:
    def __init__(self):
        #self.__build()
        self.journal = []
        self.__getFile()
    def __build(self):
        layout = [[sg.Text(self.journal)], [sg.Button("OK")]]
        # Create the window
        window = sg.Window("Demo", layout)
     
        # Create an event loop
        while True:
            event, values = window.read()
  
            # End program if user closes window or
            # presses the OK button
            if event == "OK" or event == sg.WIN_CLOSED:
                break
        window.close()
    
    # extract file
    def __getFile(self):   
        print("Get File")
        #return "Get File"
        with open("journal.txt", 'r') as file:
            self.journal = file.read()
        print(self.journal)
        #self.__build()

if __name__ == "__main__":
    windows = myApp()
    #windows.build()
