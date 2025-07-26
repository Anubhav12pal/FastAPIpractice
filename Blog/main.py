from fastapi import FastAPI



app = FastAPI()

@app.post("/blog")
def create_blog():
    return {"message": "Blog created successfully"}