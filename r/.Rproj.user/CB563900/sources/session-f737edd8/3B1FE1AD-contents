# BUCLES
# Los bucles permiten ejecutar un bloque de código varias veces mientras se cumpla una condición.

# ---------------------
# BUCLE WHILE
# ---------------------
i <- 1 # Inicializamos la variable 'i' con el valor 1.
while(i <= 10){              # Mientras la condición 'i <= 10' sea verdadera:
  print(i)                   # Imprimimos el valor actual de 'i'.
  i <- i + 1                 # Incrementamos 'i' en 1 para avanzar al siguiente valor y evitar un bucle infinito.
}

# ---------------------
# BUCLE FOR
# ---------------------
# El bucle FOR itera sobre una secuencia de valores o elementos.
for(x in 1:10){              # Iteramos sobre los valores de 1 a 10 (incluidos).
  print(x)                   # Imprimimos el valor actual de 'x' en cada iteración.
}
# Este bucle hace lo mismo que el ejemplo del bucle WHILE anterior.
# "1:10" genera un rango de valores desde 1 hasta 10.

# ---------------------
# BREAK y NEXT
# ---------------------
# 'break': Termina la ejecución del bucle inmediatamente.
# 'next': Salta la iteración actual y pasa a la siguiente.

for(x in 1:10){              # Iteramos sobre los valores de 1 a 10.
  if(x == 3){                # Si el valor actual de 'x' es igual a 3:
    next                     # Saltamos esta iteración (no ejecuta print(x) para x = 3).
  }
  if(x == 6){                # Si el valor actual de 'x' es igual a 6:
    break                    # Finalizamos el bucle (no se ejecutan más iteraciones).
  }
  print(x)                   # Imprimimos el valor de 'x' si no se activan las condiciones anteriores.
}
# Salida esperada:
# Imprime: 1, 2, 4, 5
# Explicación:
# - Cuando 'x == 3', se ejecuta 'next' y no imprime 3.
# - Cuando 'x == 6', se ejecuta 'break' y el bucle se detiene.
