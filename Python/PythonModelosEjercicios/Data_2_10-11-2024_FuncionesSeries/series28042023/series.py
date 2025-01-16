def es_primo(n):
    sw=0
    for i in range(1,n+1):
        if(n % i ==0):
            sw+=1
    if(sw==2):
        return 1
    else:
        return 0

n=int(input('n >>>>>>>'))
semilla=int(input('semilla >>>>>>>'))

cont=1
primo=0
s=0
s+=semilla

while primo<n:
    cont+=1
    sw= es_primo(cont)
    if(sw==1):
        ##print(str(s)+'+ ['+str(cont)+'] =',end=' ')
        print(s, end=' ')
        primo+=1
        s+= cont
 

