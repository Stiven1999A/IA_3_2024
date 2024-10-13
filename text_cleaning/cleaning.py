import unicodedata
import re
from nltk.corpus import stopwords

def palabras_numeros(texto):
    """
    Elimina números de las palabras que los contienen.
    
    Args:
        texto (str): El texto a procesar.
    
    Returns:
        str: El texto con las palabras que contenían números limpiadas.
    """
    patron = r'\b\w*[a-zA-Z]+\w*\d+\w*\b|\b\w*\d+\w*[a-zA-Z]+\w*\b'
    palabras_con_numeros = re.findall(patron, texto)
    palabras_limpias = [re.sub(r'\d+', '', word) for word in palabras_con_numeros]
    for viejo, nuevo in zip(palabras_con_numeros, palabras_limpias):
        texto = texto.replace(viejo, nuevo)
    return texto

def eliminar_tildes(texto):
    """
    Elimina tildes del texto.
    
    Args:
        texto (str): El texto a procesar.
    
    Returns:
        str: El texto sin tildes.
    """
    return ''.join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))

def eliminar_stopwords(texto):
    """
    Elimina las stopwords en español.
    
    Args:
        texto (str): El texto a procesar.
    
    Returns:
        str: El texto sin stopwords.
    """
    stop_words = set(stopwords.words('spanish'))
    return ' '.join(word for word in texto.split() if word.lower() not in stop_words)

def clean_text(texto):
    """
    Integra las funciones de limpieza de texto.
    
    Args:
        texto (str): El texto a procesar.
    
    Returns:
        str: El texto limpio.
    """
    texto = re.sub(r'\.\d+', '', texto)  # Elimina decimales
    texto = re.sub(r'[^\w\s]', '', texto)  # Elimina caracteres no alfanuméricos
    texto = re.sub(r'(19|20|21)(\d{2})\d{2}', r'\1\2', texto)  # Corrige años mal formateados
    texto = eliminar_tildes(texto)
    texto = texto.lower()
    texto = palabras_numeros(texto)
    texto = eliminar_stopwords(texto)
    return texto
