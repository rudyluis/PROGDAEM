a= int(input('Inserte el valor de a'))
b= int(input('Inserte el valor de b'))
if(a>b):
    print('El numero mayor es '+str(a))
else:
    print(f'El numero mayor es {b}')

## a=5  (asignacion)
## a==b  (comparacion)
## a===b  (comparacion exacta)

## 5=='5' Verdadero
## 5==='5' Falso

a = 5
b = '5'

# Comparación de valor
print(a == int(b))  # Verdadero, si b se convierte a entero

# Comparación de tipo
print(type(a) == type(b))  # Falso, porque `a` es int y `b` es str

# Comparación estricta (tipo y valor)
print(a == b and type(a) == type(b))  # Falso



if(a==b):
    print(f'Los numeros {a} y {b} son iguales')    