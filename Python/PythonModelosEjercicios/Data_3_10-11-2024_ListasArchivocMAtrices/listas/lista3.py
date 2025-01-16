
##### Fibonacci
fibo=[0,1]
for a in range (2,5):
    fibo.append(fibo[a-1]+fibo[a-2]) 
print(fibo)

###### 

def fibonacci(n):
    fibo=[0,1]
    for a in range (2,n+1):
        fibo.append(fibo[a-1]+fibo[a-2])
    return fibo

if __name__=="__main__":
    Serie_fibonacci=fibonacci(int(input('Introduzca un numero')))
    print(Serie_fibonacci)