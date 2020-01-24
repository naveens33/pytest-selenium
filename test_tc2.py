import pytest

class Test_tc2:
    def test_02(self):
        print("test02")

    @pytest.mark.skip("Not yet developed")
    def test_03(self):
        print("test03")

    @pytest.mark.skipif(5 == 5, reason="Not yet developed")
    def test_04(self):
        print("test04")

    # Asserting expected exception
    def test_05(self):
        with pytest.raises(Exception):
            raise Exception
            print("test05")


class Test_tc3:
    def test_02(self):
        print("test02")

    @pytest.mark.skip("Not yet developed")
    def test_03(self):
        print("test03")

    @pytest.mark.skipif(5 == 5, reason="Not yet developed")
    def test_04(self):
        print("test04")

    # Asserting expected exception
    def test_05(self):
        with pytest.raises(Exception):
            raise Exception
            print("test05")
