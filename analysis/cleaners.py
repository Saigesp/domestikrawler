# -*- coding: UTF-8 -*-
import time, csv, re 
from datetime import datetime

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