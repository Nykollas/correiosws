import requests as req


def calcDataMaxima(object_code):
	if(!isinstance(object_code, str)):
		object_code = str(object_code) 
	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcDataMaxima?"
	reqUrl = endpoint + "codigoObjeto=" + object_code	

#Calcula somente o prazo dado os CEP de destino e o CEP de origem
def calcPrazo(origin_cep, destiny_cep, service_code):

	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrazo?"
	req_url = endpoint + "nCdServico=" + service_code + "&sCepOrigem=" + origin_cep  + "&sCepDestino=" + destiny_cep  
	data = req.get(req_url)
	if(data.status_code == 200):
		print(data.content)
	else:
		print("Error ocurred:"+ str(data.status_code))

#Calcula o prazo dado os CEP de destino e o CEP de origem, e também calcula o preço do frete
def calcPrecoPrazo(	nCdEmpresa="", 	
			sDsSenha="", 	
			nCdServico="04510", 	
			sCepOrigem="37750000", 	
			sCepDestino="04180112", 	
			nVlPeso="0.5",          #Kg
			nCdFormato="3", 	#1 - Formato caixa/pacote, 2 - Formato rolo/prisma, 3 - Envelope
			nVlComprimento="30", 	# cm
			nVlAltura="0", 		# cm obs: 0 for envelopes
			nVlLargura="30",        # cm 
			nVlDiametro="30", 	#cm
			sCdMaoPropria="N", 	
			nVlValorDeclarado="0", 	
			sCdAvisoRecebimento="N"):
 	endpoint = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo?" 
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
				+ "&sCdAvisoRecebimento=" + nVlValorDeclarado
	data = req.get(req_url)
	if(data.status_code==200):
		print(req_url)
		print(data.content)
	else:
		print(req_url)
		print("Error: " + str(data.status_code))



	
