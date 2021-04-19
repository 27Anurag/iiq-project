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



# --> GPS ke basis pe langauges --> un sab langauge pe translate --> sentiment 


languageCodeDict = {'af': 'afrikaans',
                    'sq': 'albanian',
                    'am': 'amharic',
                    'ar': 'arabic',
                    'hy': 'armenian',
                    'az': 'azerbaijani',
                    'eu': 'basque',
                    'be': 'belarusian',
                    'bn': 'bengali',
                    'bs': 'bosnian',
                    'bg': 'bulgarian',
                    'ca': 'catalan',
                    'ceb': 'cebuano',
                    'ny': 'chichewa',
                    'zh-cn': 'chinese (simplified)',
                    'zh-tw': 'chinese (traditional)',
                    'co': 'corsican',
                    'hr': 'croatian',
                    'cs': 'czech',
                    'da': 'danish',
                    'nl': 'dutch',
                    'en': 'english',
                    'eo': 'esperanto',
                    'et': 'estonian',
                    'tl': 'filipino',
                    'fi': 'finnish',
                    'fr': 'french',
                    'fy': 'frisian',
                    'gl': 'galician',
                    'ka': 'georgian',
                    'de': 'german',
                    'el': 'greek',
                    'gu': 'gujarati',
                    'ht': 'haitian creole',
                    'ha': 'hausa',
                    'haw': 'hawaiian',
                    'iw': 'hebrew',
                    'he': 'hebrew',
                    'hi': 'hindi',
                    'hmn': 'hmong',
                    'hu': 'hungarian',
                    'is': 'icelandic',
                    'ig': 'igbo',
                    'id': 'indonesian',
                    'ga': 'irish',
                    'it': 'italian',
                    'ja': 'japanese',
                    'jw': 'javanese',
                    'kn': 'kannada',
                    'kk': 'kazakh',
                    'km': 'khmer',
                    'ko': 'korean',
                    'ku': 'kurdish (kurmanji)',
                    'ky': 'kyrgyz',
                    'lo': 'lao',
                    'la': 'latin',
                    'lv': 'latvian',
                    'lt': 'lithuanian',
                    'lb': 'luxembourgish',
                    'mk': 'macedonian',
                    'mg': 'malagasy',
                    'ms': 'malay',
                    'ml': 'malayalam',
                    'mt': 'maltese',
                    'mi': 'maori',
                    'mr': 'marathi',
                    'mn': 'mongolian',
                    'my': 'myanmar (burmese)',
                    'ne': 'nepali',
                    'no': 'norwegian',
                    'or': 'odia',
                    'ps': 'pashto',
                    'fa': 'persian',
                    'pl': 'polish',
                    'pt': 'portuguese',
                    'pa': 'punjabi',
                    'ro': 'romanian',
                    'ru': 'russian',
                    'sm': 'samoan',
                    'gd': 'scots gaelic',
                    'sr': 'serbian',
                    'st': 'sesotho',
                    'sn': 'shona',
                    'sd': 'sindhi',
                    'si': 'sinhala',
                    'sk': 'slovak',
                    'sl': 'slovenian',
                    'so': 'somali',
                    'es': 'spanish',
                    'su': 'sundanese',
                    'sw': 'swahili',
                    'sv': 'swedish',
                    'tg': 'tajik',
                    'ta': 'tamil',
                    'te': 'telugu',
                    'th': 'thai',
                    'tr': 'turkish',
                    'uk': 'ukrainian',
                    'ur': 'urdu',
                    'ug': 'uyghur',
                    'uz': 'uzbek',
                    'vi': 'vietnamese',
                    'cy': 'welsh',
                    'xh': 'xhosa',
                    'yi': 'yiddish',
                    'yo': 'yoruba',
                    'zu': 'zulu', }

coordinate_obj = geocoder.ipinfo('me')
my_coords = coordinate_obj.latlng	#current coord

print("my coords --> ",my_coords)


def to_radians(theta):
	return theta * (math.pi/180)

#returns (lat, lon) at a dist r, at angle theta
def displace(r, theta):		# args --> (in km, in degrees)
	R = 6378.1 #Radius of the Earth in km
	brng = to_radians(theta) #Bearing is 90 degrees converted to radians.
	d = r #Distance in km

	#lat2  52.20444 - the lat result I'm hoping for
	#lon2  0.36056 - the long result I'm hoping for.

	lat1 = math.radians(my_coords[0]) #Current lat point converted to radians
	lon1 = math.radians(my_coords[1]) #Current long point converted to radians

	lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
		math.cos(lat1)*math.sin(d/R)*math.cos(brng))

	lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
				math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

	lat2 = math.degrees(lat2)
	lon2 = math.degrees(lon2)

	# print(lat2)
	# print(lon2)

	return (lat2, lon2)


# Coordinates tuple.Can contain more than one pair.
coordinates = (28.613939, 77.209023)
# reverseGeocode(coordinates)


#return indian state name based on coords
def reverseGeocode(coordinates): 	# arg --> ((lat, lng), (lat, lng) ... )
	geolocator = Nominatim(user_agent="geoapiExercises")
	Latitude = str(coordinates[0])
	Longitude = str(coordinates[1])
	location = geolocator.reverse(Latitude+","+Longitude)
	address = location.raw['address']
	# print(address['state'])
	try :
		return address['state']
	except:
		return "none"




stateLanguagePair = {'Jammu and Kashmir':['hindi'],
                    'Himachal Pradesh':['hindi'],
                    'Punjab':['punjabi'],
                    'Uttarakhand':['hindi','punjabi','nepali'],
                    'Haryana':['hindi','urdu'],
                    'Delhi':['hindi','punjabi','bengali','urdu'],
                    'Uttar Pradesh':['hindi','urdu'],
                    'Rajashtan':['hindi','punjabi','urdu'],
                    'Madhya Pradesh':['hindi'],
                    'Chhattisgarh':['hindi','bengali'],
                    'Bihar':['hindi'],
                    'Jharkhand':['hindi','bengali','urdu'],
                    'West Bengal':['bengali','hindi','urdu','nepali'],
                    'Sikkim':['nepali','hindi','bengali'],
                    'Assam':['hindi','bengali','nepali'],
                    'Arunachal Pradesh':['bengali','hindi','nepali'],
                    'Nagaland':['hindi','bengali','nepali'],
                    'Mizoram':['bengali','hindi','nepali'],
                    'Tripura':['bengali','hindi','nepali'],
                    'Meghalaya':['bengali','hindi','nepali'],
                    'Manipur':['bengali','nepali','hindi'],
                    'Odisha':['odia','hindi','telugu'],
                    'Maharashtra':['marathi','hindi','gujarati'],
                    'Gujarat':['gujarati','hindi','marathi','sindhi'],
                    'Daman and Diu':['gujarati','hindi','marathi'],
                    'Goa':['hindi','marathi','kannada'],
                    'Karantaka':['kannada','telugu','marathi','urdu'],
                    'Andra Pradesh':['telugu','hindi','tamil','urdu'],
                    'Kerala':['malayalam'],
                    'Tamil Nadu':['tamil','telugu','kannada','urdu'],
                    'Puducherry':['tamil','telugu','kannada','urdu'],

                    }

def state_finder():
    temp_circum_states = []

    deg=0
    radius = 10
    delta_theta = 30
    while(deg<360):
    	returned = displace(radius,deg)
    	foundLat = returned[0]   #in degrees
    	foundLong = returned[1]   #in degrees
    	stateFound = reverseGeocode((foundLat,foundLong))
    	# print("State is " + stateFound)
    	if stateFound not in temp_circum_states:
    		temp_circum_states.append(stateFound)

    	deg = deg + delta_theta # 360/delta_theta samples
    	# --> temp_circum_states =  ['Mah','Gujarat','Karantaka']
    return temp_circum_states




def adding_langs():
    temp_langs = []
    print("Please wait, scanning area to find commonly spoken languages ")

    circum_states = state_finder()
    #adding new langs to temp_langs
    for state in circum_states:
    	if state in stateLanguagePair:
    		# stateLanguagePair = {'Maharashtra':['Marathi','Hindi','English'],'Karanataka':['Kannada','English']}
    		for language in stateLanguagePair[state]:
    			temp_langs.append(language)
    				# temp_langs+=[language]

    	else:
    		pass
    		# should be because of mismatch of naming convention of states in both places
    # print(temp_langs)
    return temp_langs

final_langs = adding_langs()






