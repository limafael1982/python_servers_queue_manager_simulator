##########################################
# Author: Rafael Lima
# Date of Creation: Friday, July 6 2018
##########################################

from Classes.Servers_Manager import ServersManager
from File_Utils.File_Read_Input import FileReadInput

INPUTFILEPATH = 'resources/others/input1.txt'
OUTPUTFILEPATH = 'resources/others/output_from_input1.txt'
TTASK = 5
UMAX = 10

fsimul = FileReadInput(INPUTFILEPATH, OUTPUTFILEPATH)
sm = ServersManager(TTASK, UMAX)

list_of_inputs = fsimul.get_list_of_inputs()
tick = 0
pricing = 0
for input_from_file in list_of_inputs:
    tick = tick + 1
    sm.remove_server_from_list_if_has_no_client()
    sm.add_input_clients_to_server_set(input_from_file)
    fsimul.write_text_to_output(sm.get_string_with_servers_and_clients() + '\n')
    print('[Tick %d] ==> %s' %(tick, sm.get_string_with_servers_and_clients()))
    pricing = sm.get_overall_cost()
    sm.reorganize_clients_in_servers()
    sm.remove_server_from_list_if_has_no_client()
    sm.update_overall_ticks()
    sm.update_all_servers_status()

print('\nBill: %d dollars. ' % pricing)




