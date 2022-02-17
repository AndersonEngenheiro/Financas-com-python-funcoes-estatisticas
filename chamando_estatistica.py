from ast import Num
import fn_estatistica

numero = [1,2,5,4,3,7,8,6,4,9,8,5,6,4,1,23,54,87]

media = fn_estatistica.media(numero)
desvio = fn_estatistica.desvio(numero)

print('médias = ', media, ' desvio padrão = ', desvio)

