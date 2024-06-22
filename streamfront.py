import streamlit as st
import requests

BASE_URL = "http://localhost:5000"

st.title("Modular Request Resolver")

# Mapping Application
st.header("Mapping Application")
origin = st.text_input("Origin", "New York")
destination = st.text_input("Destination", "Los Angeles")
if st.button("Get Directions"):
    response = requests.get(f"{BASE_URL}/mapping/directions", params={"origin": origin, "destination": destination})
    if response.status_code == 200:
        st.write(response.json()["directions"])
    else:
        st.error(response.json().get("error", "An error occurred"))

# Song Player
st.header("Song Player")
song_id = st.text_input("Song ID", "12345")
if st.button("Play Song"):
    response = requests.post(f"{BASE_URL}/song/play", json={"song_id": song_id})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

if st.button("Stop Song"):
    response = requests.post(f"{BASE_URL}/song/stop")
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

# Lighting and AC Control
st.header("Lighting and AC Control")
intensity = st.slider("Lighting Intensity", 0, 100, 50)
if st.button("Set Lighting"):
    response = requests.post(f"{BASE_URL}/lighting/set", json={"intensity": intensity})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

temperature = st.slider("AC Temperature (°C)", 16, 30, 22)
if st.button("Set AC Temperature"):
    response = requests.post(f"{BASE_URL}/ac/set", json={"temperature": temperature})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))
