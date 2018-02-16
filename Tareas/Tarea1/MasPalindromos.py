def rot(A,j):
#A=2639
#j=0
    numeracion=[]
    for i in range(0,len(str(A))):
#Tomamos la componente de la posición i que va de 0 a len(str(A)), le sumamos 1 para que se encuentre en base 10
        B=(i+1)+int(str(A)[j])
#Luego le sumamos el número j que queremos recorrer
#Obtenemos el  cociente de ese numero que será el multiplo menor del intervalo. Esto nos dará un numero entre 1 a len(str(A))
        C=B//len(str(A))
#Luego regresamos al espacio 0 a len(str(A))
        ax=abs(B-C*len(str(A)))-1
#Obtenemos un caso especial con el -1
        if ax==-1:
            ax=len(str(A))-1
        numeracion.append(ax)
    
    contador=0
    resultado=""
    while contador<(len(str(A))):
        for i in range(0,len(str(A))):
        #Asi verificaremos cada número y su respectivo valor en la cuenta
            if contador==numeracion[i]:
            #"Por ultimo sumamos la cadena de texto para dar el resutado final"
                resultado=resultado+str(A)[i]
        contador=contador+1
    return int(resultado)
#Me causo un error una vez y el ejemplo invertía el orden, hay que tener cuidado.

def r(A):
#Factores de prueba
#A=2639
    Suma=A
    for k in range(0,len(str(A))):
        Suma=Suma+rot(A,k)*(-1)**k
    return abs(Suma)

def comparador(a,b):
    list=[]
    for i in range(a,b):
        #Comparación en todo el intervalo
        #Si es palindromo:
        if str(r(i))==str(r(i))[::-1]:
            list.append(i)
            #Guarda el turbopalindromo i
    return list

a=1
b=200000+1
print("la cantidad de turbopalíndromos entre 1 y 200 000 es:")
print(len(comparador(a,b)))

#El resultado me dio: 1224 turbopalíndromos

#FFMG##
