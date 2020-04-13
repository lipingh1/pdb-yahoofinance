from datetime import datetime

import boto3
import json
import requests
import logging


LOGGING_LEVEL = "DEBUG"


def folder_path_gen(timestamp_str):
	folder_path = f"insight/{timestamp_str}/data/insightdata.json" 
	return folder_path


def add_timestamp_to_insight_json(timestamp, input_json):
	input_json["ingestion_timestamp"] = timestamp
	return input_json


def main():
	logger = logging.getLogger()
	logger.info("requesting date from insight API...")
	logger.debug("accessing url 'https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0'")

	insight_api_response = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')
	logger.debug("convert API response into json format")
	insight_data = insight_api_response.json()

	logger.debug("add current datetime to json with ingestion_timestamp")
	timestamp_str = datetime.now().strftime("%Y%m%d")
	add_timestamp_to_insight_json(timestamp_str, insight_data)

	logger.info("uploading json into s3")
	logger.debug("generate folder path with timestamp")
	folder_path = folder_path_gen(timestamp_str)

	logger.debug("using boto3, uploading json file'insight_date' into bucket'pdl-dev-nasa' with folder path")
	s3 = boto3.client('s3')
	s3.put_object(Body=json.dumps(insight_data), Bucket='pdl-dev-nasa', Key=folder_path)

	return


if __name__ == "__main__":
	main()
