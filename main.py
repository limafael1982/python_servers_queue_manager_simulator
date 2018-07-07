##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################

from Classes.Servers_Manager import ServersManager
from File_Utils.File_Read_Input import FileReadInput

INPUTFILEPATH = 'resources/others/input_testing.txt'
OUTPUTFILEPATH = 'resources/others/output_testing.txt'

fsimul = FileReadInput(INPUTFILEPATH, OUTPUTFILEPATH)
sm = ServersManager()

list_of_inputs = fsimul.get_list_of_inputs()

for input_from_file in list_of_inputs:
    sm.reorganize_clients_in_servers()
    sm.add_input_clients_to_server_set(input_from_file)
    sm.update_overall_ticks()
    sm.update_all_servers_status()
    fsimul.write_text_to_output(sm.get_string_with_servers_and_clients())



