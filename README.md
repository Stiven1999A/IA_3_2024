# Proyecto de Procesamiento de Lenguaje Natural (NLP)

## Descripción

Este proyecto utiliza varias técnicas de procesamiento de lenguaje natural (NLP) para limpiar, tokenizar y lematizar texto en español. Utiliza las librerías NLTK y spaCy para realizar estas tareas. El objetivo principal es proporcionar herramientas para el preprocesamiento de texto que pueden ser utilizadas en diversas aplicaciones de NLP.

## Estructura del Proyecto

```
IA_3_2024/
├── __init__.py
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
└── text_cleaning/
    ├── __init__.py
    ├── cleaning.py
    ├── lematization.py
    └── tokenization.py
```

## Archivos Principales

- `main.py`: Archivo principal para ejecutar el proyecto.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.
- `text_cleaning/lematization.py`: Contiene la función de lematización utilizando spaCy.
- `text_cleaning/tokenization.py`: Contiene funciones para la tokenización del texto.
- `text_cleaning/cleaning.py`: Contiene funciones para la limpieza del texto.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone -b feature/NLTK <URL_DEL_REPOSITORIO>
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd IA_3_2024
    ```
3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Descarga los paquetes necesarios de NLTK y spaCy:
    ```sh
    python -m spacy download es_core_news_sm
    python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
    ```

## Uso

Para ejecutar el archivo `main.py` y ver un ejemplo de uso de las funciones de tokenización y lematización, sigue estos pasos:

1. Asegúrate de haber instalado todas las dependencias y descargado los paquetes necesarios de NLTK y spaCy como se describe en la sección de Instalación.

2. Ejecuta el archivo `main.py`:
    ```sh
    python main.py
    ```

El contenido de `main.py` es el siguiente:

```python
"""Ejemplo de Uso de las funciones de tokenización y lematización de texto"""
import nltk
from text_cleaning.tokenization import tokenizar_texto
from text_cleaning.lematization import lemmatize_text

# Descarga de paquetes de nltk
nltk.download('punkt')
nltk.download('stopwords')

# Texto que vamos a procesar
texto = "El año 2021 fue increíble, pero el 2022 será aún mejor!"

# Tokenización del texto
texto_tokens = tokenizar_texto(texto)
print("Tokens:", texto_tokens)

# Lematización del texto
lemmatized_text = lemmatize_text(texto)
print("Texto lematizado:", lemmatized_text)
```

Este script descargará los paquetes necesarios de NLTK, procesará el texto de ejemplo, lo tokenizará y lematizará, y luego imprimirá los resultados en la consola.


### Funcionalidades

### Limpieza de Texto
La limpieza de texto se realiza utilizando varias funciones definidas en `text_cleaning/cleaning.py`. Estas funciones incluyen:

- `palabras_numeros(texto)`: Elimina los números de las palabras que los contienen.
- `eliminar_tildes(texto)`: Elimina las tildes de las palabras.
- `eliminar_stopwords(texto)`: Elimina las stopwords en español utilizando la librería NLTK.
- `clean_text(text)`: Integra todas las funciones anteriores para realizar una limpieza completa del texto. Esta función elimina caracteres especiales, convierte el texto a minúsculas, elimina números de las palabras, elimina tildes y elimina stopwords.

Ejemplo de uso:
```python
from text_cleaning.cleaning import clean_text

texto = "El año 2021 fue increíble, pero el 2022 será aún mejor!"
texto_limpio = clean_text(texto)
print(texto_limpio)
```

Este código imprimirá:
```
año fue increible pero sera aun mejor
```

### Tokenización
La tokenización se realiza utilizando funciones definidas en `text_cleaning/tokenization.py`. La función `tokenizar_texto` toma un texto como entrada, lo limpia utilizando la función `clean_text` y luego lo tokeniza utilizando `word_tokenize` de NLTK. 

Ejemplo de uso:
```python
from text_cleaning.tokenization import tokenizar_texto

texto = "El año 2021 fue increíble, pero el 2022 será aún mejor!"
tokens = tokenizar_texto(texto)
print(tokens)
```

Este código imprimirá:
```
['año', 'fue', 'increible', 'pero', 'sera', 'aun', 'mejor']
```

### Lematización
La lematización se realiza utilizando el modelo de spaCy en español. La función `lemmatize_text` en `text_cleaning/lematization.py` toma un texto como entrada y devuelve el texto lematizado.

Ejemplo de uso:
```python
from text_cleaning.lematization import lemmatize_text

texto = "Los gatos están corriendo y saltando por el jardín."
texto_lematizado = lemmatize_text(texto)
print(texto_lematizado)
```

Este código imprimirá:
```
el gato estar correr y saltar por el jardín
```

### Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

