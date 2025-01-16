def series_suma_resta(n, semilla=1, inicio=1):
    s=semilla
    sw=1
    data=semilla
    #ser=(inicio+data)*sw
    for a in range(1,n+1,1):
        ser=inicio+data
        print(str(ser)+'-->'+str(data), end='  ')
        s=s+semilla
        if(a%2==0):
            sw*=-1
        data=s*sw
       

series_suma_resta(10,2,43)

