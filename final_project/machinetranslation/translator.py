"""module for translation"""
from deep_translator import MyMemoryTranslator



def english_to_french(english_text):
    """this function translate fron english text to french text"""
    french_text = MyMemoryTranslator(source='english',target='french').translate(english_text)
    return french_text



def french_to_english(french_text):
    """this function translate from french text to english text"""
    english_text =  MyMemoryTranslator(source='french',target='english').translate(french_text)
    return english_text
