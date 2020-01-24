import pytest


@pytest.fixture(scope="session", autouse=True)
def object(request):
    x = 6
    print("enter->Session")

    def exit():
        print("exit->Session")

    request.addfinalizer(exit)
    return x
'''
@pytest.fixture(autouse=True)
def object1(request):
    x = 5
    print("enter")

    def exit():
        print("exit")

    request.addfinalizer(exit)
    return x
'''