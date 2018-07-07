##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################

import Client
from uuid import uuid4
from time import strftime


class Server:

    # constructor:
    def __init__(self, max_num_clients, max_hops):
        self.__no_connected_clients = 0
        self.__umax = max_num_clients
        self.__max_hops = max_hops
        self.__id = self._generate_server_id()
        self.clients = []

    # public methods:

    '''
        The add_client method returns:
        0 -> a client was successfully added
        1 -> number of maximum clients was reached.
    '''

    def add_client(self, client):
        if self.__no_connected_clients >= self.__umax:
            print('Maximum number of maximum clients UMAX=% in this server reached.' % self.__umax)
            return_value = 1
        else:
            self.__no_connected_clients = self.__no_connected_clients + 1
            self.clients.append(client)
            return_value = 0
        return return_value

    '''
        The update_server_status must be called each time a clock tick passes:
        It returns:
        0 -> All occured as expected
        1 -> No client removed
        2 -> Client list was empty
    '''

    def update_server_status(self):
        return_value = self._update_clients_hop()
        return_value = return_value + self._remove_client_from_server_based_on_hop()
        return return_value

    # protected methods:

    @staticmethod
    def _generate_server_id():
        return str(uuid4().hex) + strftime("%Y-%m-%d-%H-%M-%S")

    '''
        The update_clients_hop returns:
        0 -> if all the clients hop were successfully updated
        1 -> if the clients list is empty
    '''

    def _update_clients_hop(self):
        return_value = 1
        new_clients_list = []
        if len(self.clients) > 0 and self.__no_connected_clients > 0:
            for c in self.clients:
                c.increase_hop()
                new_clients_list.append(c)
            return_value = 0
        return return_value

    def _remove_client_from_server_using_hash_code(self, hash_code):
        if self.__no_connected_clients > 0:
            for c in self.clients:
                if c.get_hash_code() == hash_code:
                    assert isinstance(c, Client)
                    self.clients.remove(c)
                    self.__no_connected_clients = self.__no_connected_clients - 1

    '''
        The _remove_client_from_server_based_on_hop method returns:
        1 -> if no client was removed
        0 -> There was (were) client (s) removed. 
    '''

    def _remove_client_from_server_based_on_hop(self):
        clients_hash_to_remove = []
        return_value = 1
        if len(self.clients) > 0:
            for i in range(0, len(self.clients)):
                if self.clients[i].get_current_hop() >= self.__max_hops:
                    clients_hash_to_remove.append(self.clients[i].get_hash_code())
                    return_value = 0
        if len(clients_hash_to_remove) > 0:
            for hash in clients_hash_to_remove:  # type: hash: string that contains clients hashcode
                self._remove_client_from_server_using_hash_code(hash)
        return return_value
