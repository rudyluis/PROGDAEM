minutos=int(input("Ingrese la cantidad de minutos que habló por llamada "))
hora=int(input("Ingrese el horario que empezó la llamada, solo la hora (0-24)"))
print ("Menú Opciones")
print("20-EEUU,costo 2$")
print("15-America Central,costo 2.2$")
print("18-America del Sur,costo 1.5$")
print("19-Europa,costo 3.5$")
print("23-Asia,costo 6$")
print("25-África,costo 6$")
print("29-Oceanía,costo 5$")
if(0<hora<6):
    descuento=0.6
else:
    descuento=1

codigo=input("Ingrese el código para su llamada-->")

match codigo:
    case '20':
        costo=2
    case '15':
        costo=2.2
    case '18':
        costo=1.5
    case '19':
        costo=3.5
    case '23':
        costo=6
    case '25':
        costo=6
    case '29':
        costo=5
costo_llamada=minutos*costo*descuento

if(descuento==1):
    print('El costo de su llamada en tarifa normal es: ',costo_llamada)
else:
    print('El costo de su llamada con descuento es: ',costo_llamada)



