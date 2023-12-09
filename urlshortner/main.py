from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def default():
    return {"message":"Welcome to this FastAPI app"}


@app.post('/shorten')
def shorten():
    return {"message":"Welcome to this FastAPI app"}