
# PRE INSTALLS
# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
# pip install googletrans
# pip install geopy

# import geocoder
from geopy.geocoders import Nominatim
import reverse_geocoder as rg 
import pprint 
import math
from geopy.distance import geodesic
import speech_recognition as sr 
from googletrans import Translator
import geocoder
from math import radians, cos, sin, asin, sqrt

# cuss = open("sensetive.txt", "r")

coordinate_obj = geocoder.ipinfo('me')
my_coords = coordinate_obj.latlng	#current coord

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

def reverseGeocode(coordinates): 	# arg --> ((lat, lng), (lat, lng) ... )
	geolocator = Nominatim(user_agent="geoapiExercises")
	Latitude = str(coordinates[0])
	Longitude = str(coordinates[1])
	location = geolocator.reverse(Latitude+","+Longitude) 
	address = location.raw['address']
	# print(location)
	try :
		return address['state']
	except:
		return "none"
 




states = [	# (coord, [lang])	
	((11.1271, 78.6569),["Tamil","English","Hindi"]),
	((19.0760, 72.8777),["English","Hindi","Marathi"])
]


# { state : [languages] }

stateLanguagePair = {'Maharashtra':['Marathi','Hindi','English'],'Karanataka':['Kannada','English']}


deg=0
radius = 10
delta_theta = 6
allStatesFound = []
while(deg<360):
	returned = displace(radius,deg)
	foundLat = returned[0]   #in degrees
	foundLong = returned[1]   #in degrees
	stateFound = reverseGeocode((foundLat,foundLong))
	# print("State is " + stateFound)
	if stateFound not in allStatesFound:
		allStatesFound.append(stateFound)

	deg = deg + delta_theta # 360/delta_theta samples
	# --> allStatesFound =  ['Mah','Gujarat','Karantaka']
	
languagesInState = ["Hindi", "English"]
for state in allStatesFound:
	if state in stateLanguagePair:
		# stateLanguagePair = {'Maharashtra':['Marathi','Hindi','English'],'Karanataka':['Kannada','English']}
		for language in stateLanguagePair[state]:	
			if language!="English" and language!="Hindi":
				languagesInState.append(language)
				# languagesInState+=[language]
	else:
		pass
		# should be because of mismatch of naming convention of states in both places

# languageInState should contain all the languages spoken in states in the vicinity of the area
print(languagesInState)

# geolocator = Nominatim(user_agent="geoapiExercises")
# Latitude = "25.594095"
# Longitude = "85.137566"
  
# location = geolocator.reverse(Latitude+","+Longitude) 
# print(location)

# geodesic(kolkata, delhi).km





# Question - What if the driver is from some other state 
# and the state in which he is loading/unloading is some other state?
# 
# stateLanguagePair = {'Maharashtra':['Eng','Hin','Marathi','Gujrati']}



# TO DO
# Detect language based on location (GPS)
# TALK TO PRAKHAR ABOUT THE SPHERICAL LANGUAGE FINDING ALGORITHM


# translator = Translator()
# # print(googletrans.LANGUAGES)
# def takeCommandHindi(): 
		
# 	r = sr.Recognizer() 
# 	with sr.Microphone() as source: 
# 		print('Listening') 
# 		r.pause_threshold = 0.7
# 		audio = r.listen(source) 
# 		try: 
# 			print("Recognizing") 
# 			Query = r.recognize_google(audio, language='hi-In') 
# 			# print("the statement was='", Query, "'") 
# 		except Exception as e: 
# 			print(e) 
# 			print("Repeat the statement") 
# 			return "None"
# 		return Query 


# Query = takeCommandHindi()
# # print(Query)


# # THIS LINE GIVES SOME KIND OF ERROR
# t = translator.translate(Query)
# # print(t)
# flg=0
# for cusses in cuss:
# 	if(cusses == t):
# 		flg=1
# 		break

# print(("Contains profanity\n", "Does not contain profanity\n") [flg])



####$$$$$%%%%%%####$$$$$%%%%%%####$$$$$%%%%%%####$$$$$%%%%%%####$$$$$%%%%%%####$$$$$%%%%%%####$$$$$%%%%%%####$$$$$%%%%%%









