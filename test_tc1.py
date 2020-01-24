import pytest

def test_01():
    print("test_01")

def test_02():
    print("test02")
    assert 5 == 7

@pytest.mark.skip("Not yet developed")
def test_03():
    print("test03")

@pytest.mark.skipif(5==5,reason="Not yet developed")
def test_04():
    print("test04")

def test_05():
    print("test05")
    with pytest.raises(Exception):
        raise Exception
