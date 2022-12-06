from OSLogManagement import os_log_parameters, show_last_log

if __name__ == '__main__':
    listado = os_log_parameters('ipconfig', regex_function='search', regex_parameters='Address IPv4.+: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', show_log=True)
    string = ''.join(listado) # lista a string
    print(listado)
    print(string)
    show_last_log()