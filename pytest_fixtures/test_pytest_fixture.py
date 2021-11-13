import pytest


@pytest.fixture()
def setUp():
    print("\nSetup")


def test1(setUp):
    print("Executing test1!")
    assert True


@pytest.mark.usefixtures("setUp")
def test2():
    print("Executing test2!")
    assert True
