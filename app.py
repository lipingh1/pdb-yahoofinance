from datetime import datetime

import boto3
import json
import requests


def folder_path_gen(timestamp_str):
	folder_path = f"insight/{timestamp_str}/data/insightdata.json" 
	return folder_path


def add_timestamp_to_insight_json(timestamp, input_json):
	input_json["ingestion_timestamp"] = timestamp
	return input_json


def main():
	insight_api_response = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')
	insight_data = insight_api_response.json()

	timestamp_str = datetime.now().strftime("%Y%m%d")
	add_timestamp_to_insight_json(timestamp_str,insight_data)

	folder_path = folder_path_gen(timestamp_str)

	s3 = boto3.client('s3')
	s3.put_object(Body=json.dumps(insight_data), Bucket='pdl-dev-nasa', Key=folder_path)

	return
 


if __name__ == "__main__":
	main()
