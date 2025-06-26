# Ejercicio 2

def num_pares (a, b):  # definiendo numeros pares
    a = int(input('ingrese el primer valor: ')) # solicitando valores
    b = int(input('ingrese el segundo valor: '))
    if a > b:                                       # verificacion de numeros
        print (f'a debe ser menor que b')
        
    if a < 0 or b < 0:
        print ('los numeros no pueden ser negativos')
        
    lista_pares = []                              # creando la lista pares
    for i in range(a, b+1):
        if i % 2 == 0:                             #validadnde que sea par
            lista_pares.append(i)                   #agregando los valores pares a la lista
    return lista_pares
resultado = num_pares(1, 20)                        # obteniendo la funcion
cantidad = len(resultado)                           # obteniendo la cantidad de numeros    
print(f'los numeros pares en el rango son {resultado} y tiene en total {cantidad} numeros') #usando f strngs para presentar los resultados

                
