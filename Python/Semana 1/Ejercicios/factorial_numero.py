## factorial
## caso del for
n = int(input('Introduzca un numero:'))
fact=1

## para n=1 con paso 1 hacer
#1 hasta <n
#for i in range(n)    0,1,2,3,4  n=5
#for   letras= {A,B,C,D}
# for i in letras     A,B,C,D
for i in range(1,n+1):
    ##fact=fact*i
    fact*=i
    print(i, end=" ")
print(f"{n}!= {fact}")
## forma del while
fact=1
i=1

while(i<=n):
    print(i, end="   ")
    fact*=i
    i+=1  ##i=i+1
print(f"{n}!= {fact}")