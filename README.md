# CS 335 — Assignment 01: Working with AI & ML APIs
**Northeastern Illinois University — Introduction to Artificial Intelligence**  
Instructor: O. Adham-Sindy, MS, PMP

---
# Assignment 01 — API Implementation

**Name:** Rubi Shrestha
**Course:** CS 335 — Introduction to Artificial Intelligence
**API Used:** Open-Meteo Weather API

## Description

This project uses the Open-Meteo API to retrieve weather data using Python.
It makes multiple API calls to fetch hourly temperature data for different cities.

## API Calls Implemented

1. New York weather (GET request)
2. Chicago weather (GET request)
3. Parameterized weather request (Warsaw, Miami, Los Angeles)

## Sample Output

CALL 1 — New York Weather
2026-04-28T00:00 → 12.3°C
2026-04-28T01:00 → 11.8°C

CALL 2 — Chicago Weather
2026-04-28T00:00 → 10.1°C

CALL 3 — Warsaw Weather
2026-04-28T00:00 → 8.5°C

## Notes

* Used latitude and longitude for API requests
* Extracted hourly temperature data from JSON response
* Open-Meteo API does not require an API key
