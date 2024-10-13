import spacy

def load_spacy_model(model_name="es_core_news_sm"):
    """Carga el modelo de spaCy especificado.
    
    Args:
        model_name (str): Nombre del modelo de spaCy a cargar.
        
    Returns:
        spacy.lang: El modelo de spaCy cargado.
    """
    try:
        nlp = spacy.load(model_name)
        return nlp
    except OSError as e:
        print(f"Error al cargar el modelo de spaCy: {e}")
        return None

def lemmatize_text(texto, nlp):
    """Lematiza el texto usando el modelo spaCy especificado.
    
    Args:
        texto (str): El texto a lematizar.
        nlp (spacy.lang): El modelo de spaCy cargado.
        
    Returns:
        str: El texto lematizado.
    """
    if nlp is None:
        return texto
    
    doc = nlp(texto)
    return " ".join([token.lemma_ for token in doc])

# Cargar el modelo de spaCy en español
nlp = load_spacy_model()

# Ejemplo de uso
texto = "Los gatos están jugando en el jardín."
texto_lematizado = lemmatize_text(texto, nlp)
print(texto_lematizado)
