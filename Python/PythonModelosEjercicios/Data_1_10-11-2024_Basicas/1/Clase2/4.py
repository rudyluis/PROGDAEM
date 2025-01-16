segundos = int(input("Introduce una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
seg_restantes = segundos % 60
print(f"{segundos} segundos son equivalentes a {horas} horas, {minutos} minutos y {seg_restantes} segundos.")
