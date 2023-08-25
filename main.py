import pyttsx3

text_speech = pyttsx3.init()

while True:
    user_text = input("Welcome to the RoboSpeech. Please Type the text you want to want me to speak: ")
    text_speech.say(user_text)
    text_speech.runAndWait()

    if user_text == 'q'.casefold():
        text_speech.say("Thank you for using RoboSpeech")
        text_speech.runAndWait()
        break


