n=int(input("INTRODUZCA LA CANTIDAD DE NUMEROS "))
X=int(input("INTRODUZCA EL PRIMER VALOR "))
y=int(input("INTRODUZCA EL SEGUNDO VALOR "))
semilla=int(input("INTRODUZCA LA SEMILLA "))
valor=semilla
for i in range(1,n+1,1):
    if i%2==1:
        valor=valor*X
        print(valor, end=" ")
    else:
        valor=valor*y
        print(valor*(-1), end=" ")
