import requests
import pandas as pd
from datetime import datetime

# Step 1: Set the city and URL
city = "Stockholm"
url = f"https://wttr.in/{city}?format=%t"  # %t gives temperature in Celsius

# Step 2: Get the temperature
response = requests.get(url)
temperature = response.text.strip()  # e.g., '+15°C'

# Step 3: Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Step 4: Save to CSV
df = pd.DataFrame([{
    "Timestamp": timestamp,
    "Temperature": temperature
}])

# Append to existing CSV or create new
csv_file = "temperature_log.csv"
try:
    existing_df = pd.read_csv(csv_file)
    df = pd.concat([existing_df, df], ignore_index=True)
except FileNotFoundError:
    pass

df.to_csv(csv_file, index=False)
print(f"Logged temperature: {temperature} at {timestamp}")
