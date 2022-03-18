# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:17:08 2022

@author: User
"""

import socket

HOST = '127.0.0.1'
PORT = 8081

server = socket.socket()
server.bind((HOST,PORT))
print("server started")
print("listening for client connection")

server.listen(1)
client,client_add = server.accept()
print("client " , client_add , "connected to the server")

while True:
    command = input("Enter command ")
    command = command.encode()
    client.send(command)
    print("command sent")
    output = client.recv(1024)
    output = output.decode()
    print("output is " , output)