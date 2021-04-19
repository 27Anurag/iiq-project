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



def compute(metric_1, metric_2):
	return ((0.645)*metric_1+(0.355)*metric_2)/2

# print(compute(ity.intensity_metric, nlp.anger_metric))
