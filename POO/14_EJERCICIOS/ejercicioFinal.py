from textblob import TextBlob
class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
    
    def analizar_sentimientos(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy Negativo", "31")

rangos = [
    ((-0.8, -0.3), Sentimiento("Negativo","31")),
    ((-0.3, -0.1), Sentimiento("Algo Negativo","31")),
    ((-0.1, 0.1), Sentimiento("Neutral","33")),
    ((0.1, 0.4), Sentimiento("Algo Positivo","32")),
    ((0.4, 0.9), Sentimiento("Positivo","32")),
    ((0.9, 1), Sentimiento("Muy Positivo","32"))
]

def obtencion_polaridad(texto):
    analisis = TextBlob(texto)
    return analisis.sentiment.polarity

while True:
    analizador = AnalizadorDeSentimientos(rangos)
    frase_analizada = input("\x1b[1;33m" + "Dime algo " + "\x1b[0;37m")
    sentimiento = analizador.analizar_sentimientos(obtencion_polaridad(frase_analizada))
    print(sentimiento)