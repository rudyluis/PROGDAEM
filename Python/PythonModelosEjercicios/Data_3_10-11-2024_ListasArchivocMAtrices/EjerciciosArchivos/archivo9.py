import openai
import speech_recognition as sr
import pyttsx3

#### librerias
###pip install openai
###pip install SpeechRecognition
###pip install pyaudio

#### link https://platform.openai.com/apps 
#### https://platform.openai.com/account/api-keys 

openai.api_key = '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'
def obtener_respuesta(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def transcribir_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='es')  # Utiliza el reconocimiento de voz de Google
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print("Error al conectar con el servicio de reconocimiento de voz: {0}".format(e))

    return ""

def leer_texto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

while True:
    
    texto_transcrito = transcribir_audio()
    ##texto_transcrito=input('>>>')
    if(texto_transcrito=='salir'):
        quit()
    ##print("Texto transcrito: ", texto_transcrito)
    ##respuesta = obtener_respuesta(texto_transcrito)

    print(texto_transcrito)
    leer_texto(texto_transcrito)
