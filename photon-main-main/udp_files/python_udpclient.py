import socket

print("in client")
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 7500)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def transmitEquipmentCode(equipmentCode):

    # Convert equipment code to string then encode in bytes
    ec = str(equipmentCode)
    bytesToSend = str.encode(ec)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
