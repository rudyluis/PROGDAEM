###  1 22 333 4444 55555

def serie_ene(n):
    
    for i in range ( 1, n+1):
        ser=''
        for j in range(1,i+1,1):
            ser=ser+str(i)
        print(ser, end=' ')

serie_ene(4)