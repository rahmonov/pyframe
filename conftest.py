import pytest

from pyframe.api import PyFrameAPI


@pytest.fixture
def api():
    return PyFrameAPI()

@pytest.fixture
def client(api):
    return api.test_session()
