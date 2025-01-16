palabra=input('Introduzca la palabra: ')
inversa=palabra
palabra=list(palabra)
inversa=list(inversa)
inversa.reverse()
print(palabra)
print(inversa)
if(palabra==inversa):
    print('Es palindroma')
else:
    print('No es Palindroma')
