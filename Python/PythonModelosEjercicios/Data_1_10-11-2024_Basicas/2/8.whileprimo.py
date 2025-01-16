n=int(input('Introduzca un numero >>>'))
cont=0
sw=0
while(cont<n):
    cont=cont+1
    if(n%cont==0):
        sw+=1
if(sw==2):
    print('El numero '+str(n)+" es primo")
else:
    print('El numero '+str(n)+" no es primo")