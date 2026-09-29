from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib

app=FastAPI()
model=joblib.load('review.pkl')

@app.get("/")
def home():
    return {'msg':'Welcome to the world of API'}

@app.get("/details")
def details():
    return {'name':'Aditya','age':41}

@app.get("/predict")
def predict(review:str):
    p=model.predict([review])
    return JSONResponse({'prediction':str(p[0])})