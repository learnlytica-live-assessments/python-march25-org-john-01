import pytest
from assignments.assignment1 import add

def test_add():
    # Verify that the add function works as expected.
    assert add(2, 3) == 5, "Expected add(2, 3) to return 5"