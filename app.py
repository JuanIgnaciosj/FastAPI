from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # RUTA POR DEFECTO
def message():
    return "hello world"


# OJO  POR QUE LA EJECUCION DEBE SER uvicorn (nombrearchivo.py):app
