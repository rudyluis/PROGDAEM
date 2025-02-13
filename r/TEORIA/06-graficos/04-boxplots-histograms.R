# DIAGRAMAS DE CAJAS E HISTOGRAMAS

# diagramas de cajas -> boxplot()
# 
# estos diagramas muestran c?mo est?n distribuidos los datos
# 
# muestran de forma visual los siguientes valores:
#   - valor m?nimo
#   - valor m?ximo
#   - mediana
#   - Q1
#   - Q2 (mediana)
#   - Q3
boxplot(mtcars$mpg)

# esos mismos valores pueden ser obtenidos usando comandos como summary()
summary(mtcars$mpg)

# sin embargo, podemos usar tambi?n el comando boxplot.stats() para obtener
# valores at?picos si los hubiera
boxplot.stats(mtcars$mpg)



# histogramas -> histogram()
# 
# representan las frecuencias de los valores agrupadas en rangos
# 
# son similares a los gr?ficos de barras, pero los histogramas agrupan los
# datos en rangos de forma continua
# 
# esos rangos son calculados autom?ticamente
print(mtcars)
hist(mtcars$hp)
barplot(mtcars$hp) # para ver la diferencia




