#Franco Ivan Petruccelli DNI:37240131
segundo_numero_no_es_cero = True

while(segundo_numero_no_es_cero):
    primer_numero = int(input('Ingrese el numero: '))
    segundo_numero = int(input('Es divisible por: '))
    if(segundo_numero != 0):
        if(primer_numero % segundo_numero == 0):
            print('Si')
        else:
            print('No')
    else:
        segundo_numero_no_es_cero = False
        print('No es posible dividir por 0')


