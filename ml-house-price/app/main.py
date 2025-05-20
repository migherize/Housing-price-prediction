from fastapi import FastAPI
from app.predict import predict_price
from app.schemas import HouseFeatures

app = FastAPI()

@app.post("/predict")
def predict(features: HouseFeatures):
    result = predict_price(features)
    return {"prediction": result}
