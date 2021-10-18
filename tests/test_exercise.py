import pytest
import os

def test_exercise(capsys):
    os.chdir('src')

    from exercise import read_records_from_file
    file = "data.txt"
    records = read_records_from_file(file)

    assert records == ["lily","anton","levi","amy"]
