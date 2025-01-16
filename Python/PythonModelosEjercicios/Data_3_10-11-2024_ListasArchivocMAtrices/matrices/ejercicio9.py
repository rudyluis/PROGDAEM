def cruz(n):
    matriz=[[0]*n for _ in range(n)]
    for i in range(n):
        if i==n//2:
            for j in range(n):
                matriz[i][j]=j+1
        else:
            matriz[i][n//2]=n+i+1
    return matriz

def matriz_cruz(n):
    matriz=[[0]*n for _ in range(n)]
    if(n%2==0):
        return
    cont=0
    for i in range(n):
        cont+=1
        matriz[i][n//2]=cont
    cont+=1
    for i in range(n):

        if(i==n//2):
            continue
        else:
            matriz[n//2][i]=cont
            cont+=1
    return matriz
n=int(input("Introduzca un valor para n: "))
matriz_r=cruz(n)
print("Version Valeria")
for fila in matriz_r:
    print(fila)


print("otra version")
matriz_r=matriz_cruz(n)

for fila in matriz_r:
    print(fila)
