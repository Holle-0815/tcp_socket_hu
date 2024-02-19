#!/usr/bin/env python3

from datetime import datetime
import socket
import sys
import os

#Parameter
TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2])
BUFFER_SIZE = 1024
argument = sys.argv[3]

PFAD = sys.path[0]
file_name = "messages.txt"
path_file = os.sep.join([PFAD, file_name])

file = open(path_file, 'a+')

MESSAGE = str.encode(argument)

#file.write( datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' )
file.write( '--------------> Start Session ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((TCP_IP, TCP_PORT))
    file.write( datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' )
    file.write( 'Connected to ' + TCP_IP +' / ' + str(TCP_PORT) + '\n' )

    s.send(MESSAGE)
    file.write( datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' )
    file.write( 'Send ' + argument + '\n' )
    
    s.close()
    file.write( datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' )
    file.write( 'Closed connection to ' + TCP_IP +' / ' + str(TCP_PORT) + '\n' )
except: 
    file.write( datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' )
    file.write( 'Error ' + str( sys.exc_info()[0] ) + '\n' )
    file.write( 'Not Send ' + argument + '\n' )
    #print("Error:", sys.exc_info()[0]) 

file.write( '<------------- End Session ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
file.close()
