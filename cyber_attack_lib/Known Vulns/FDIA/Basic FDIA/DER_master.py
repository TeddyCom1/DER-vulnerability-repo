'''
Created by Calvin Long z5255352 (UNSW)

How to use DER_master.py

python3 DER_master.py ip_address Server_port num_connections

e.g.

python3 DER_master.py 127.0.0.1 8081 10

This code will wait for in comming connections and display the data obtained from the Devices 
'''

from cProfile import label
from pydoc import cli
from socket import *
from threading import Thread
import sys
import matplotlib.pyplot as plt
import time

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
num_connections = int(sys.argv[3])
serverAddress = (serverHost, serverPort)

# define socket for the server side and bind address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)


clients = []


'''
Stored in the format
client_data[
    {
        client_num: #,
        client_values: []
    },
    ...
]
'''
client_data = []

class ClientThread(Thread):
    def __init__(self, clientAddress, clientSocket):
        Thread.__init__(self)
        self.clientAddress = clientAddress
        self.clientSocket = clientSocket
        self.clientAlive = True
        clients.append(self)
        

    def run(self):
        data = ''
        while self.clientAlive:
            try:
                data = self.read_data()
            except timeout as e:
                continue
            
            if data == '':
                self.clientAlive = False
                break

            self.display_data(data)
            self.store_data(data)

        clients.remove(self)

    def display_data(self, data):
        print(data)

    def store_data(self,data):
        split = data.split(' ')
        for i in client_data:
            if int(split[0]) == i['client_num']:
                i['client_values'].append(float(split[1]))

    def read_data(self):
        data = self.clientSocket.recv(1024)
        data = data.decode()
        data = data.rstrip('\n')
        return data

print("\n===== Server is running =====")
print("===== Waiting for connection request from clients...=====")

for i in range(0, num_connections):
    client_data.append({
        'client_num': i,
        'client_values': []
    })

for i in range(0, num_connections):
    serverSocket.listen()
    clientSockt, clientAddress = serverSocket.accept()
    clientThread = ClientThread(clientAddress, clientSockt)
    clientThread.start()
    
while len(clients) > 0:
    time.sleep(1)

for i in client_data:
    plt.plot([x for x in range(0, len(i['client_values']))], i['client_values'], label="Client "+str(i['client_num']))

plt.xlabel('num entries')
plt.ylabel('value')

plt.title('DER connection sim MASTER')

plt.legend()

plt.show()