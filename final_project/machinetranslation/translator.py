import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= version,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    #write the code here
    if english_text is None:
        return True
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    #print(french_text)
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    #write the code here
    if french_text is None:
        return True
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    #print(english_text)
    return english_text['translations'][0]['translation']