def series_numero_prog(n):
     cont=1
     while (cont<=n):
          for i in range(1,cont+1,1):
               print(i, end='  ')
          for i in range(cont,0,-1):
               print(i, end='  ')
          cont+=1 
#1 1 1 2 2 1 1 2 3 3 2 1

series_numero_prog(3)

