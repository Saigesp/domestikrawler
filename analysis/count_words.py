# -*- coding: UTF-8 -*-
import time, csv, re 
from datetime import datetime
from cleaners import *

# python -c "from count_words import *; count_words()"

def count_words():
	input_file = '/home/saigesp/git/domestikrawler/data/jobslinks2.csv'
	output_file = '/home/saigesp/git/domestikrawler/data/jobswords.csv'

	words = {
		'program':		['programa', 'desarroll', 'softw', 'develo', 'ecommerce', 'front'],
		'web':			['web', 'programa', 'desarroll', 'develo', 'ecommerce', 'front', 'ux', 'ui'],
		'frameworks':	['wordpress', 'magento', 'prestashop', 'drupal', 'joomla'],
		'lenguage':		['html', 'css', 'java', 'php', 'flash'],
		'mobile':		['app', 'ios', 'android', 'mobile'],
		'data':			['datos', 'data', 'visualizac'],
		'director':		['director', 'direcc', 'arte', 'art director', 'arti'],
		'software':		['photoshop', 'illustrator', 'indesign'],
		'design':		['graphi', 'grafi', 'tipogr', 'industr', 'maqueta', 'fotogr', 'motion', '3d', 'edic', 'packa', 'multim'],
		'publi':		['copy', 'ejecutiv']
	}

	with open(input_file, 'rt') as read_csv, open(output_file, 'w') as write_csv:
		writer = csv.writer(write_csv, delimiter=',',lineterminator='\n')
		reader = csv.reader(read_csv, delimiter = ',')
		last_date = '201704'
		data = ['yyyymm']
		seen = {}
		for key in sorted(words):
			data.append(key)
			seen[key] = 0
		writer.writerow(data)
		for row in reader:
			for key in words:
				for word in words[key]:
					if word in cleanString(row[2]): seen[key] += 1

			date = row[0].split('-')
			date[1] = str(int(date[1]) + 1)

			if int(date[1]) < 10:
				date[1] = '0'+date[1]

			if int(date[1]) == 13:
				date[1] = '01'
				date[0] = str(int(date[0])+1)

			yyyymm = date[0]+date[1]
			
			print(row[0],cleanString(row[2]))
			if not last_date == yyyymm:
				last_date = yyyymm
				data = [yyyymm]
				for key in sorted(seen):
					data.append(seen[key])
				writer.writerow(data)
				for key in words:
					seen[key] = 0
