##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################

import Client


class Server:

    # constructor:
    def __init__(self, max_num_clients, max_hops):
        self.__no_connected_clients = 0
        self.__umax = max_num_clients
        self.__max_hops = max_hops
        self.clients = []

    # public methods
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
        The update_clients_hop returns:
        0 -> if all the clients hop were successfully updated
        1 -> if the clients list is empty
    '''

    def update_clients_hop(self):
        return_value = 1
        new_clients_list = []
        if len(self.clients) > 0:
            for c in self.clients:
                c.increase_hop()
                new_clients_list.append(c)
            return_value = 0
        return return_value

    # protected methods:
    def _remove_client_from_server_based_on_hop(self):
        clients_hash_to_remove = []
        if len(self.clients) > 0:
            for i in range(0, len(self.clients)):
                if self.clients[i].get_current_hop() >= self.__max_hops:
                    clients_hash_to_remove.append(self.clients[i].get_hash_code())
        if len(clients_hash_to_remove) > 0:
            for hash in clients_hash_to_remove:
                for c in self.clients:
                    if c.get_hash_code() == hash:
                        assert isinstance(c, Client)
                        self.clients.remove(c)
