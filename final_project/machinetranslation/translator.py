""" This Module has two methods: 1. Translate from English to French
                                2. Translate from French to English"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """ Translate input (in English) to French """
    translation_response = language_translator.\
    translate(text=english_text,model_id='en-fr').get_result()
    french_text=translation_response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ Translate input (in French) to English """
    translation_response = language_translator.\
    translate(text=french_text,model_id='fr-en').get_result()
    english_text=translation_response['translations'][0]['translation']
    return english_text
