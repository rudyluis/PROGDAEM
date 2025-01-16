##[4,5,9,3,6]
##[4,0,0,0,6]

import random
serie=[random.randint(0,100) for _ in range(random.randint(0,100))]
print(serie)
##nueva_serie2=[_ for _ in serie if _ %2 ==0]
##print(nueva_serie2)
nueva_serie=[_ if _ %2 ==0 else 0 for _ in serie ]
print(nueva_serie)