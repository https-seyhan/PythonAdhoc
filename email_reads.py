import pandas as pd
import os
import psutil
import datetime
import json
import eml_parser

os.chdir('/home/saul/kaggle')

class readFiles:
	name= 'read email files'#print('Received Domain', json_object['header']['received_domain'], '\n')
	email_details = []

	def __init__(self):
		self.email_context = [['', '','', '', '', '']]
		self.read_eml_file()

	def read_eml_file(self):
		with open('sample_file.eml', 'rb') as email:
  			raw_email = email.read()
		
		ep = eml_parser.EmlParser()
		parsed_eml = ep.decode_email_bytes(raw_email)
		#print(json.dumps(parsed_eml))
		self.get_information(json.dumps(parsed_eml, indent=4, sort_keys=True, default=str))

	def get_information(self, text):
		#print('Email Text ', text)
		#print(type(text))
		json_data = json.loads(text)
		self.get_header(json_data)

	def get_header(self, json_object):
		#print('Date ', json_object['header']['date'], '\n')
		#print('From ', json_object['header']['from'], '\n')
		#print('Received ', json_object['header']['received'], '\n')
		for item in json_object['header']:
			#print(item)
			#print(item['date'])
			if item == 'received':
				#print('Received called')
				#print(len(json_object['header']['received']))
				for element in range(len(json_object['header']['received'])):
					#print('Received elements ', json_object['header']['received'][element])
					elements = list(json_object['header']['received'][element].items())
					readFiles.email_details.append(elements)
		
		
		for list_recurse in range(len(readFiles.email_details)):
			for list_element in range(len(readFiles.email_details[list_recurse])):
				print('Tuple Size ', len(readFiles.email_details[list_recurse][list_element]))
				tuple_element = 0
				print('List Element Size ', list_element)
				print('List ', readFiles.email_details[list_recurse][list_element])
				
				while tuple_element < list_element:
					print('tuple_element ', tuple_element)
					#print('tuple_element size ', len(tuple_element))
					print("Elements ", readFiles.email_details[list_recurse][list_element][tuple_element])
					read_element = readFiles.email_details[list_recurse][list_element][tuple_element]
					print('Type ', type(read_element))
					tuple_element += 1
					




#files = readFiles()
readFiles()
#files
