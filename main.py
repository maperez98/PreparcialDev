from fastapi import FastAPI

app = FastAPI()


@app.get("/2prueba")
def read_root():
    return {"Hello": "Esta es la prueba para  verificar que funciona lanzar el localhost"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}