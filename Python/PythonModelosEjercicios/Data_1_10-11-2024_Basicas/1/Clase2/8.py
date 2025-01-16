contraseña_correcta = "python123"
while True:
    contraseña = input("Introduce la contraseña: ")
    if contraseña == contraseña_correcta:
        print("Contraseña correcta. ¡Bienvenido!")
        break
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")