import pytest

@pytest.mark.parametrize("uname,pword",[("test01","pw01"),("test02","pw02")])
def test(uname,pword):
    print(uname,pword)