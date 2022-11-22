'''
Created by Calvin Long z5255352 (UNSW)
How to use DER_device.py

Start a DER_master server to accept all the connections

then run:

python3 DER_device.py Address_of_server Port_of_server number_of_devices

e.g.

python3 DER_device.py 127.0.0.1 1234 10

This will automatically connect 10 der devices to DER_master server running
'''


from socket import *
import sys
from threading import Thread
import time
import numpy as np
import matplotlib.pyplot as plt

NUM_SIN = 20

out_array = np.sin(np.linspace(-np.pi, np.pi, NUM_SIN))

'''
Stored in the format
actual_data[
    {
        actual_num: #,
        actual_values: []
    },
    ...
]
'''
actual_data = []
clients = []


class ClientThread(Thread):
    def __init__(self, clientSocket, serverAddress, client_num):
        Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientSocket.connect(serverAddress)
        self.clientAlive = True
        self.client_num = client_num
        clients.append(self)

    def run(self):
        counter = 0
        start_time = time.time()
        while self.clientAlive:
            time.sleep(0.5)
            self.communicate(str(out_array[counter]+float(self.client_num)))
            for i in actual_data:
                if i['actual_num'] == self.client_num:
                    i['actual_values'].append(out_array[counter]+float(self.client_num))
            counter = (counter + 1) % NUM_SIN

            if time.time() - start_time > 10:
                self.clientAlive = False

        clients.remove(self)
        self.clientSocket.close()

    def communicate(self, message):
        self.clientSocket.send((str(self.client_num)+ ' ' + message).encode())

    def display_info(self, info):
        print('Client ' + str(self.client_num) + ': ' + info)

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
number_devices = int(sys.argv[3])

serverAddress = (serverHost, serverPort)

for i in range(0, number_devices):
    client_com = ClientThread(socket(AF_INET, SOCK_STREAM), serverAddress, i)
    client_com.start()
    actual_data.append({
        'actual_num': i,
        'actual_values': []
    })

while len(clients) > 0:
    time.sleep(1)

for i in actual_data:
    plt.plot([x for x in range(0, len(i['actual_values']))], i['actual_values'], label="Actual "+str(i['actual_num']))

plt.xlabel('num entries')
plt.ylabel('value')

plt.title('Actual values output by DER devices')

plt.legend()

plt.show()