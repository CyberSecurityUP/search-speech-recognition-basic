#Importando as bibliotecas de reconhecimento de voz, execução do browser (IE, GOOGLE, FIREFOX e etc..)
#Tradução e execução do som

import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound

print("CRIADO POR JOAS")
def cria_audio(audio): #Função de audio, tradução e execução
    tts = gTTS(audio,lang='pt-BR') #Ele define que o audio vai ser em Portugues
    tts.save('hello.mp3') #Salva em um arquivo.mp3
    print("Estou aprendendo o que você disse...")
    playsound('hello.mp3') #Executa o arquivo.mp3

sr.Microphone(device_index=1)

r = sr.Recognizer()

r.energy_threshold=5000
#Abro a detecção do som que entrar pelo microfone
with sr.Microphone() as source:
    print("Fale: ")
    audio = r.listen(source) #Vai armazenar o audio e esperar ser chamado
    try: #Ele experimenta
        text = r.recognize_google(audio,language='pt-BR') #Aonde vai entrar o audio e a lingua que ele vai entender
        print("Você disse: ".format(text))
        url='https://www.google.co.in/search?q='
        search_url=url+text #Ele ajunta a url e no final dela ele insere o audio que entra na variavel text
        webbrowser.open(search_url) #Abre o browser
    except: #Da uma excessão caso o experimento de errado
        print("Não reconheci")

cria_audio(text) #Executa a função ao qual Reproduz tudo que entrar na variavel text
