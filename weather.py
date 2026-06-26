import requests
# Your API key from OpenWeatherMap
API_KEY = "ad36fc30e1612de40f5de2f55f3c88d6"
# City you want weather for
city = input("Enter city name: ")
# Build the URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
# Send the request
response = requests.get(url)
# Check if request was successful
if response.status_code == 200:
    # Convert response to dictionary
    data = response.json()
    # Extract and print the values
    print("\n--- Weather Report ---")
    print("City        :", data["name"])
    print("Country     :", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels Like  :", data["main"]["feels_like"], "°C")
    print("Min Temp    :", data["main"]["temp_min"], "°C")
    print("Max Temp    :", data["main"]["temp_max"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Wind Speed  :", data["wind"]["speed"], "m/s")
    print("Condition   :", data["weather"][0]["description"].title())
elif response.status_code == 401:
    print("Invalid API key. Wait 2 hours if you just created it.")
elif response.status_code == 404:
    print("City not found. Check the spelling.")
else:
    print("Something went wrong. Status code:", response.status_code)