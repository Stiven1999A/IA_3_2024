from nltk import word_tokenize
from cleaning import clean_text

def tokenizar_texto(texto):
    """Esta función tokeniza el texto limpio"""
    texto_limpio = clean_text(texto)
    tokens = word_tokenize(texto_limpio)
    return tokens
