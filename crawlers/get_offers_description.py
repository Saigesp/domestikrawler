# -*- coding: UTF-8 -*-
import os, time, csv
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen

# python -c "from get_offers_description import *; get_offers_description()"

def parse_response_simple(url):
	try:
		time.sleep(0.5)
		web = Request(url)
		web.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
		web = urlopen(web).read()
		return web

	except Exception as e:
		print('Error parseando web:\n', e)
		return False

def get_offers_description():
	debug = True
	path_general = '/home/saigesp/git/domestikrawler'
	filename = '/data/jobslinks2.csv'
	with open(path_general + filename, 'rt') as read_csv:
		reader = csv.reader(read_csv, delimiter = ',')
		for row in reader:
			try:
				time.sleep(0.25)
				print(row[1])
				pagedata = parse_response_simple(row[3])
				soup = BeautifulSoup(pagedata, "html.parser")
				description = soup.select('.job-description')[0].get_text()
				f = open(path_general + '/data/descriptions/' + row[0] + '_' + row[1] + '.txt','w')
				f.write(description)
				f.close()
			except Exception as e:
				if debug: print(time.strftime("%Y-%m-%d %H:%M:%S") + ' Error general:\n', e)
				break