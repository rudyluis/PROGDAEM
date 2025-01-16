def factorial_inverso(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
    while fact<0:
        fact=int(fact)
        print(fact, end=' ' )
        fact /=n
        n=n-1
factorial_inverso(4)