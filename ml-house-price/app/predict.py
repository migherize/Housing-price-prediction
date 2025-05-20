import joblib
import numpy as np
from app.schemas import HouseFeatures

model = joblib.load("app/model.joblib")

def predict_price(features: HouseFeatures):
    data = np.array([[features.MedInc, features.HouseAge, features.AveRooms,
                      features.AveBedrms, features.Population, features.AveOccup,
                      features.Latitude, features.Longitude]])
    return model.predict(data)[0]
