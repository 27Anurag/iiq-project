# PRE INSTALLS
# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
# pip install googletrans
# pip install geopy
# import geocoder

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from geopy.geocoders import Nominatim
import reverse_geocoder as rg
import pprint
import math
from geopy.distance import geodesic
import speech_recognition as sr
from googletrans import Translator
import geocoder
from math import radians, cos, sin, asin, sqrt

from multiprocessing import Process
import threading
import get_lang_algo as GLA
import nlp
import intensity as ity
import time
import unimetric as uni
#FLOW : get coords-->find state based on it --> get lang spoken around this state-->take input in these lang-->convert input to english-->sentiment anal

final_score = False

def audio():
	nlp.realtime_sa()

def video():
	print("****** Video funtion called ******")

def intensity():
	ity.run()




if __name__ == '__main__':

	final_langs = GLA.adding_langs() #initialization
	print("Langs working with --> ", final_langs)

	threading.Thread(target=audio).start()	
	# threading.Thread(target=video).start()
	threading.Thread(target=intensity).start()

	# time.sleep(10)

	# print("Unimetric value --> ", uni.compute(ity.intensity_metric, nlp.anger_metric))


		
	


