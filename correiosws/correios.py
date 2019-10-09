#-*- coding:utf-8 -*- 

import requests as req
import xmltodict

def calcDataMaxima(object_code):
	if(not isinstance(object_code, str)):
		object_code = str(object_code) 
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcDataMaxima?"
	reqUrl = endpoint + "codigoObjeto=" + object_code	


#Calcula somente o prazo dado o CEP de destino e o CEP de origem
def calcPrazo(origin_cep, destiny_cep, service_code):

	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrazo?"
	req_url = endpoint + "nCdServico=" + service_code + "&sCepOrigem=" + origin_cep  + "&sCepDestino=" + destiny_cep  
	data = req.get(req_url)
	if(data.status_code == 200):
		print(data.content)
	else:
		print("Error ocurred:"+ str(data.status_code))


#Calcula o prazo dado o CEP de destino e o CEP de origem, e também calcula o preço do frete, com a data atual
def calcPrecoPrazo(	nCdEmpresa="", 	
			sDsSenha="", 	
			nCdServico="", 	
			sCepOrigem="", 	
			sCepDestino="", 	
			nVlPeso="",          #Kg
			nCdFormato="", 	#1 - Formato caixa/pacote, 2 - Formato rolo/prisma, 3 - Envelope
			nVlComprimento="", 	# cm
			nVlAltura="", 		# cm obs: 0 for envelopes
			nVlLargura="",        # cm 
			nVlDiametro="", 	#cm
			sCdMaoPropria="", 	
			nVlValorDeclarado="", 	
			sCdAvisoRecebimento=""):
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo?" 
	req_url = endpoint + "nCdEmpresa=" + nCdEmpresa \
				+ "&sDsSenha=" + sDsSenha \
				+ "&nCdServico=" + nCdServico \
				+ "&sCepOrigem=" + sCepOrigem \
				+ "&sCepDestino=" + sCepDestino \
				+ "&nVlPeso=" + nVlPeso \
				+ "&nCdFormato="  + nCdFormato \
				+ "&nVlComprimento=" + nVlComprimento\
				+ "&nVlAltura=" + nVlAltura \
				+ "&nVlLargura=" + nVlLargura \
				+ "&nVlDiametro=" + nVlDiametro \
				+ "&sCdMaoPropria=" + sCdMaoPropria \
				+ "&nVlValorDeclarado=" + nVlValorDeclarado \
				+ "&sCdAvisoRecebimento=" + nVlValorDeclarado
	data = req.get(req_url)
	if(data.status_code==200):
		res = xmltodict.parse(data)
		print(res)
	else:
		print("Error: " + str(data.status_code))
#Calcula somente o prazo com uma data especificada  	..
def calcPrazoData(nCdServico, sCepOrigem, sCepDestino, sDtCalculo):
	endpoint = "https://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoData?"
	req_url = endpoint + "nCdServico=" + nCdServico \
			+ "sCepOrigem=" + sCepOrigem \
			+ "sCepDestino=" + sCepDestino \
			+ "sDtCalculo=" + sDtCalculo

	data = req.get(req_url)
	if(data.status_code=="200"):

		print(data.content)
	else:
		print("Error: " + str(data.status_code))
#Calcula o prazo considerando restrição de entrega 	
def calcPrazoRestricao(nCdServico, sCepOrigem, sCepDestino, sDtCalculo):
	endpoint = "https://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrazoRestricao?"
	req_url = endpoint + "nCdServico=" + nCdServico \
			+ "sCepOrigem=" + sCepOrigem \
			+ "sCepDestino=" + sCepDestino \
			+ "sDtCalculo=" + sDtCalculo

	data = req.get(req_url)
	if(data.status_code=="200"):

		print(data.content)
	else:
		print("Error: " + str(data.status_code))
#Calcula somente o preço com a data atual 
def calcPreco(	nCdEmpresa="", 	
			sDsSenha="", 	
			nCdServico="", 	
			sCepOrigem="", 	
			sCepDestino="", 	
			nVlPeso="",          #Kg
			nCdFormato="", 	#1 - Formato caixa/pacote, 2 - Formato rolo/prisma, 3 - Envelope
			nVlComprimento="", 	# cm
			nVlAltura="", 		# cm obs: 0 for envelopes
			nVlLargura="",        # cm 
			nVlDiametro="", 	#cm
			sCdMaoPropria="", 	
			nVlValorDeclarado="", 	
			sCdAvisoRecebimento=""):
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPreco?"
	req_url = endpoint + "nCdEmpresa=" + nCdEmpresa \
				+ "&sDsSenha=" + sDsSenha \
				+ "&nCdServico=" + nCdServico \
				+ "&sCepOrigem=" + sCepOrigem \
				+ "&sCepDestino=" + sCepDestino \
				+ "&nVlPeso=" + nVlPeso \
				+ "&nCdFormato="  + nCdFormato \
				+ "&nVlComprimento=" + nVlComprimento\
				+ "&nVlAltura=" + nVlAltura \
				+ "&nVlLargura=" + nVlLargura \
				+ "&nVlDiametro=" + nVlDiametro \
				+ "&sCdMaoPropria=" + sCdMaoPropria \
				+ "&nVlValorDeclarado=" + nVlValorDeclarado \
				+ "&sCdAvisoRecebimento=" + nVlValorDeclarado
	data = req.get(req_url)
	if(data.status_code==200):
		print(data.content)
	else:
		print("Error: " + str(data.status_code))
#Calcula somente o preço com uma data especificada 
def calcPrecoData(	nCdEmpresa="", 	
			sDsSenha="", 	
			nCdServico="", 	
			sCepOrigem="", 	
			sCepDestino="", 	
			nVlPeso="",          #Kg
			nCdFormato="", 	#1 - Formato caixa/pacote, 2 - Formato rolo/prisma, 3 - Envelope
			nVlComprimento="", 	# cm
			nVlAltura="", 		# cm obs: 0 for envelopes
			nVlLargura="",        # cm 
			nVlDiametro="", 	#cm
			sCdMaoPropria="", 	
			nVlValorDeclarado="", 	
			sCdAvisoRecebimento="",
		 	sDtCalculo=""):
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoData?" 
	req_url = endpoint      + "nCdEmpresa=" + nCdEmpresa \
				+ "&sDsSenha=" + sDsSenha \
				+ "&nCdServico=" + nCdServico \
				+ "&sCepOrigem=" + sCepOrigem \
				+ "&sCepDestino=" + sCepDestino \
				+ "&nVlPeso=" + nVlPeso \
				+ "&nCdFormato="  + nCdFormato \
				+ "&nVlComprimento=" + nVlComprimento\
				+ "&nVlAltura=" + nVlAltura \
				+ "&nVlLargura=" + nVlLargura \
				+ "&nVlDiametro=" + nVlDiametro \
				+ "&sCdMaoPropria=" + sCdMaoPropria \
				+ "&nVlValorDeclarado=" + nVlValorDeclarado \
				+ "&sCdAvisoRecebimento=" + nVlValorDeclarado \
				+ "&sDtCalculo=" + nVlValorDeclarado 
	data = req.get(req_url)
	if(data.status_code==200):
		print(data.content)
	else:
		print("Error: " + str(data.status_code))
		
		
#Calcula os preços dos serviços FAC 
def calcPrecoFac(	nCdServico="04510", 	 	
			nVlPeso="0.5", #kg
			strDataCalculo="" ):
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoData?" 
	req_url = endpoint      + "&nCdServico=" + nCdServico \
				+ "&nVlPeso=" + nVlPeso \
				+ "&strDataCalculo" 

	data = req.get(req_url)
	if(data.status_code==200):
		print(data.content)
	else:
		print("Error: " + str(data.status_code))



#Calcula o preço e o prazo com uma data especificada 
def calcPrecoPrazoData(	nCdEmpresa="", 	
			sDsSenha="", 	
			nCdServico="", 	
			sCepOrigem="", 	
			sCepDestino="", 	
			nVlPeso="",          #Kg
			nCdFormato="", 	#1 - Formato caixa/pacote, 2 - Formato rolo/prisma, 3 - Envelope
			nVlComprimento="", 	# cm
			nVlAltura="", 		# cm obs: 0 for envelopes
			nVlLargura="",        # cm 
			nVlDiametro="", 	#cm
			sCdMaoPropria="", 	
			nVlValorDeclarado="", 	
			sCdAvisoRecebimento=""):
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazoData?" 
	req_url = endpoint      + "nCdEmpresa=" + nCdEmpresa \
				+ "&sDsSenha=" + sDsSenha \
				+ "&nCdServico=" + nCdServico \
				+ "&sCepOrigem=" + sCepOrigem \
				+ "&sCepDestino=" + sCepDestino \
				+ "&nVlPeso=" + nVlPeso \
				+ "&nCdFormato="  + nCdFormato \
				+ "&nVlComprimento=" + nVlComprimento\
				+ "&nVlAltura=" + nVlAltura \
				+ "&nVlLargura=" + nVlLargura \
				+ "&nVlDiametro=" + nVlDiametro \
				+ "&sCdMaoPropria=" + sCdMaoPropria \
				+ "&nVlValorDeclarado=" + nVlValorDeclarado \
				+ "&sCdAvisoRecebimento=" + nVlValorDeclarado \
				+ "&sDtCalculo=" + nVlValorDeclarado
	data = req.get(req_url)
	if(data.status_code==200):
		print(data.content)
	else:
		print("Error: " + str(data.status_code))
#Calcula o preço e o prazo considerando as restrições de entrega 
def calcPrecoPrazoRestricao(	nCdEmpresa="", 	
			sDsSenha="", 	
			nCdServico="", 	
			sCepOrigem="", 	
			sCepDestino="", 	
			nVlPeso="",          #Kg
			nCdFormato="", 	#1 - Formato caixa/pacote, 2 - Formato rolo/prisma, 3 - Envelope
			nVlComprimento="", 	# cm
			nVlAltura="", 		# cm obs: 0 for envelopes
			nVlLargura="",        # cm 
			nVlDiametro="", 	#cm
			sCdMaoPropria="", 	
			nVlValorDeclarado="", 	
			sCdAvisoRecebimento=""):
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazoRestricao?" 
	req_url = endpoint      + "nCdEmpresa=" + nCdEmpresa \
				+ "&sDsSenha=" + sDsSenha \
				+ "&nCdServico=" + nCdServico \
				+ "&sCepOrigem=" + sCepOrigem \
				+ "&sCepDestino=" + sCepDestino \
				+ "&nVlPeso=" + nVlPeso \
				+ "&nCdFormato="  + nCdFormato \
				+ "&nVlComprimento=" + nVlComprimento\
				+ "&nVlAltura=" + nVlAltura \
				+ "&nVlLargura=" + nVlLargura \
				+ "&nVlDiametro=" + nVlDiametro \
				+ "&sCdMaoPropria=" + sCdMaoPropria \
				+ "&nVlValorDeclarado=" + nVlValorDeclarado \
				+ "&sCdAvisoRecebimento=" + nVlValorDeclarado \
				+ "&sDtCalculo=" + nVlValorDeclarado
	data = req.get(req_url)
	if(data.status_code==200):
		print(data.content)
	else:
		print("Error: " + str(data.status_code))



#Lista os serviços que estão disponíveis para cálculo de preço e/ou prazo 
def listaServicos():
		endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/ListaServicos?" 
		req_url = endpoint
		data = req.get(req_url)
		if(data.status_code == 200):
			print(data.content)
		else:	
			print("Error: " + str(data.status_code))

#Lista os serviços que são calculados pelo STAR 
def listaServicosSTAR():
		endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/ListaServicosSTAR?" 
		req_url = endpoint
		data = req.get(req_url)
		if(data.status_code == 200):
			print(data.content)
		else:
			
			print("Error: " + str(data.status_code))
#Método para mostrar se o trecho consultado utiliza modal aéreo ou terrestre 
def verificaModal(nCdServico="",
		sCepOrigem="", 
		sCepDestino=""):

		endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/VerificaModal?" 
		req_url = endpoint + "nCdServico=" + nCdServico + "&sCepOrigem=" + sCepOrigem + "&sCepDestino=" + sCepDestino
		data = req.get(req_url)
		if(data.status_code == 200):
			print(data.content)
		else:			
			print("Error: " + str(data.status_code))

#Retorna a versão atual do componente 
def getVersao():
		endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/getVersao?" 
		req_url = endpoint
		data = req.get(req_url)
		if(data.status_code == 200):
			print(data.content)
		else:
			
			print("Error: " + str(data.status_code))

	
