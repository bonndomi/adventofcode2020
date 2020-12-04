import os.path

import pytest


@pytest.fixture(params=['javier', 'jessica', 'reference'])
def user(request):
    return request.param


@pytest.fixture()
def user_data(user):
    root = os.path.dirname(os.path.abspath(__file__))
    yield os.path.join(root, user)
