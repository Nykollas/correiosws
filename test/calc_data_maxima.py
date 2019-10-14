#_*_coding:utf-8_*_
from  correiosws import correios
import json
objCode = ""
data = correios.calc_data_maxima(
        objCode
    )
print(data)






