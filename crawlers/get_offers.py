# -*- coding: UTF-8 -*-
import os, json, time, csv, re
from bs4 import BeautifulSoup 
from datetime import datetime
from urllib.request import Request, urlopen

# python -c "from get_offers import *; get_offers()"

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

def get_offers():
	pagenum = 0
	totalpages = 551
	debug = True
	filename = 'jobslinks2.csv'
	with open(filename, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',')

		while pagenum < totalpages:
			pagenum += 1
			try:
				if debug: print(time.strftime("%Y-%m-%d %H:%M:%S") + ' Abriendo url: https://www.domestika.org/es/jobs/date/forever?page='+str(pagenum))
				pagedata = parse_response_simple('https://www.domestika.org/es/jobs/date/forever?page='+str(pagenum))
				soup = BeautifulSoup(pagedata, "html.parser")

				for jobitem in soup.select('.jobs-list .job-item'):

					# Get data
					job = {}
					job['title'] = jobitem.select('.job-title')[0].get_text()
					job['url'] = jobitem.select('.job-title')[0]['href']
					job['_id'] = job['url'].split('/')[5].split('-')[0]
					date = jobitem.select('.job-item__date')[0].get_text().replace('\n', '').split('/')
					job['date'] = '20'+date[2]+'-'+date[1]+'-'+date[0]
						
					# Write data in csv
					try:
						data = [job['date'], job['_id'], job['title'], job['url']]
						writer.writerow(data)
					except:
						print(time.strftime("%Y-%m-%d %H:%M:%S") + ' codec cant\'t decode')

					# Debug
					if debug:
						try:
							print(time.strftime("%Y-%m-%d %H:%M:%S") + ' ' + job['title'])
						except:
							print(time.strftime("%Y-%m-%d %H:%M:%S") + ' codec cant\'t decode')


			except Exception as e:
				if debug: print(time.strftime("%Y-%m-%d %H:%M:%S") + ' Error general:\n', e)
				break