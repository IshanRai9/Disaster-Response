# Create a virtual environment
python -m venv path/disaster_env 
python disaster_env/bin/activate  
On Windows, use: disaster_env\Scripts\activate

# Install required Python libraries
pip install torch transformers requests tweepy flask fastapi beautifulsoup4 pandas numpy geopandas opencv-python matplotlib python-dotenv streamlit

# API keys:
Twitter: https://developer.twitter.com/
Nasa Firms (scroll down and click on get map key): https://firms.modaps.eosdis.nasa.gov/api/area/
