#!/usr/bin/env python3

import socket
import sys
import os

#Parameter
TCP_IP = '127.0.0.1' # '10.182.217.108.'
TCP_PORT = 1234 #8181
BUFFER_SIZE = 1024
#argument = sys.argv[1]
argument = "Data;22391021099H23;52345235235;13;5;"

#file_name = "C:\Users\wagnerho\Documents\Python\message.txt"

# 
PFAD = sys.path[0]
file_name = "messages.txt"
path_file = os.sep.join([PFAD, file_name])

print( PFAD)
print( file_name)
print( path_file )
file = open(path_file, 'a+')

MESSAGE = str.encode(argument)

file.write( argument )
file.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#message_file.write( argument )
print ("Übergebene Daten:", argument)

try:
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
#data = s.recv(BUFFER_SIZE)
#print ("receiver data:", data)
    s.close()
except: 
    print("Connect Fehler:", sys.exc_info()[0]) 
    

    



'''
KUNDENMATERIAL = sys.argv[1]
HANDLINGUNIT = sys.argv[2]
SOLLMENGE = sys.argv[3]
ISTMENGE = sys.argv[4]
'''