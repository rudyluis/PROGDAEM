x=0
n= int(input('Introduzca un valor de n'))
while x<n:
    #x=x+1
    x+=1
    print(x)

#%%
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue  # Salta cuando x es 5
    if x == 8:
        break  # Rompe el bucle cuando x es 8
    print(x)

#%%
for x in range(1,n+1):
    print(x)
#%%
for letra in "Python":
    print(letra)
#%%
# Imprimir números del 10 al 1 en decrementos de 2
for i in range(10, 0, -2):
    print(i)

for i in range(5):
    if i == 3:
        break  # Salir del bucle si i es 3
    print(i)
else:
    print("El bucle terminó sin interrupciones.")