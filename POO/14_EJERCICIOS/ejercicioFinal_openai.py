import openai

openai.api_key = ""
system_rol = '''Haz de cuenta que eres un analizador de sentimientos.
                Yo te paso sentimientos y analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres
                SOLO RESPUESTAS NUMERICAS. Donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
                Puedes ir entre esos rangos, es decir 0.3, -0.5, etc también son válidos.
                (Puedes responder solo con ints o floats)'''

mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimientos(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad <= -0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[0;37m"
        elif polaridad > -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polaridad > 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo Positivo" + "\x1b[0;37m"
        elif polaridad > 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy Positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Muy Negativo" + "\x1b[0;37m"
        
analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "Dime algo" + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )

    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimientos(float(respuesta))
    print(sentimiento)