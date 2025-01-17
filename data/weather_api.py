

import requests
import json
import pandas as pd

# API URL
url = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=auto"

#Send the GET request
response = requests.get(url)

# Check if the request is successful
if response.status_code == 200:
    print("Data retrieved successfully!")
    weather_data = response.json()  
else:
    print(f"Unable to fetch data. Status code: {response.status_code}")
    exit()

# Extract hourly data
hourly_data = weather_data.get("hourly", {})
if not hourly_data:
    print("No hourly data found in the response.")
    exit()

# Convert hourly data to a DataFrame
df = pd.DataFrame(hourly_data)

# Save the DataFrame to a CSV file
df.to_csv("weather_data.csv", index=False)
print("Data saved to weather_data.csv")

# Save the weather data to a JSON file
json.dump(weather_data, open("weather_data.json", "w"), indent=4)
print("Data saved to weather_data.json")

df.dropna(inplace=True)
