binario= int(input('Introduzca un numero binario'))
conta=0
decimal=0
while(binario !=0):
    dig= binario % 10
    binario = binario//10
    decimal=decimal+dig*2**conta
    conta+=1
  ### conta= conta+1
print('El valor decimal es: '+str(decimal))
