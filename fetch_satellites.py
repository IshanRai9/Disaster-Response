FIRMS_API = "695848598e7868c4098c3be1604b46a4"
url = f"https://firms.modaps.eosdis.nasa.gov/api/v1/area/csv?key={FIRMS_API}&bbox=-120,35,-119,36&date=2024-02-01&sensor=VIIRS_NOAA20"
response = requests.get(url)

data = response.json()
print(data)