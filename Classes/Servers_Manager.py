##########################################
# Author: Rafael Lima
# Date of Creation: Saturday, July 7 2018
##########################################

from Server import Server
from Client import Client

class ServersManager:

    # constructor
    def __init__(self, ttask, umax):
        self.__overall_ticks = 0
        self.__overall_cost = 0
        self.__servers_list = []
        self.__ttask = ttask
        self.__umax = umax

    # protected methods:

    def _add_server_to_list(self, server):
        assert isinstance(server, Server)
        self.__servers_list.append(server)
        return server.get_id()

    def _remove_server_from_list_based_on_id(self, server_id):
        for s in self.__servers_list:
            if server_id == s.get_id():
                assert isinstance(s, Server)
                self.__servers_list.remove(s)

    # public methods:

    def get_overall_ticks(self):
        return self.__overall_ticks

    # TODO: construct a logic to get the overall cost

    def update_overall_ticks(self):
        self.__overall_ticks = self.__overall_ticks + 1

    def get_string_with_servers_and_clients(self):
        text_to_be_printed = ""
        if len(self.__servers_list) > 0:
            for s in self.__servers_list:
                assert(s, Server)
                text_to_be_printed = text_to_be_printed + str(s.get_current_number_of_clients()) + " "
        return text_to_be_printed

    def add_input_clients_to_server_set(self, no_clients):
        nserver = 0
        ans = -1
        non_added_clients = no_clients
        if len(self.__servers_list > 0):
            while non_added_clients > 0:
                client = Client()
                while nserver < len(self.__servers_list):
                    if self.__servers_list[nserver].add_client(client) == 0:
                        non_added_clients = non_added_clients - 1
                        pass
                    else:
                        nserver = nserver + 1
                ans = self._alloc_server_based_on_remaining_clients(non_added_clients, nserver, client)
        else:
            ans = self._alloc_server_based_on_remaining_clients(self, non_added_clients, 0, None)
        return ans

    def _alloc_server_based_on_remaining_clients(self, non_added_clients, starting_point, client):
        servers_to_alloc = (non_added_clients / self.__umax) + (non_added_clients % self.__umax)
        for s in range(0, servers_to_alloc):
            server = Server()
            print('Added server with id: %s' % self._add_server_to_list(server))
        s = starting_point
        while non_added_clients > 0:
            while s < len(self.__servers_list):
                if type(client) is None:
                    client = Client()
                if self.__servers_list[s].add_client(client) == 1:
                    s = s + 1
                else:
                    non_added_clients = non_added_clients - 1
        return non_added_clients



























