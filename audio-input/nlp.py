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
import threading

import get_lang_algo as GLA

analyser = SentimentIntensityAnalyzer()

# lanuageCodeRecieved = getCodeForLanguage(GLA.final_langs[0])   # change for all languages later


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
                    'zu': 'zulu', 
                    }


def getCodeForLanguage(inputLanguage):
    for languageCode, language in languageCodeDict.items():
         if language == inputLanguage:
             return languageCode
 
    return "Language not translable"

#translate
def takeCommandInLanguageIdentified(language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing")
        langaugeCode = getCodeForLanguage(language)
        print("langauage code recieved for the language is "+ str(langaugeCode))
        Query = r.recognize_google(audio, language=langaugeCode)
        print("the statement was='", Query, "'")
    except Exception as e:
        print(e)
        print("Repeat the statement")
        return "None"
    return Query



# # function returns 1,-1,0 for pos,neg,neutral sentiments
def sentimentAnalysisScores(sentence):
    # print("Sentence recieved by sentimenetAnalysisScore is "+str(sentence))
    sentence = str(sentence)
    SA_score = analyser.polarity_scores(sentence)
    compundScore = SA_score['compound'] 
    if compundScore >= 0.05:
        return 1
    elif compundScore > -0.05 and compundScore < 0.05:
        return 0
    else:
        return -1

emotion = ["neutral", "positive", "negative"]


anger_metric = 0

def realtime_sa():
    global convertedEnglishSentence
    translator = Translator()

    print(">>>>>>>>>> "+ str(GLA.final_langs[0]))

    recognized_sentence =  takeCommandInLanguageIdentified(GLA.final_langs[0])
    print("recognized sentences is "+ recognized_sentence)

    if(recognized_sentence.find('*')!=-1):
        print("emotion is negative")
        anger_metric = 1
    else:
        convertedEnglishSentence = translator.translate(recognized_sentence)
        print("Converted to English Sentence is --> "+str(convertedEnglishSentence))
        sentimentScore = sentimentAnalysisScores(convertedEnglishSentence)
        print("emotion is --> "+ emotion[sentimentScore])
        anger_metric = sentimentScore

        # if(emotion[sentimentScore]=="negative"):
        #     anger_metric = True 


def multithread_langs():
    threading.Thread(target=realtime_sa(GLA.final_langs[0])).start()
    threading.Thread(target=realtime_sa(GLA.final_langs[1])).start()
    threading.Thread(target=realtime_sa(GLA.final_langs[2])).start()




