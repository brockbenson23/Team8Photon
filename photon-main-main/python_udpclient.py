import socket
import threading

print("in client")
localIP = "127.0.0.1"
serverAddressPort = (localIP, 7501)
bufferSize = 1024
broadcastPort = (localIP, 7500)


def sendMessage(clientMsg):
    UDPClientSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # transmit message
    bytesToSend = str.encode(clientMsg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print(f"clientMsg = {clientMsg}")


def receiveMessage(serverAddressPort):
    UDPClientSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # receive message
    UDPClientSocket.bind(("127.0.0.1", serverAddressPort))
    msgFromServer = str(UDPClientSocket.recvfrom(1024)[0])[2:-1]
    UDPClientSocket.close()
    return msgFromServer
