'''
Created by Calvin Long z5255352 (UNSW)
How to use DER_device.py

Start a DER_master server to accept all the connections

then run:

python3 DER_sus.py Address_of_server Port_of_server num_clients

e.g.

python3 DER_sus.py 127.0.0.1 1234

This will automatically connect 10 der devices to DER_master server running
'''

from socket import *
import sys
from threading import Thread
import time
import numpy as np

NUM_SIN = 20

out_array = np.sin(np.linspace(-np.pi, np.pi, NUM_SIN))

class ClientThread(Thread):
    def __init__(self, clientSocket, serverAddress, num_devices):
        Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientSocket.connect(serverAddress)
        self.clientAlive = True
        self.num_devices = num_devices

    def run(self):
        start_time = time.time()
        counter = 0
        while self.clientAlive:

            self.communicate(counter, str(out_array[counter]+float(10)))
            counter += 1
            time.sleep(10/self.num_devices)
            
            if time.time() - start_time > 10:
                self.clientAlive = False

        self.clientSocket.close()

    def communicate(self, client_num ,message):
        self.clientSocket.send((str(client_num)+ ' '+ message).encode())

    def display_info(self, info):
        print('Client ' + str(self.client_num) + ': ' + info)

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
number_devices = int(sys.argv[3])

serverAddress = (serverHost, serverPort)

client_com = ClientThread(socket(AF_INET, SOCK_STREAM), serverAddress, number_devices)
client_com.start()