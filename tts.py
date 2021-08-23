from gtts import gTTS
from playsound import playsound

language = 'en'

# text = input("Enter your text :")
def tts(text):
    tts = gTTS(text,lang=language,slow=False)
    tts.save('/home/shakil/chatbot-alpha/Output/speech.wav')
    playsound('/home/shakil/chatbot-alpha/Output/speech.wav')

    return playsound

# tts('Hi there how can i help you')