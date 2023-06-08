#Franco Ivan Petruccelli DNI:37240131
numero = int(input('Ingrese el número entero: '))
suma = 0

for i in range(2, numero + 1):
    if(i%2 == 0):
        print(i)
        suma += i

print('La suma de los numeros pares es: ', suma)
