##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################

from uuid import uuid4
from time import strftime


class Client:

    # constructor:
    def __init__(self):
        self.__hash_code = self._generate_hash_code()
        self.__hops = 0
        self.__date_of_creation = strftime("%Y-%m-%d--%H-%M-%S")

    # public methods:
    def increase_hop(self):
        self.__hops = self.__hops + 1

    def get_current_hop(self):
        return self.__hops

    def get_hash_code(self):
        return self.__hash_code

    # protected and static methods:
    @staticmethod
    def _generate_hash_code(self):
        code = str(uuid4().hex)
        return code