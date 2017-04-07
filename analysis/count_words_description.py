# -*- coding: UTF-8 -*-
import time, csv, re, glob, os
from datetime import datetime
from cleaners import *
from bs4 import BeautifulSoup

# python -c "from count_words_description import *; count_words_description()"

def count_words_description():
	input_path = '/home/saigesp/git/domestikrawler/data/descriptions/'
	output_file = '/home/saigesp/git/domestikrawler/data/jobswords_description.csv'

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

	with open(output_file, 'w') as write_csv:
		writer = csv.writer(write_csv, delimiter=',',lineterminator='\n')
		last_date = ''
		data = ['yyyymm']
		seen = {}
		for key in sorted(words):
			data.append(key)
			seen[key] = 0
		writer.writerow(data)

		for file in sorted(glob.glob(os.path.join(input_path, '*.txt'))):
			with open(file, 'r') as txtfile:
				text=txtfile.read()
				for key in words:
					for word in words[key]:
						if word in cleanString(text): seen[key] += 1

				date = file.split('/')[7]
				date = date.split('_')[0]
				date = date.split('-')

				yyyymm = date[0]+date[1]
				
				# print(date)
				if not last_date == yyyymm:
					last_date = yyyymm
					data = [yyyymm]
					for key in sorted(seen):
						data.append(seen[key])
					print(data)
					writer.writerow(data)
					for key in words:
						seen[key] = 0
