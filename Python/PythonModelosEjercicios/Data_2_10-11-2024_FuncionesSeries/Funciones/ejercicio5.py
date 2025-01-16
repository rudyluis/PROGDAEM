import funciones
for n in range(1,11):
    sumDivisor=0
    for x in range(1,n+1):
        if(n%x==0):
            print (x, end='-')
            sumDivisor+=x
    print("para "+str(n)+" total = ", sumDivisor)
