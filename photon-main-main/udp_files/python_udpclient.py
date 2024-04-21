import socket
from .. import python_supabase


print("in client")
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 7501)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def transmitEquipmentCode(equipmentCode):

    # Convert equipment code to string then encode in bytes
    ec = str(equipmentCode)
    bytesToSend = str.encode(ec)


def sendID(equipID): # equipID is the equipmentID of the player who got hit
    msgFromClient = str(equipID)
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
# # Receiving equipment ID from the server
# received_data, _ = UDPClientSocket.recvfrom(bufferSize)
# equipment_id = received_data.decode()
# print("Received Equipment ID:", equipment_id)
