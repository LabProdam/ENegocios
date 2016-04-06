#Código de acesso ao WebService do E-Negócios

>Este código fornece funções para utilizar o WebService E-Negócios, 
>que foi fabricado e fornecido pelo LabProdam. 
	
##Funções fornecidas pelo código

###getSheet(file_name=None)
- file_name (str)

>Se for dado um nome ao arquivo a pesquisa será salva em um arquivo ".json",
>Retorna uma lista de dicionários que representam as linhas da tabela inteira

###searchText(text,file_name=None)
- text (str)
- file_name (str)

>Pesquisa um texto na coluna "Objeto",
>se for dado um nome ao arquivo a pesquisa será salva em um arquivo ".json",
>Retorna uma lista de dicionários que representam as linhas encontradas

###searchPeriod(min_date,max_date,file_name=None)
- min_date (str)
- max_date (str)
- file_name (str)

min_date e max_date precisam seguir o modelo "dd-mm-aaaa"

>Pesquisa um período (uma data mínima e uma data máxima) na coluna "Data de Abertura",
>se for dado um nome ao arquivo a pesquisa será salva em um arquivo ".json"
>Retorna uma lista de dicionários que representam as linhas encontradas

###searchTexts(texts,folder_name=None)
- texts (list[str])
- folder_name (str)

>Pesquisa uma lista de textos na coluna Objeto, 
>se for dado um nome à pasta, as pesquisas serão salvas separadamente dentro dessa pasta
>Retorna uma lista de dicionários que representam as linhas encontradas em todas as pesquisas

###searchPeriods(periods,folder_name=None)
- texts (list[ tuple(str,str) ]) or (list[ list[str,str] ])
- folder_name (str)

>Pesquisa uma lista de períodos (tuplas ou listas 
>de duas datas - a primeira sempre menor do que a segunda data), 
>se for dado um nome à pasta, as pesquisas serão salvas separadamente dentro dessa pasta
>Retorna uma lista de dicionários que representam as linhas encontradas em todas as pesquisas

	Se fornecer, em qualquer uma das funções à cima, file_name ou folder_name, 
	precisa ser no formato string válido para se nomear um arquivo ou pasta, respectivamente.

##Requerimentos

- Python 2.7 instalado
- Acesso à internet

##Desenvolvedor
	
LabProdam

##Licença

Este código está sob a licença MIT presente neste repositório.

