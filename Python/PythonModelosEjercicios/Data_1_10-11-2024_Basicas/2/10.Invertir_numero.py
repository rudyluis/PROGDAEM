n= int(input('Introduzca un valor n  >>>>'))
cont=0
num=0
aux=n
while (n!=0):   #### n>0 (V)  n>=0    n!=0 (V) n==0
    dig=n%10
    num= num*10+dig
    n= n//10

if(aux==num):
    print('El numero es capicua')
else:
    print('El numero no es capicua')

 