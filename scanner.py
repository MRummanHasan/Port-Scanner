#!/bin/python3


import sys
import socket
from datetime import datetime
from unittest import result

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #ranslate hostname to IPV4
else:
    print("Invalid amount of arguments.")
    print("Syntax: pyhon3 scanner.py <ip>")

#Add a banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
        for port in range(50,85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) #wait for 1 second for port to respond
            result = s.connect_ex((target,port)) #return error indicator
            if result == 0:
                print("Port {} is open". format(port))
            s.close()

except KeyboardInterrupt:
    print("\nExiting program on user input")
    sys.exit()
except socket.gaierror:
    print("HOstname could not be resolved")
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()


#python3 scanner.py <ip>








"""
from cgitb import Hook
import imp
from socket import socket
import socket
HOST = '127.0.0.1'
PORT = 777
#ipv4 conn, port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
"""