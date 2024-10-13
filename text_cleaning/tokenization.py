from nltk import word_tokenize
from text_cleaning.cleaning import clean_text

def tokenizar_texto(texto):
    """
    Esta función tokeniza el texto limpio.
    
    Args:
        texto (str): El texto a limpiar y tokenizar.
        
    Returns:
        list: Una lista de tokens.
        
    Raises:
        ValueError: Si el texto proporcionado no es una cadena.
    """
    if not isinstance(texto, str):
        raise ValueError("El texto proporcionado debe ser una cadena.")
    
    try:
        texto_limpio = clean_text(texto)
        tokens = word_tokenize(texto_limpio)
        return tokens
    except Exception as e:
        print(f"Error al tokenizar el texto: {e}")
        return []
