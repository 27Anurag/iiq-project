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


import get_lang_algo as GLA
import nlp

#FLOW : get coords-->find state based on it --> get lang spoken around this state-->take input in these lang-->convert input to english-->sentiment anal

final_langs = GLA.adding_langs()
print("Langs working with --> ", final_langs)
nlp.realtime_sa()
