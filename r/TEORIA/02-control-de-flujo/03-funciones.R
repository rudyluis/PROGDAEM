

#### FUNCIONES DEFINIDAS POR EL USUARIO
# sintaxis de las funci?nes: nombreDeFunci?n <- function(argumentos){}
# 
# si no se le asigna ning?n nombre (o variable) a la funci?n, se dice que es
# una "funci?n an?nima"
# 
# para llamar a una funci?n con su nombre, se escribe directamente el nombre de
# esa funci?n seguido de par?ntesis en los que van introducidos los par?metros,
# es decir, los argumentos que necesita la funci?n

# definici?n de la funci?n
pow <- function(x, y){
  print(x ^ y) # la funci?n IMPRIME el valor, no lo devuelve
}
# llamadas a la funci?n:
pow(2, 3) # imprime el valor de 2^3, no devuelve nada
pow(6, 2) # imprime el valor de 6^5, no devuelve nada



# otro ejemplo:
# definir la funci?n: nombreDeFunci?n <- function(par?metros){}
sum <- function(x, y){
  return(x + y) # la funci?n DEVUELVE el valor, no lo imprime
}
# llamadas a la funci?n:
print(sum(1, 2)) # imprimir el valor devuelto por la funci?n (1+2 = 3)
resultado <- sum(3, 5) # ahora la variable "resultado" guarda el valor 8 (3+5)
print(resultado) # 8 -> como "resultado" es una variable, se puede usar



# ARGUMENTOS POR DEFECTO
# se puede asignar un valor por defecto a una variable
# 
# los argumentos por defecto son ?tiles cuando la funci?n trabaja con alg?n valor
# que no es obligatorio aportar
# 
# si no se aporta ning?n par?metro a la funci?n, ?sta utilizar? el valor por
# defecto, pero si se le pasa alg?n par?metro, lo utilizar?

saludar <- function(name="estudiante"){
  print(paste("Hola", name, sep=" "))
}
saludar() # imprime: "Hola estudiante"
saludar("June") # imprime: "Hola June"