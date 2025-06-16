from typing import Union
from fastapi import FastAPI

app = FastAPI()
# RESTAPI 
@app.get("/")
def read_root():
    return {"Hello": "ABHISEK M HIREMATH"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}
