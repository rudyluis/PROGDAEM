import areas.operaciones2 

print('[A] = suma de 2 numeros')
print('[B] = Resta de 2 numeros')
print('[C] = Multiplicacion de 2 numeros')
print('[D] = Division de 2 numeroas')

a=int(input('valor A'))
b=int(input('valor B'))

opcion= input('Selecciones el valor ')
opcion=opcion.upper()
match opcion:
    case 'A':
        areas.operaciones2.suma(a,b)
    case 'B':
        areas.operaciones2.resta(a,b)
    case 'C':
        areas.operaciones2.multiplicacion(a,b)
    case 'D':
        areas.operaciones2.division(a,b)
    
    