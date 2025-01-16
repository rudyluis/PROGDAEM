saludo = "Hola"
nombre = "Ana"
mensaje = saludo + ", " + nombre + "!"
print(mensaje)


nombre = "María"
edad = 25
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje)
print(len(mensaje))
# Repetición de cadenas
linea = "-"
print(linea * 10)  # Imprime 10 guiones seguidos

texto = "Python"
print("Primer carácter:", texto[0])  # P
print("Último carácter:", texto[-1])  # n
print("Subcadena 'yth':", texto[1:4])  # yth
print("Subcadena 'yth':", texto[::-1])  # metodo de la cuchilla


frase = "   aprende Python   "
print("En mayúsculas:", frase.upper())  # APRENDE PYTHON
print("En minúsculas:", frase.lower())  # aprende python
print("Sin espacios extra:", frase.strip())  # "aprende Python"
print("Reemplazar palabras:", frase.replace("aprende", "enseña"))  # enseña Python


frase = "Python es divertido"
print("¿La frase empieza con 'Python'? :", frase.startswith("Python"))  # True
print("¿La frase contiene 'divertido'? :", "divertido" in frase)  # True

