### factorial
### caso del for
n = int(input('Inotroduzca un valor: '))
fact=1
for i in range(1,n+1):
    fact*=i
    #factorial=factorial*i   cont+=1
print(f"{n}!={fact}")

##### factorial con while
fact=1
i=1
while(i<=n): 
    fact*=i   ## forma abreviado de multiplicador   fact=fact*i
    i+=1      ## forma abreviada del contrado       i=i+1
print(f"{n}!={fact}")  