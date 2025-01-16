##[3,6,9,1,10,15]
##[9,36,81,1,100,156]
##suma de elemento=451
import random

serie=[random.randint(0,100) for _ in range(random.randint(0,100))]
print(serie)

print('La suma de los valores de la lista es:',sum([_ **2 for _ in serie ]))



