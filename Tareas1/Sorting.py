debug = False #Cambien este valor a False para pedir los datos al usuario

#Arreglo de entrenamiento
text = "6,3,9,5,1,7,1"

if not debug:
    text = input("Ingrese una secuencia de valores naturales separados por coma: ")
    
    #Convertimos la cadena de caracteres en una lista
values = [int(i) for i in text.split(',')]

# Coloquen aquí su algoritmo de acomodo para acomodar la variable values
solucion=[]
solucion.append(values[0])
#Compararemos el numero de la lista values con el ya dado
for i in range(1,len(values)):
    #Para saber donde añadir el valor usaremos un contador
    n=0
    for j in range(0,len(solucion)):
        if values[i]>solucion[j]:
            n=n+1
    #Asi sabemos en que posición colocarlo        
    solucion.insert(n,values[i])
print("El conjunto ordenado es ")
print(solucion)    

#A veces sirve escribiendo con "_" al conjunto.

#FFMG#
