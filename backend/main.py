from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hood-pop backend is running"}