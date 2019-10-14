#_*_coding:utf-8_*_
from  correiosws import correios
import json
#Cálculo do preço de transporte e do prazo

nCdServico="04014"
nCepOrigem="37750000"	
nCepDestino="37750000"	
sDtCalculo = ""
data = correios.calc_prazo_restricao(
	nCdServico=nCdServico,
        sCepOrigem=nCepOrigem,
        sCepDestino=nCepDestino,
	sDtCalculo=sDtCalculo
)
print(data)






