# -*- coding: UTF-8 -*-
import time, csv, re 
from datetime import datetime

# python -c "from count_words import *; count_words()"

input_file = 'jobslinks.csv'
output_file = 'jobswords.csv'

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
		'flash':				0,
		'motion graphics':		0,
		'grafico':				0,
		'web':					0,
		'data':					0,
		'director de arte': 	0,
		'programador':		 	0,
		'wordpress':		 	0,
		'maquetador':		 	0,
		'ux':				 	0,
		'ui':				 	0,
		'video':			 	0,
		'ios':				 	0,
		'android':			 	0,
		'game':				 	0,
		'mobile':			 	0,
		'ecommerce':			0,
		'frontend':				0,
		'industrial':			0,
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
			if 'flash' in cleanString(row[2]): seen['flash'] += 1
			if 'wordpress' in cleanString(row[2]): seen['wordpress'] += 1
			if 'grafic' in cleanString(row[2]): seen['grafico'] += 1
			if 'graphic' in cleanString(row[2]): seen['grafico'] += 1
			if 'maquetador' in cleanString(row[2]): seen['maquetador'] += 1
			if 'director de arte' in cleanString(row[2]): seen['director de arte'] += 1
			if 'art director' in cleanString(row[2]): seen['director de arte'] += 1
			if 'web' in cleanString(row[2]): seen['web'] += 1
			if 'ios' in cleanString(row[2]): seen['ios'] += 1
			if 'android' in cleanString(row[2]): seen['android'] += 1
			if 'data' in cleanString(row[2]): seen['data'] += 1
			if 'ux' in cleanString(row[2]): seen['ux'] += 1
			if 'ui' in cleanString(row[2]): seen['ui'] += 1
			if 'game' in cleanString(row[2]): seen['game'] += 1
			if 'video' in cleanString(row[2]): seen['video'] += 1
			if 'programador' in cleanString(row[2]): seen['programador'] += 1
			if 'programacion' in cleanString(row[2]): seen['programador'] += 1
			if 'desarrollador' in cleanString(row[2]): seen['programador'] += 1
			if 'develo' in cleanString(row[2]): seen['programador'] += 1
			if 'motion graphics' in cleanString(row[2]): seen['motion graphics'] += 1
			if 'mobile' in cleanString(row[2]): seen['mobile'] += 1
			if 'ecommerce' in cleanString(row[2]): seen['ecommerce'] += 1
			if 'front' in cleanString(row[2]): seen['frontend'] += 1
			if 'industr' in cleanString(row[2]): seen['industrial'] += 1

			date = row[0].split('-')
			yyyymm = date[0]+date[1]
			
			if not last_date == yyyymm:
				last_date = yyyymm
				data = [yyyymm]
				for key in seen:
					data.append(seen[key])
				writer.writerow(data)
				seen = {
					'total':				0,
					'flash':				0,
					'motion graphics':		0,
					'grafico':				0,
					'web':					0,
					'data':					0,
					'director de arte': 	0,
					'programador':		 	0,
					'wordpress':		 	0,
					'maquetador':		 	0,
					'ux':				 	0,
					'ui':				 	0,
					'video':			 	0,
					'ios':				 	0,
					'android':			 	0,
					'game':				 	0,
					'mobile':			 	0,
					'ecommerce':			0,
					'frontend':				0,
					'industrial':			0,
				}
				print(yyyymm)

		print(seen)
