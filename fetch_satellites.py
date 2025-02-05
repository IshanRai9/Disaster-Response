import os
import requests
from dotenv import load_dotenv

load_dotenv()

FIRMS_API_KEY = os.getenv("FIRMS_API_KEY")
url = f"https://firms.modaps.eosdis.nasa.gov/api/v1/area/csv?key={FIRMS_API_KEY}&bbox=-120,35,-119,36&date=2024-02-01&sensor=VIIRS_NOAA20"
response = requests.get(url)
data = response.text
print(data)