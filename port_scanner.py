#!usr/bin/python3

import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host= input("Please enter the IP:")
port=int(input("Please enter the port:"))

def PortScanner(port):
    if s.connect_ex((host, port)):
        print("the port is closed")
    else:
        print("The port is open")

PortScanner(port)
