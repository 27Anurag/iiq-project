
# PRE INSTALLS
# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
# pip install googletrans

import speech_recognition as sr 
from googletrans import Translator

cuss = open("sensetive.txt", "r")

translator = Translator()
# print(googletrans.LANGUAGES)
def takeCommandHindi(): 
		
	r = sr.Recognizer() 
	with sr.Microphone() as source: 
		print('Listening') 
		r.pause_threshold = 0.7
		audio = r.listen(source) 
		try: 
			print("Recognizing") 
			Query = r.recognize_google(audio, language='hi-In') 
			print("the statement was='", Query, "'") 
		except Exception as e: 
			print(e) 
			print("Repeat the statement") 
			return "None"
		return Query 

Query = takeCommandHindi()

# print(Query)


# THIS LINE GIVES SOME KIND OF ERROR
t = translator.translate(Query)
# print(t)
flg=0
for cusses in cuss:
	if(cusses == t):
		flg=1
		break

print(("Contains profanity\n", "Does not contain profanity\n") [flg])





