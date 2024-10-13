import unicodedata
import re
from nltk.corpus import stopwords

def palabras_numeros(texto):
    """Esta función elimina números de las palabras que los contienen"""
    patron = r'\b\w*[a-zA-Z]+\w*\d+\w*\b|\b\w*\d+\w*[a-zA-Z]+\w*\b'
    palabras_con_numeros = re.findall(patron, texto)
    palabras_limpias = [re.sub(r'\d+', '', word) for word in palabras_con_numeros]
    diccionario = dict(zip(palabras_con_numeros, palabras_limpias))
    for viejo, nuevo in diccionario.items():
        texto = texto.replace(viejo, nuevo)
    return texto

def eliminar_tildes(texto):
    """Esta función elimina tildes"""
    return "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))

def eliminar_stopwords(texto):
    """Esta función elimina las stopwords en español"""
    stop_words = set(stopwords.words('spanish'))
    texto = ' '.join([word for word in texto.split() if word.lower() not in stop_words])
    return texto

def clean_text(text):
    """Esta función integra las funciones de limpieza de texto"""
    text = re.sub(r'\.\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r"(19|20|21)(\d{2})\d{2}", r"\1\2", text)
    text = eliminar_tildes(text)
    text = text.lower()
    text = palabras_numeros(text)
    text = eliminar_stopwords(text)
    return text
