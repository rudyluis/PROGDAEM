import random
serie=[random.randint(0,100) for _ in range(random.randint(0,100))]
##nueva_lista=[expresion for elemento in iterable if (condicion)]
print(serie)
pares=[_ for _ in serie if _ %2==0]
pares=[x for x in serie if x %2==0]

    
        

print(pares)