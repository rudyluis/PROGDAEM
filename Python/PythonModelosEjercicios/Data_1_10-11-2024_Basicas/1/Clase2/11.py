nombre = "Ana"
saludo = "Hola"
mensaje = saludo + ", " + nombre + "!"
print(mensaje)

frase = "Python es divertido"
print("La longitud de la frase es:", len(frase))

palabra = "Python"
print("Primer carácter:", palabra[0])
print("Último carácter:", palabra[-1])


# Repetición de cadenas
linea = "-"
print(linea * 10)  # Imprime 10 guiones seguidos

texto = "Python"
print("Primer carácter:", texto[0])  # P
print("Último carácter:", texto[-1])  # n
print("Subcadena 'yth':", texto[1:4])  # yth
print("", texto[::-1])

frase = "   aprende Python   "
print("En mayúsculas:", frase.upper())  # APRENDE PYTHON
print("En minúsculas:", frase.lower())  # aprende python
print("Sin espacios extra:", frase.strip())  # "aprende Python"
print("Reemplazar palabras:", frase.replace("aprende", "enseña"))  # enseña Python

frase = "Python es divertido"
print("¿La frase empieza con 'Python'? :", frase.startswith("Python"))  # True
print("¿La frase contiene 'divertido'? :", "divertido" in frase)  # True


nombre = "María"
edad = 25
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)


frase = "Python es un lenguaje poderoso"
palabras = frase.split()  # Divide por espacios
print("Lista de palabras:", palabras)

texto = "Me encanta aprender Python. Python es genial."
print("Primera aparición de 'Python':", texto.find("Python"))  # Índice de la primera aparición
print("Veces que aparece 'Python':", texto.count("Python"))  # Total de veces que aparece
