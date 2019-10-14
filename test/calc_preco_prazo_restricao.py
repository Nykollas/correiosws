#_*_coding:utf-8_*_
from  correiosws import correios
import json
nCdEmpresa=""
sDsSenha=""
nCdServico="04014"
nCepOrigem="37750000"	
nCepDestino="37750000"	
nVlPeso="0.5"
nCdFormato="1"
nVlComprimento="15"
nVlAltura="15"
nVlLargura="15"
nVlDiametro="15"
sCdMaoPropria="N"
nVlValorDeclarado=str(0)
sCdAvisoRecebimento="N"
data = correios.calc_preco_prazo_restricao(
        nCdEmpresa=nCdEmpresa,
        sDsSenha=sDsSenha,
        nCdServico=nCdServico,
        sCepOrigem=nCepOrigem,
        sCepDestino=nCepDestino,
        nVlPeso=nVlPeso,
	nCdFormato=nCdFormato,
        nVlComprimento=nVlComprimento,
        nVlAltura=nVlAltura,
        nVlLargura=nVlLargura,
        nVlDiametro=nVlDiametro,
        sCdMaoPropria=sCdMaoPropria,
        nVlValorDeclarado=nVlValorDeclarado,
        sCdAvisoRecebimento=sCdAvisoRecebimento,
    )
print(data)






