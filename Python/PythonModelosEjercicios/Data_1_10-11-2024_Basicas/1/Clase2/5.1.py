# Solicitar datos al usuario
precio_original = float(input("Introduce el precio original del producto: $"))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))

# Calcular el monto del descuento
monto_descuento = (porcentaje_descuento / 100) * precio_original

# Calcular el precio final
precio_final = precio_original - monto_descuento

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Precio original: ${precio_original:.2f}")
print(f"Porcentaje de descuento: {porcentaje_descuento}%")
print(f"Monto de descuento: ${monto_descuento:.2f}")
print(f"Precio final con descuento: ${precio_final:.2f}")