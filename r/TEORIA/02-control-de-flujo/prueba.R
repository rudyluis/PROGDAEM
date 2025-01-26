library(dplyr)
library(ggplot2)

# Resumir datos
resumen <- mtcars %>%
  group_by(cyl) %>%
  summarize(MediaHP = mean(hp), MediaMPG = mean(mpg))

print(resumen)

# Gráfico
ggplot(data = resumen, aes(x = factor(cyl), y = MediaHP)) +
  geom_bar(stat = "identity", fill = "coral") +
  theme_minimal() +
  labs(title = "Potencia Media por Número de Cilindros", x = "Cilindros", y = "Potencia Media (HP)")

x <- 10
y <- 5
suma <- x + y
print(suma)
