import socket

print("in client")
serverAddressPort = ("127.0.0.1", 7501)
#bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

## expecting  equipment code
#equipID = UDPClientSocket.recvfrom(1024)[0]

def sendMessage(bytePair0, bytePair1): # equipID is the equipmentID of the player who got hit
    # transmit message
    clientMsg = str(bytePair0) + ':' + str(bytePair1)
    bytesToSend = str.encode(clientMsg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    # receive message
    msgFromServer = str(UDPClientSocket.recvfrom(1024)[0])[2:-1]
    msg = "Message from Server {}".format(msgFromServer)
    print(msg)


sendMessage(5556, 43)

