# Una lista es una colección ordenada de elementos. 
# A cada elemento de la lista le corresponde un índice, que se usa para referirnos a ellos.

cursos = ["python", "django", "flask", "c", "c++", "c#", "java", "php"]  
# Creamos una lista llamada 'cursos' que contiene cadenas de texto.

# Obtener el primer elemento 
curso = cursos[0]  # Usamos el índice 0 para acceder al primer elemento de la lista ("python").
print(curso)  # Imprimimos "python".

# Obtener el último elemento
curso = cursos[-1]  # Usamos el índice -1 para acceder al último elemento de la lista ("php").
print(curso)  # Imprimimos "php".

# Obtener los primeros 3 elementos
sub = cursos[0:3]  # Usamos slicing para tomar una sublista desde el índice 0 hasta el 3 (excluye el índice 3).
print(sub)  # Imprimimos ['python', 'django', 'flask'].

# Obtener todos los elementos a partir de un índice
sub = cursos[5:]  # Tomamos todos los elementos desde el índice 5 hasta el final.
print(sub)  # Imprimimos ['c#', 'java', 'php'].

# Obtener la lista tal cual
sub = cursos[:]  # Con slicing [:] obtenemos una copia exacta de la lista completa.
print(sub)  # Imprimimos ['python', 'django', 'flask', 'c', 'c++', 'c#', 'java', 'php'].

# Obtener la lista a partir de índices con saltos
sub = cursos[1:7:2]  
# Obtenemos una sublista que empieza en el índice 1 hasta el 7 (excluye el índice 7) con un salto de 2 elementos.
print(sub)  # Imprimimos ['django', 'c', 'c#'].

# Obtener el inverso de la lista
sub = cursos[::-1]  
# Usamos slicing con [::-1] para recorrer la lista desde el final hacia el inicio (invertirla).
print(sub)  
# Imprimimos ['php', 'java', 'c#', 'c++', 'c', 'flask', 'django', 'python'].
