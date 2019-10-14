#_*_coding:utf-8_*_
from  correiosws import correios
import json
nCdServico="04014"
nCepOrigem="37750000"	
nCepDestino="37750000"	
data = correios.calc_prazo(
	nCdServico=nCdServico,
        sCepOrigem=nCepOrigem,
        sCepDestino=nCepDestino
)
print(data)






