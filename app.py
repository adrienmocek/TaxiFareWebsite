import streamlit as st
import requests
import datetime as dt

date = st.date_input('Enter a date ')
time = st.time_input('Enter a time', dt.datetime(2022,2,25,10,30))
date_time = str(date) + " " + str(time)
pickup_longitude = st.number_input('Enter a pickup longitude')
pickup_latitude = st.number_input('Enter a pickup latitude')
dropoff_longitude = st.number_input('Enter a dropoff longitude')
dropoff_latitude = st.number_input('Enter a dropoff latitude')
passenger_count = st.number_input('Enter a passenger count')

params = {'pickup_datetime': date_time,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': int(passenger_count)
}


url = 'https://taxifare.lewagon.ai/predict'

response = requests.get(url, params)
response = response.json()
st.markdown(response)
