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
        self.__cost_current_tick = []

    # protected methods:

    def _compute_cost_current_tick(self):
        self.__cost_current_tick
        for s in range(0, self.__servers_list):
            self.__cost_current_tick.append(
                dict(server_id=self.__servers_list[s].get_id, current_tick=self.__servers_list[s].get_server_tick))

    def _compute_current_overall_cost(self):
        current_price = 0
        for s in range(0, self.__servers_list):
            current_price = current_price + 1
        self.__overall_cost = self.__overall_cost + current_price

    def _add_server_to_list(self, server):
        assert isinstance(server, Server)
        self.__servers_list.append(server)
        return server.get_id()

    def _remove_server_from_list_based_on_id(self, server_id):
        for s in self.__servers_list:
            if server_id == s.get_id():
                assert isinstance(s, Server)
                self.__servers_list.remove(s)

    def _remove_server_from_list_if_has_no_client(self):
        for s in self.__servers_list:
            if s.get_current_number_of_clients() == 0:
                assert isinstance(s, Server)
                self.__server_list.remove(s)

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

    def _check_positions_from_servers_list(self):
        check_full_vec = []
        self._remove_server_from_list_if_has_no_client()
        for s in range(0, len(self.__servers_list)):
            if self.__servers_list[s].get_current_number_of_clients() == self.__umax:
                check_full_unit = {'Full': True, 'Pos': s,
                                   'Number_of_clients': self.__servers_list[s].get_current_number_of_clients()}
                check_full_vec.append(check_full_unit)
            else:
                check_full_unit = {'Full': False, 'Pos': s,
                                   'Number_of_clients': self.__servers_list[s].get_current_number_of_clients()}
                check_full_vec.append(check_full_unit)
            return check_full_vec

    # public methods:
    def get_cost_current_tick(self):
        self._compute_cost_current_tick()
        return self.__cost_current_tick

    def get_overall_ticks(self):
        return self.__overall_ticks

    def update_overall_ticks(self):
        self.__overall_ticks = self.__overall_ticks + 1
        for s in range(0, len(self.__servers_list)):
            self.__servers_list[s].update_tick()

    def update_all_servers_status(self):
        ssize = len(self.__servers_list)
        if ssize > 0:
            for s in range(0, ssize):
                self.__servers_list[s].update_server_status()

    def reorganize_clients_in_servers(self):
        tot_num_conn_clients = 0
        if len(self.__servers_list) > 0:
            for s in range(0, len(self.__servers_list)):
                tot_num_conn_clients = tot_num_conn_clients + self.__servers_list[s].get_current_number_of_clients()
            optimum_number_of_servers = (tot_num_conn_clients / self.__umax) + (tot_num_conn_clients % self.__umax)
            if len(self.__servers_list) > optimum_number_of_servers:
                check_full_vec = self.__check_positions_from_servers_list()
                v = 0
                while v < len(check_full_vec) - 1:
                    if check_full_vec[v]['Full'] == False:
                        pos_to_insert = check_full_vec[v]['Pos']
                        for c in range(v + 1, len(check_full_vec)):
                            if check_full_vec[c]['Full'] == False:
                                pos_to_remove = check_full_vec[c]['Pos']
                                client = self.__servers_list[pos_to_remove].pop_smaller_hop_client()
                                self.__servers_list[pos_to_insert].append(client)
                        check_full_vec = self.__check_positions_from_servers_list()
                    v = v + 1

    def get_string_with_servers_and_clients(self):
        text_to_be_printed = ""
        if len(self.__servers_list) > 0:
            for s in self.__servers_list:
                assert (s, Server)
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
