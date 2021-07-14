from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def aboba():
    return{"Hello Abobus"}