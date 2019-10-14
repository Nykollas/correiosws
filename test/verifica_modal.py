from correiosws import correios

nCdServico=""
sCepOrigem=""
sCepDestino=""
data = correios.lista_servicos(nCdServico, sCepOrigem, sCepDestino)

print(data)

