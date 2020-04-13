import pytest
from ..app import add_timestamp_to_insight_json


def test_timestamp_add_correct():
	input_timestamp = "20020202"
	input_data = {"data": "test"}
	expected_output = {"data": "test",
						"ingestion_timestamp": "20020202"}
	actual_output = add_timestamp_to_insight_json(input_timestamp, input_data)
	assert actual_output == expected_output