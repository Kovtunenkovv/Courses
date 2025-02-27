from gtts import gTTS #Google Text-to-Speech
import pygame
import os

def speak(text):
    if not text or text == ' ':
        print("Text is empty")
        return
    
    lang = 'ru'  #'en'

    tts = gTTS(text=text, lang=lang)
    audio_file = "output.mp3"
    tts.save(audio_file)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    os.remove(audio_file)

def main():
    while True:
        text = input("Enter the text or q for exit: ")
        if text.lower() in ['q', 'exit']:
            print("App is ending")
            break
        speak(text)

if __name__ == "__main__":
    main()
