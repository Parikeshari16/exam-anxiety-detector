# Placeholder for FastAPI backend
from fastapi import FastAPI
from model.bert_model import predict_anxiety

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Exam Anxiety Detector API"}

@app.post("/predict")
def predict(text: str):
    result = predict_anxiety(text)
    return {"prediction": result}
