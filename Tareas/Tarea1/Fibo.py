print("Se genero una función la cual suma de los elementos impares de la serie de fibonacci hasta el primer elemento superior a 100 000")

#Generamos la función que genera el elemento n de la serie de fibbonaci, con n>=2
def fibonnaci(n):
    x0=0
    x1=1
    for i in range(0,n-1):
        s=x0+x1
        x0=x1
        x1=s
    return s

#Generamos la función que suma de elementos impares de la serie de fibonnaci
def suma(n):
    if n==0:
        resultado=0
        x=0
    if n==1:
        resultado=1
        x=1
    if n>1:
        resultado=1
        x=2
        while resultado<=n:
            if fibonnaci(x)%2==1:
                resultado=resultado+fibonnaci(x)
                x=x+1
            else:
                x=x+1
    return resultado
print("el resultado es",suma(100000),".")

#FFMG#
