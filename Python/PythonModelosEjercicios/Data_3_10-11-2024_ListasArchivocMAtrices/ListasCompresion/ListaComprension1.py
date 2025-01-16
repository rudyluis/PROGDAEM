##3 nueva_lista=[expresion for elemento in iterable if (condicion)]

import random
[1,2,3,4,5]
l=[]
n=5
## clasico
for _ in range(n):
    l.append(_)
print(l)
##por comprension
l=[_ for _ in range(n)]
l=[i for i in range(n)]
print(l)
### numeros randomicos


serie=[random.randint(0,100) for _ in range(random.randint(0,100))]

print(serie)

cuadrados =[x**2 for x in range(1,random.randint(0,100))]
print(cuadrados)

