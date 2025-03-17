import os
import pandas as pd
import numpy as np
import pytest
from assignments.assignment2 import read_data, get_average_salary, get_department_counts, get_top_earners

# Sample data for testing; normally, you might use a temporary CSV file.
TEST_CSV_CONTENT = """Name,Department,Salary,JoiningDate
Alice,HR,50000,2020-01-15
Bob,Engineering,70000,2019-06-01
Charlie,Engineering,65000,2021-03-20
Diana,Marketing,55000,2018-11-30
"""

# Fixture to create a temporary CSV file for testing read_data.
@pytest.fixture
def sample_csv(tmp_path):
    csv_file = tmp_path / "employees.csv"
    csv_file.write_text(TEST_CSV_CONTENT)
    return str(csv_file)

def test_read_data(sample_csv):
    # Test function 1: read_data should return a DataFrame with the correct columns.
    df = read_data(sample_csv)
    assert isinstance(df, pd.DataFrame), "read_data should return a DataFrame."
    expected_columns = {"Name", "Department", "Salary", "JoiningDate"}
    assert expected_columns.issubset(set(df.columns)), f"DataFrame must contain columns {expected_columns}."