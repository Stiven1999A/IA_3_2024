import spacy

# Cargar el modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

def lemmatize_text(texto):
    """Esta función lematiza el texto usando el modelo spaCy en español"""
    doc = nlp(texto)
    return " ".join([token.lemma_ for token in doc])
