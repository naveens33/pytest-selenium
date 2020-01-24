import pytest


class Test_tc1:
    @pytest.fixture(autouse=True)
    def object1(self, request, object):
        x = object
        print("enter")

        def exit():
            print("exit")

        request.addfinalizer(exit)
        return x

    def setup_method(self, method):
        print("setup_method")

    @pytest.mark.run(order=2)
    def test_01(self,object1,object):
        print(object1,object)
        print("test01")

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_02(self):
        print("test02")

    def teardown_method(self, method):
        print("teardown_method")