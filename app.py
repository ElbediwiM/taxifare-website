import requests
import streamlit as st
import pandas as pd
import pydeck as pkl
'''
# TaxiFareModel front
'''
API_URL = "https://taxifare.lewagon.ai/predict"


            


st.title("🚕 NYC Taxi Fare Predictor")

with st.form("predict"):
    pickup_dt   = st.text_input("Pickup datetime (YYYY-MM-DD HH:MM:SS)",
                                "2014-07-06 19:18:00")
    pickup_lon  = st.number_input("Pickup longitude",  value=-73.950655)
    pickup_lat  = st.number_input("Pickup latitude",   value=40.783282)
    dropoff_lon = st.number_input("Drop-off longitude", value=-73.984365)
    dropoff_lat = st.number_input("Drop-off latitude",  value=40.769802)
    passengers  = st.number_input("Passengers", min_value=1, max_value=8, value=2)
    submitted = st.form_submit_button("Predict 🚀")

if submitted:
    params = dict(
        pickup_datetime=pickup_dt,
        pickup_longitude=pickup_lon,
        pickup_latitude=pickup_lat,
        dropoff_longitude=dropoff_lon,
        dropoff_latitude=dropoff_lat,
        passenger_count=passengers,
    )
    resp = requests.get(API_URL, params=params).json()
    fare = resp["fare"]
    st.success(f"💰 Estimated fare: **${fare:.2f}**")
df = pd.DataFrame([
    {"lat": pickup_lat, "lon": pickup_lon, "color": [0, 255, 0]},
    {"lat": dropoff_lat, "lon": dropoff_lon, "color": [255, 0, 0]},
])
st.map(df)  # Streamlit’s built-in map



## Finally, we can display the prediction to the user


