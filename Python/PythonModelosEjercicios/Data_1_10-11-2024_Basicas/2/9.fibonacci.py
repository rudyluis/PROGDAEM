n=int(input("INTRODUZCA UN NUMERO "))
a=0
b=1
cont=0
while cont<n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    cont += 1