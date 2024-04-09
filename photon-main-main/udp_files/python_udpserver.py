import socket

localIP = "127.0.0.1"
receivePort = 7502
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, receivePort))

print("UDP server up and listening")

# Listen for incoming messages
while(True):
   
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    equipmentCode = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(equipmentCode)
    clientIP  = "Client IP Address:{}".format(address)
   
    print(equipmentCode)
    print(clientIP)
