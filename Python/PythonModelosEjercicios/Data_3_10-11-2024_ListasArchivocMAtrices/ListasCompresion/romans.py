def numeros_romanos(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb =["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    rom_num = ""
    i = 0
    while n>0:
        for _ in range(n//val[i]):
            rom_num+= syb[i]
            n -= val[i]
        i+= 1
    return rom_num
numero=int(input("elija un numero"))
num_romano=numeros_romanos(numero)
print(f"{numero} en numeros romanos es:{num_romano}")
