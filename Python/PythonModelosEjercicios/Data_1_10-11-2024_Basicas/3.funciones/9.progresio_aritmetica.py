#### n=7
##valor 2,3,4,7,6,11,8
##posi [1 2 3 4 5 6 7]
### impar (1)2,(3)4,(5)6,(7)8
#### par  (2)3,(4)7,(6)11
def prog_arimetica(n):
    impar=2
    par=3
    for i in range(1,n+1):
        if(i % 2==0):
            print(par, end=" - ")
            par+=4
        else:
            print(impar, end=" - ")
            impar+=2
## PRINCIPAL 
print('Progresion Aritmetica')
n= int(input('>>>>'))
prog_arimetica(n)
