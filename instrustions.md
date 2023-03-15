Steps to run api:
1. Create a virtual environment : `python3 -m venv car_price_env`
2. Activate Virtual environment : `source car_price_env/bin/activate`
3. Install requirements : `pip install -r requirements.txt`
4. run : `python3 api.py`
5. Use this dict as a request json: 
{
  "Car_Name": "ritz",
  "Present_Price": 5.59,
  "Kms_Driven": 27000,
  "Fuel_Type": "Petrol",
  "Seller_Type": "Dealer",
  "Transmission": "Manual",
  "Age": 9
}
