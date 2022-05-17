import pandas as pd
import os
import psutil

class readFiles:
	name= 'read csv files'
	print('Read Files')
	
	def __init__(self):
		print(psutil.virtual_memory())
		
		
	

if '__name__' == '__main_':
	files = readFiles()

