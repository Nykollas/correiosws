#_*_coding:utf-8_*_
from  correiosws import correios
import json
nCdServico="04014"
nVlPeso="0.5"
nCdFormato="1"
sDtCalculo = ""
data = correios.calc_preco_fac(
        nCdServico=nCdServico,
	nVlPeso=nVlPeso,
	sDtCalculo=sDtCalculo
    )
print(data)






