import pandas as pd
import os
import psutil

class readFiles:
	name= 'read csv files'
	print('Read Files')
	
	
	def __init__(self):
		#self.read_memory()
		#print(psutil.virtual_memory())
		print('Virtual Memory Percent ', psutil.virtual_memory().percent)
		
	def read_memory(self):
		print(psutil.virtual_memory())
		
		
	


files = readFiles()
	#readFiles()
files

