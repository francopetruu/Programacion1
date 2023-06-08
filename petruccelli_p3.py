#Franco Ivan Petruccelli DNI:37240131
cadena_no_es_salir = True

while(cadena_no_es_salir):
    cadena = input('Ingrese la cadena de caracteres: ')
    if(cadena == "salir"):
        print("Saliendo del programa")
        cadena_no_es_salir = False
    else:
        for c in cadena:
            print(c)

        print('La cantidad de letras es: ', len(cadena))
        
