#!/usr/bin/python

import sys
#Esta funcao transforma um numero em sua forma de texto
def numberToBaseString(number,base):
    output = ''                             #limpa a saida
    if number < base:
        output = number                     #se o numero eh menor que a base retorna o numero
    else:
        rem = number % base                 #caso contrario retira a menor parte utilizando o modulo
        output = str(rem)                   #guardo o resultado do resto na string
        rn = (number - rem) / base          #retiro do numero o resto e divido pela base
        rs = numberToBaseString(rn,base)    #chamo novamente a funcao
        output = str(rs)+output             #vou concatenando na frente a string para retornar o numero na nova base
    return output


#main program

number = int(sys.argv[1])
base = int(sys.argv[2])


output = numberToBaseString(number,base)

print 'Numero:' ,number, 'na base',base, 'eh: ',output
