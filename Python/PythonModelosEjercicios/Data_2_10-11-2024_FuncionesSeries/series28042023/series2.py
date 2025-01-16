def serie(n):
    serien=[1]
    for i in range(3,n+2):
        s=str(serien[-1])+'$'
        cont=1
        numero=''
        for j in range(1, len(s)):
            if(s[j]!=s[j-1]):
                numero+=(str(cont)+s[j-1])
                cont=1
            else:
                cont+=1
        serien.append(int(numero))
    return serien

print(serie(8))

def serie2(n):
    serien='1'
    print('1', end=' ')
    for i in range(3,n+2):
        
        s=serien+'#'
       
        cont=1
        numero=''
        for j in range(1, len(s)):
            if(s[j]!=s[j-1]):
                numero+=(str(cont)+s[j-1])
                
                cont=1
            else:
                cont+=1
        ####serien.append(int(numero))
        ##serien=serien+str(numero)
        print(numero,end=' ' )
        serien=numero
    return serien

###print(serie2(4))
serie2(10)