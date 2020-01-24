import pytest

@pytest.mark.parametrize("i",[65,87,45,98,80])
def test(i):
    print(i)
    assert i>50