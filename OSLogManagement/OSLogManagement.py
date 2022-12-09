"""
  ____              _______ _   ______ _       ___ __    __
 |  _ \            /__   __(_)/__   __(_) _ __|_| |\ \\  / /
 | |_) |_   _         | |   _    | |   _ | '__| | | \ \\/ /
 |  _ <| | | |        | |  | |   | |  | || |    | |  \  \\
 | |_) | |_| |        | |  | |   | |  | || |    | | / /\ \\
 |____/ \__, |        |_|  |_|   |_|  |_||_|    |_|/_/  \_\\
         __/ |                                               
        |___/
"""

import os, re
import logging

logging.basicConfig(level=logging.INFO)

def os_log_parameters(os_command:str, regex_function:str, regex_parameters:str, export_log=True):
    """Allows you to use regular expressions to extract specific information from the log resulting from os.system() and store it in variables.

    Args:
        os_command (str): OS command to execute
        regex_function (str): 'findall', 'search', 'split', 'sub'
        regex_parameters (str): parameters to execute.

    Returns:
        list: Returns the output of regex.
    """

    assert regex_function in ['findall', 'search', 'split', 'sub'], f"No permitido regex_function '{regex_function}' \nValores válidos: 'findall', 'search', 'split', 'sub'"
    
    if export_log:
        os.system(f'{os_command} > ./last_log.txt')

    if regex_function == 'findall':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output
        

    elif regex_function == 'search':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output

    elif regex_function == 'split':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output

    elif regex_function == 'sub':
        temp_log = open('./last_log.txt', 'r')
        regex_output = re.findall(regex_parameters, temp_log.read())
        return regex_output

def show_last_log():
    """_summary_
    It is useful for copying special characters (which do not load in your text editor) and using them in regex parameters.
    """
    temp_log = open('./last_log.txt', 'r')
    logging.info(temp_log.read())
    temp_log.close()
    
