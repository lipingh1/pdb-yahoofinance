import pytest
from app import folder_path_gen

def test_folder_path_correct():
	input_timestamp = "20020202"
	expected_output = "insight/20020202/data/insightdata.json"
	actual_output = folder_path_gen(input_timestamp)
	assert actual_output ==   expected_output