from fastapi import FastAPI

data = {"Hello": "World ok 2"}
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World ok"}


@app.get("/f2")
def f2():
    return data

@app.get("/f2/{id}")
def f2(id: int):
    return {"id": id, "data": data}
