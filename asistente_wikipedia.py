import pyttsx3
import speech_recognition
import wikipedia 

engine = pyttsx3.init()
recognizer = speech_recognition.Recognizer()

def sintesis(text):
 engine.say(text)
 engine.runAndWait()

def reconocimiento():
    try:
        with speech_recognition.Microphone() as source:
            print("Escuchando... ")
            audio = recognizer.listen(source)
            mensaje = recognizer.recognize_google(audio,language="es")
            print(mensaje)
    except:
       pass
    return mensaje

def buscar_wikipedia():
    try:
        sintesis("Hola, soy tu asistente de wikipedia, di lo que estas buscando")
        mensaje = reconocimiento()
        busqueda = mensaje
        wikipedia.set_lang("es")
        respuesta = wikipedia.summary(busqueda, sentences = 1)
        sintesis(respuesta)
    except:
        sintesis("¡No se encontraron resultados para tu busqueda!")

buscar_wikipedia()