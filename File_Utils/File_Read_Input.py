##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################


class FileReadInput:

    # constructor
    def __init__(self, filename):
        self.__filename = filename
        self.__list_of_inputs = self._compute_list_of_inputs

    # protected methods:
    def _compute_list_of_inputs(self):
        try:
            f = open(self.__filename, 'r')
            list_of_inputs = file.readlines()
            f.close()
        except IOError:
            print('The file %s could not be read' % self.__filename)
        return list_of_inputs

    # public methods
    def get_filename(self):
        return self.__filename

    def get_list_of_inputs(self):
        return self.__list_of_inputs
