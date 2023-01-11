# README.md

Warning (bug not fixed): The LogManagemet package exports the terminal log in an unencrypted last_log.txt file, so it is exposed to plaintext in cases of forensic data recovery.

Designed to create variables with results that you can obtain by filtering the log that your terminal gives you by OS commands.  

Instalation:
pip install OSLogManagement

    >>> from LogManagement import os_commands_regex
    >>> ip_adress = os_commands_regex(os_command='ipconfig', regex_function='search', regex_parameters='IP Address.+: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    >>> print(ip_adress)
    ['192.168.0.101']

    # convert list to string:
    >>> ip =''.join(ip_adress)
    >>> print(ip)
    192.168.0.101


show_last_log()
    """_summary_
    It is useful for copying special characters (which do not load in your text editor) and using them in regex parameters.
    example:
    
    >>> from LogManagement import show_last_log
    >>> show_last_log()
    INFO:root:
    Configuraci¢n IP de Windows

    Adaptador de LAN inal mbrica Wi-Fi:

       Sufijo DNS espec¡fico para la conexi¢n. . : home
       Direcci¢n IPv6 . . . . . . . . . . : 444:444:444:4444:4444:4444:4444:4444
       Direcci¢n IPv6 . . . . . . . . . . : 333:333:333::3
       Direcci¢n IPv6 . . . . . . . . . . : 333:333:333::3
       V¡nculo: direcci¢n IPv6 local. . . : 222::222:222:222:222%2
       Direcci¢n IPv4. . . . . . . . . . . . . . : 192.168.1.2
       M scara de subred . . . . . . . . . . . . : 111.111.111.111
       Puerta de enlace predeterminada . . . . . : 1111:1111:d1::a11f:c11a
                                           

    >>>>>> ip_adress = os_commands_regex(os_command='ipconfig', regex_function='search', regex_parameters='Direcci¢n IPv4.+: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    >>> print(ip_adress)
    ['192.168.1.2']
    """
    
Warning (bug not fixed):
The LogManagemet package exports the terminal log in an unencrypted last_log.txt file, so it is exposed to plaintext in cases of forensic data recovery.


Useful content:

- regex101.com -> build, test and debug regex

- Tutorial práctico REGEX en español: https://www.youtube.com/watch?v=Mc2j8Q-MHB4&ab_channel=ThePyCoach -> credits: The PyCoach 

- Generate regex code with ChatGPT: https://chat.openai.com/

