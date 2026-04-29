# CS 335 — Introduction to Artificial Intelligence
# API Assignment Starter Code — Northeastern Illinois University
#
# TODO: Replace BASE_URL, endpoints, params, and payload fields
#       with values from your chosen API's documentation.
# ─────────────────────────────────────────────────────────────

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = None

# TODO: Replace with your API's base URL
BASE_URL = "https://api.open-meteo.com/v1"

# update or extend per call if your API requires it



def divider(label):
    print(f"\n{'=' * 50}\n{label}\n{'=' * 50}")


# ── Call 1: GET request ───────────────────────────────────
# Use for retrieving data without a request body.
# TODO: Update url and params.
def call_one_get():
    divider("CALL 1 — New York Weather")

    url = f"{BASE_URL}/forecast"

    params = {"latitude": 40.7128, "longitude": -74.0060, "hourly": "temperature_2m"}  # TODO: update these

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("NYC temperatures (first 5 hours):")
        times = data["hourly"]["time"][:5]
        temps = data["hourly"]["temperature_2m"][:5]

        for t, temp in zip(times, temps):
            print(f"{t} → {temp}°C")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 2: POST request ──────────────────────────────────
# Use for sending data to the API (e.g., a prompt or input text).
# TODO: Update url and payload fields.
def call_two_post():
    divider("CALL 2 — Chicago Weather")

    url = f"{BASE_URL}/forecast"
    params = {"latitude":41.8781, "longitude": -87.6298, "hourly": "temperature_2m"}



    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Chicago temperatures (first 5 hours):")  # TODO: update key
        times = data["hourly"]["time"][:5]
        temps = data["hourly"]["temperature_2m"][:5]

        for t, temp in zip(times, temps):
            print(f"{t} → {temp}°C")


    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 3: Parameterized POST ────────────────────────────
# Same as Call 2 but accepts dynamic input to show varied output.
# TODO: Update url and payload fields.
def call_three_parameterized(city: str):
    divider(f"CALL 3 — {city} Weather")

    cities = { "warsaw": (52.2297, 21.0122), "miami": (25.7617, -80.1918), "los angeles": (34.0522, -118.2437),}
    city = city.lower()
    if city not in cities:
        print("City not supported. Try: warsaw, miami, or los angeles")
        return
    lat, lon = cities[city]

    url = f"{BASE_URL}/forecast"

    params = {"latitude": lat, "longitude": lon, "hourly": "temperature_2m"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"{city.title()} temperature (first 5 hours):")  # TODO: update key
        times = data["hourly"]["time"][:5]
        temps = data["hourly"]["temperature_2m"][:5]

        for t, temp in zip(times, temps):
            print(f"{t} → {temp}°C")

    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


if __name__ == "__main__":
    call_one_get()
    call_two_post()
    call_three_parameterized("Warsaw")

