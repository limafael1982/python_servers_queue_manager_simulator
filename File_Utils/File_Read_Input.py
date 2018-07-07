##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################


class FileReadInput:

    # constructor
    def __init__(self, input_filename, output_filename):
        self.__input_file_name = input_filename
        self.__output_filename = output_filename

    # public methods
    def get_input_filename(self):
        return self.__input_file_name

    def get_list_of_inputs(self):
        list_of_inputs = []
        try:
            f = open(self.__input_file_name, 'r')
            list_of_inputs_str = f.readlines()
            f.close()
        except IOError:
            print('The file %s could not be read' % self.__input_file_name)
        for l in list_of_inputs_str:
            list_of_inputs.append(int(l))
        return list_of_inputs

    def write_text_to_output(self, text):
        try:
            f = open(self.__output_filename, 'a+')
            f.write(text + '\n\r')
            f.close()
        except IOError:
            print('The file %s could not be written' % self.__output_filename)
