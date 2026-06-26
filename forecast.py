import requests
import pandas as pd

API_KEY = "ad36fc30e1612de40f5de2f55f3c88d6"
city = input("Enter city name: ")

# Forecast endpoint — different from yesterday
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    # data["list"] contains 40 readings — one every 3 hours for 5 days
    readings = []

    for item in data["list"]:
        reading = {
            "datetime"  : item["dt_txt"],
            "temp"      : item["main"]["temp"],
            "feels_like": item["main"]["feels_like"],
            "humidity"  : item["main"]["humidity"],
            "wind"      : item["wind"]["speed"],
            "condition" : item["weather"][0]["description"].title()
        }
        readings.append(reading)

    # Convert list of dictionaries into a DataFrame
    df = pd.DataFrame(readings)

    # Print the full forecast table
    print(f"\n--- 5 Day Forecast for {city.title()} ---\n")
    print(df.to_string(index=False))

    # Some useful info about your data
    print(f"\nTotal readings : {len(df)}")
    print(f"Highest temp   : {df['temp'].max()} °C")
    print(f"Lowest temp    : {df['temp'].min()} °C")
    print(f"Average humidity: {df['humidity'].mean():.1f} %")

elif response.status_code == 401:
    print("Invalid API key.")
elif response.status_code == 404:
    print("City not found.")
else:
    print("Something went wrong. Status code:", response.status_code)