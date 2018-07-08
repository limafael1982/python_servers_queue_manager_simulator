##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
# This set of unit tests is responsible for testing the Client class
##########################################

import pytest

from Classes.Client import Client


@pytest.fixture
def conf():
    conf = {'UMAX': 2, 'TTASK': 4}
    return conf


def test_client_constructor(conf):
    client1 = Client()
    assert 1 == client1.get_current_hop()
    assert type(client1.get_hash_code()) == str
