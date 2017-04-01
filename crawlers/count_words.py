# -*- coding: UTF-8 -*-
import time, csv, re 
from datetime import datetime

# python -c "from count_words import *; count_words()"

input_file = 'jobslinks.csv'
output_file = '/home/saigesp/git/domestikrawler/a6b6f6d32d824dea8ab086c0dc8fe50e/jobswords.csv'

def cleanString(texto):
	texto = texto.decode('latin-1').encode('utf-8')
	texto = texto.lower()
	texto = texto.replace('.', ' ')
	texto = texto.replace('ñ', 'n')
	texto = texto.replace('á', 'a')
	texto = texto.replace('é', 'e')
	texto = texto.replace('í', 'i')
	texto = texto.replace('ó', 'o')
	texto = texto.replace('ú', 'u')
	texto = texto.replace('¿', ' ')
	texto = texto.replace('?', ' ')
	texto = texto.replace('(', ' ')
	texto = texto.replace(')', ' ')
	texto = texto.replace('-', ' ')
	texto = texto.replace('–', ' ')
	texto = texto.replace('+', ' ')
	texto = texto.replace('/', ' ')
	texto = texto.replace('<', ' ')
	texto = texto.replace('>', ' ')
	texto = texto.replace('«', ' ')
	texto = texto.replace('»', ' ')
	texto = texto.replace('´', ' ')
	texto = texto.replace('`', ' ')
	texto = texto.replace('"', ' ')
	texto = texto.replace('  ', ' ')
	texto = texto.replace('  ', ' ')
	texto = texto.replace('disenadores', 'disenador')
	return texto

def count_words():
	seen = {
		'total':				0,
		'noprogramador':		0,
		'programador':		 	0,
	}

	with open(input_file, 'rt') as read_csv, open(output_file, 'w') as write_csv:
		writer = csv.writer(write_csv, delimiter=',',lineterminator='\n')
		reader = csv.reader(read_csv, delimiter = ',')
		last_date = '201704'
		data = ['yyyymm']
		for key in seen:
			data.append(key)
		writer.writerow(data)
		for row in reader:
			seen['total'] += 1
			if 'wordpress' in cleanString(row[2]): seen['programador'] += 1
			elif 'web' in cleanString(row[2]): seen['programador'] += 1
			elif 'app' in cleanString(row[2]): seen['programador'] += 1
			elif 'ios' in cleanString(row[2]): seen['programador'] += 1
			elif 'softw' in cleanString(row[2]): seen['programador'] += 1
			elif 'android' in cleanString(row[2]): seen['programador'] += 1
			elif 'programador' in cleanString(row[2]): seen['programador'] += 1
			elif 'programacion' in cleanString(row[2]): seen['programador'] += 1
			elif 'desarroll' in cleanString(row[2]): seen['programador'] += 1
			elif 'develo' in cleanString(row[2]): seen['programador'] += 1
			elif 'mobile' in cleanString(row[2]): seen['programador'] += 1
			elif 'ecommerce' in cleanString(row[2]): seen['programador'] += 1
			elif 'front' in cleanString(row[2]): seen['programador'] += 1
			elif 'html' in cleanString(row[2]): seen['programador'] += 1
			elif 'css' in cleanString(row[2]): seen['programador'] += 1
			elif 'java' in cleanString(row[2]): seen['programador'] += 1
			elif 'php' in cleanString(row[2]): seen['programador'] += 1
			elif 'datos' in cleanString(row[2]): seen['programador'] += 1
			elif 'data' in cleanString(row[2]): seen['programador'] += 1
			elif 'flash' in cleanString(row[2]): seen['programador'] += 1
			elif 'ui' in cleanString(row[2]): seen['programador'] += 1
			elif 'ux' in cleanString(row[2]): seen['programador'] += 1
			elif 'director' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'direcc' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'arte' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'arti' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'art director' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'graphic' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'grafi' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'tipog' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'industr' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'maqueta' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'copy' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'ejecuti' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'fotog' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'motion' in cleanString(row[2]): seen['noprogramador'] += 1
			elif '3d' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'edit' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'packa' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'indesi' in cleanString(row[2]): seen['noprogramador'] += 1
			elif 'multim' in cleanString(row[2]): seen['noprogramador'] += 1

			date = row[0].split('-')
			yyyymm = date[0]+date[1]
			
			print(row[0],cleanString(row[2]))
			if not last_date == yyyymm:
				last_date = yyyymm
				data = [str(int(yyyymm)+1)]
				for key in seen:
					data.append(seen[key])
				writer.writerow(data)
				seen = {
					'total':				0,
					'noprogramador':		0,
					'programador':		 	0,
				}

		print(seen)
