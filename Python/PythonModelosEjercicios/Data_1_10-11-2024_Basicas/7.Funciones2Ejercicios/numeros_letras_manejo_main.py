# Listas de palabras para las unidades, decenas y centenas
unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
diez_a_veinte = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

def numero_a_letras(n):
    if n == 0:
        return "cero"
    elif n < 10:
        return unidades[n]
    elif n < 20:
        return diez_a_veinte[n - 10]
    elif n < 100:
        decena = n // 10
        unidad = n % 10
        return decenas[decena] + " " + unidades[unidad]
    elif n == 100:
        return "cien"
    elif n < 1000:
        centena = n // 100
        resto = n % 100
        if resto == 0:
            return centenas[centena]
        else:
            return centenas[centena] + " " + numero_a_letras(resto)

def main():
    n = int(input("Ingrese un número (1-1000): "))
    if 1 <= n <= 1000:
        resultado = numero_a_letras(n)
        print(f"{n} en palabras es: {resultado}")
    else:
        print("Número fuera de rango, ingrese un número entre 1 y 1000.")

if __name__ == "__main__":
    main()