import requests
from datetime import datetime

insight_api_response = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')
insight_data = insight_api_response.json()

date_time_obj = datetime.now()
timestamp_str = date_time_obj.strftime("%Y%m%d")
print(timestamp_str)

insight_data["ingestion_timestamp"] = timestamp_str

print(insight_data)


def folder_path_gen(timestamp_str):
	folder_path = f"insight/{timestamp_str}/data/insightdata.json" 
	return folder_path

print(folder_path_gen(timestamp_str))