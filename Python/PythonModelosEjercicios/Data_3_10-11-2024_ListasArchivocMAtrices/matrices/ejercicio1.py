lista=[4,5,6]
matriz=[[4,5,6],
        [1,2,3],
        [6,2,3]
        ]

print(matriz[0][2])

print(matriz)

Matriz2=[]
lista1=[4,7,8,9]
lista2=[3,5,2,3]
lista3=[2,6,7,9]

Matriz2.append(lista1)
Matriz2.append(lista2)
Matriz2.append(lista3)

print(Matriz2)


n=3   ##filas
m=4   ## columnas
matriz3=[]
for i in range(n):
    fila=[]
    for j in range(m):
        valor=int(input(f'Introduzca un valor para la fila {i},{j} : '))
        fila.append(valor)
    matriz3.append(fila)

print(matriz3)    

for fila in matriz3:
    print(fila)

