# -*- coding: utf-8 -*-
'''
Este código fornece funções para utilizar o WebService E-Negócios, que foi fabricado e fornecido pelo LabProdam. 
	getSheet(file_name=None)
		file_name precisa ser no formato string válido para se nomear um arquivo
	searchText(text,file_name=None)
		text precisa ser no formato string
	searchPeriod(min_date,max_date,file_name=None)
		min_date e max_date precisam ser no formato string, segundo o modelo "dd-mm-aaaa"
	searchTexts(texts,folder_name=None)
		texts precisa ser uma lista de strings a serem pesquisadas
	searchPeriods(periods,folder_name=None)

Se fornecer, em qualquer uma das funções à cima, file_name ou folder_name, 
precisa ser no formato string válido para se nomear um arquivo ou pasta, respectivamente
'''
import urllib
import urllib2
import json
import os

#Constante com o endereço para acessar o WebService
URL_WEBSERVICE="https://script.google.com/macros/s/AKfycbz6iMd5GZDy6ppzuQLKXFlzMEpozuns2PcGCIR0xEo2BKQXejxZ/exec"

def callWebService(app,data=None):
	'''
	Define os parametros passados, acessa o webservice, 
	lê a resposta do acesso, fecha a conexão com o webservice 
	e retorna a resposta lida em string
	'''
	global URL_WEBSERVICE
	
	request_parameter={'app': app}
	if data!=None :
		request_parameter['data'] = data
	
	conn=urllib2.urlopen(
		URL_WEBSERVICE,
		data=urllib.urlencode(request_parameter)
	)
	retrieved_data=conn.read()
	conn.close()
	return retrieved_data	

def saveFile(file_name,data):
	'''
	Tenta abrir o arquivo com o nome dado + extensão '.json' para gravar
	Sobrescreve o arquivo com data
	Fecha o arquivo
	Do contrário ele apenas fecha o arquivo
	Retorna True se o arquivo foi salvo
	'''
	file_saved=False
	try:
		arq=open(file_name+'.json','wb')
		arq.write(data)
		arq.close()
		file_saved=True
	except Exception,e:
		print e
		arq.close()
	return file_saved

def saveAndReturnJson(file_name,data):
	'''
	Verifica se o nome do arquivo é válido e salva data ainda em formato de texto nele,
	Transforma data em código disponibilizando-o para uso no programa
	Retorna data transformada
	'''
	if file_name!=None:
		saveFile(file_name,data)
	return json.loads(data)

def getSheet(file_name=None):
	'''
	Se for dado um nome ao arquivo a pesquisa será salva em um arquivo ".json",
	Retorna uma lista de dicionários que representam as linhas da tabela inteira
	'''
	retrieved_data=callWebService("get")
	return saveAndReturnJson(file_name,retrieved_data)

def searchText(text,file_name=None):
	'''
	Pesquisa um texto na coluna "Objeto",
	se for dado um nome ao arquivo a pesquisa será salva em um arquivo ".json",
	Retorna uma lista de dicionários que representam as linhas encontradas
	'''
	retrieved_data=callWebService("search text",text)
	return saveAndReturnJson(file_name,retrieved_data)

def searchPeriod(min_date,max_date,file_name=None):
	'''
	Pesquisa um período (uma data mínima e uma data máxima) na coluna "Data de Abertura",
	se for dado um nome ao arquivo a pesquisa será salva em um arquivo ".json"
	Retorna uma lista de dicionários que representam as linhas encontradas
	'''
	retrieved_data=callWebService("search date",json.dumps([min_date,max_date]))
	return saveAndReturnJson(file_name,retrieved_data)

def createFolderIfDoestExists(folder_name):
	'''
	Verifica se o nome da pasta é válido, se a pasta não existe e então cria a pasta
	'''
	if folder_name!=None:
		if not os.path.exists(folder_name):
			os.mkdir(folder_name)

def searchTexts(texts,folder_name=None):
	'''
	Pesquisa uma lista de textos na coluna Objeto, 
	se for dado um nome à pasta, as pesquisas serão salvas separadamente dentro dessa pasta
	Retorna uma lista de dicionários que representam as linhas encontradas em todas as pesquisas
	'''
	retrieved_data=[]
	createFolderIfDoestExists(folder_name)
	for text in texts:
		retrieved_data+=searchText(text,None if folder_name==None else folder_name+str(os.sep)+text)
	return retrieved_data


def normalizePeriod(period):
	'''
	Garante que o período seja uma lista e não uma tupla
	Transforma os separadores das datas dos períodos em "-" evitando erros ao salvar a pesquisa	
	'''
	#---Explicação:---#
	'''
		Se os períodos forem fornecidos como tuplas e não listas, eles não podem ser modificados,
		E se as datas apresentam caracteres ruins para nomes de arquivos como / ou \ ocorrerá erro ao tentar salvar a pesquisa.
		Para poder modificar uma única posição numa string é necessário transformá-la numa lista
		A ''.join(data) junta todas as posições da lista que antes era string a uma string vazia
	'''
	period=list(period)
	period[0]=list(period[0])
	period[1]=list(period[1])
	period[0][2]='-'
	period[0][5]='-'
	period[1][2]='-'
	period[1][5]='-'
	period[0]=''.join(period[0])
	period[1]=''.join(period[1])

def searchPeriods(periods,folder_name=None):
	'''
	Pesquisa uma lista de períodos(tuplas ou listas de duas datas - a primeira sempre menor do que a segunda data), 
	se for dado um nome à pasta, as pesquisas serão salvas separadamente dentro dessa pasta
	Retorna uma lista de dicionários que representam as linhas encontradas em todas as pesquisas
	'''
	retrieved_data=[]
	createFolderIfDoestExists(folder_name)
	for period in periods:
		normalizePeriod(period)
		retrieved_data+=searchPeriod(period[0],period[1],None if folder_name==None else folder_name+str(os.sep)+period[0]+' to '+period[1])
	return retrieved_data
