import pytest
from parametrize_example.read_excel_data import get_data
@pytest.mark.parametrize("name,addrs,acc,details",get_data())
def test_01(name, addrs, acc, details):
    print(name, addrs, acc, details)