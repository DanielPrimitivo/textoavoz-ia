# Textoavoz-ia

Textoavoz-ia trata de un cliente (Flask), en el cual, podemos subir una imagen con texto que llama a una API (FastAPI) que extrae el texto de la imagen y que es devuelto al cliente para que este transforme el texto a voz.

## Installation

La app1 (Flask) es levantada en un entorno virtual y las librerías utilizadas las podemos encontrar en requimerents.txt

La app2 (FastAPI) es levantada con Docker y la imagen utilizada se encuentra en: https://hub.docker.com/r/dprimitivoc/app2_web/tags

## Usage

Crear entorno virtual en app1 e instalar las librerías que podemos encontrar en requirements.txt

```bash
# activar entorno virtual
app1$ source venvPR1/bin/activate

export FLASK_APP=app
export FLASK_ENV=development

# levantar app1
app1/code$ flask run
```

Utilizar la imagen de Docker Hub para levantar la app2.
