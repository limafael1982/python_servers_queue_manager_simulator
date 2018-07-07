##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################


class FileReadInput:

    # constructor
    def __init__(self, input_filename, output_filename):
        self.__input_file_name = input_filename
        self.__output_filename = output_filename
        self.__list_of_inputs = self._compute_list_of_inputs

    # protected methods:
    def _compute_list_of_inputs(self):
        try:
            f = open(self.__input_file_name, 'r')
            list_of_inputs = f.readlines()
            f.close()
        except IOError:
            print('The file %s could not be read' % self.__input_file_name)
        return list_of_inputs

    # public methods
    def get_input_filename(self):
        return self.__input_file_name

    def get_list_of_inputs(self):
        return self.__list_of_inputs

    def write_text_to_output(self, text):
        try:
            f = open(self.__output_filename, 'a+')
            f.write(text + '\n\r')
            f.close()
        except IOError:
            print('The file %s could not be written' % self.__output_filename)
