import pandas as pd
import os
import psutil

class readFiles:
	name= 'read csv files'
	print('Read Files')
	print(psutil.virtual_memory())
	
	def __init__(self):
		#self.read_memory()
		print(psutil.virtual_memory())
		
	def read_memory(self):
		print(psutil.virtual_memory())
		
		
	

if '__name__' == '__main_':
	files = readFiles()
	files

