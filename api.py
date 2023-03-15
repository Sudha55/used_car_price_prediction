import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

# Load the model and scaler objects from the .pkl files
model = joblib.load("linreg.pkl")
sc = joblib.load("sc.pkl")

car_label_encode = joblib.load("label_encoder_for_car_name.pkl")

fuel_type_label_encode = joblib.load("label_encoder_for_fuel_type.pkl")

label_encoder_for_seller_type = joblib.load("label_encoder_for_seller_type.pkl") 

label_encoder_for_transmission = joblib.load("label_encoder_for_transmission.pkl")

class CarData(BaseModel):
    Car_Name: str
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    Age: int


app = FastAPI()


@app.post("/predict")
def predict(data: CarData):
    df = pd.DataFrame([data.dict()])

    df['Car_Name'] = car_label_encode.transform(df['Car_Name'])

    df['Fuel_Type'] = fuel_type_label_encode.transform(df['Fuel_Type'])

    df['Seller_Type'] = label_encoder_for_seller_type.transform(df['Seller_Type'])

    df['Transmission'] = label_encoder_for_transmission.transform(df['Transmission'])

    x = sc.transform(df)

    y_pred=model.predict(x)
    print("Y pred", y_pred)
    return str(y_pred[0])


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8501)


