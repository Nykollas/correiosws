import requests as req
import xmltodict

def get_rastro(user, pass, obj):

	endpoint = "https://webservice.correios.com.br/service/rastro/Rastro.wsdl?"
	user =  ""
	senha = ""
	tipo="L"
	resultado="T"
	lingua = "101"
	objetos =  obj.join("")
        data = req.get(endpoint + "usuario=" + user \
				+ "&senha=" + senha \
				+ "&tipo=" + tipo \ 
				+ "&resultado=" + resultado \
				+ "&lingua=" + lingua \
				+ "&objetos=" + objetos)
	if(data.status_code == 200):
		res = xmltodict.parse(data.content)
		print(res)
	else:
		print("Error: " + data.status_code)



