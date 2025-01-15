import funcionmayor3numeros


######################################
###APLICACION PRINCIPAL
a= int(input("Ingrese el valor de a>>>"))
b= int(input("Ingrese el valor de b>>>"))
c= int(input("Ingrese el valor de c>>>"))
#### una funcion puede devolver un valor de retorno
## el valro de retorno es mayor

#mayor= encontrar_mayor3numeros(a,b,c)
mayor= funcionmayor3numeros.encontrar_mayor3numeros(a,b,c)
print(f'El mayor de los 3 numero {a},{b},{c} es: {mayor}')