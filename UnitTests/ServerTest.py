##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
# This set of unit tests is responsible for testing the Server class
##########################################

import pytest

from Classes.Server import Server
from Classes.Client import Client

@pytest.fixture
def conf():
    conf = {'UMAX' : 2, 'TTASK' : 4}
    return conf


def test_server_constructor(conf):

    server1 = Server(conf['UMAX'], conf['TTASK'])
    assert 1 == server1.get_server_tick()

    assert 0 == server1.get_current_number_of_clients()

    assert type(server1.get_id()) == str


def test_server_add_client(conf):

    server1 = Server(conf['UMAX'], conf['TTASK'])
    client1 = Client()

    server1.add_client(client1)

    assert 1 == len(server1.clients), "There was an error an adding the client"
    assert 1 == server1.get_current_number_of_clients(), "There was an error an counting the number of clients"


def test_remove_client_from_server(conf):

    server1 = Server(conf['UMAX'], conf['TTASK'])
    client1 = Client()
    client_hash_code = client1.get_hash_code()
    server1.add_client(client1)

    assert str == type(client_hash_code), "The hash code must be a string"

    # before removing, the server length should be 1
    assert 1 == server1.get_current_number_of_clients()

    server1._remove_client_from_server_using_hash_code(client_hash_code)
    # now the server should not have any clients
    assert 0 == server1.get_current_number_of_clients()


def test_clients_who_have_hops_larger_than_umax_shall_not_stay_on_server(conf):

    server1 = Server(conf['UMAX'], conf['TTASK'])
    client1 = Client()

    for i in range(0, conf['UMAX'] + 5):
        client1.increase_hop()

    server1.add_client(client1)
    server1.update_server_status()

    assert 0 == server1.get_current_number_of_clients()







