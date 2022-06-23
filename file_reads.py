import pandas as pd
import os
import psutil
import datetime
import json
import eml_parser

class readFiles:
	name= 'read csv files'
	print('Read Files')
	
	
	def __init__(self):
		#self.read_memory()
		#print(psutil.virtual_memory())
		print('Virtual Memory Percent ', psutil.virtual_memory().percent)
		print(psutil)
		self.read_eml_file()
		
	def read_memory(self):
		print(psutil.virtual_memory())
	
	def read_eml_file(self):
		with open('sample_file.eml', 'rb') as email:
  			raw_email = email.read()

	

#files = readFiles()
readFiles()
#files

