import socket

print("in client")
print("in client")
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 7501)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def broadcastID(id):
    print('in broadcast')
    ec = str(id)
    bytesToSend = str.encode(ec)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)


def sendMessage(bytePair0, bytePair1):
    # transmit message
    clientMsg = str(bytePair0) + ':' + str(bytePair1)
    bytesToSend = str.encode(clientMsg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    # receive message (if needed)
    # msgFromServer = str(UDPClientSocket.recvfrom(1024)[0])[2:-1]
    # msg = "Message from Server {}".format(msgFromServer)
    # print(msg)


print('before sendmessage')
print('leaving client')
