import socket

print("in client")
localIP = "127.0.0.2"
serverAddressPort = (localIP, 7501)
bufferSize = 1024
broadcastPort = (localIP, 7500)

def sendMessage(bytePair0, bytePair1): 
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    # transmit message
    clientMsg = str(bytePair0) + ':' + str(bytePair1)
    bytesToSend = str.encode(clientMsg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print(f"clientMsg = {clientMsg}")
    
    # receive message
    UDPClientSocket.bind(broadcastPort)
    msgFromServer = str(UDPClientSocket.recvfrom(1024)[0])[2:-1]
    msg = "Message from Server {}".format(msgFromServer)
    UDPClientSocket.close()
    return msg


