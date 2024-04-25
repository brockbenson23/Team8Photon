import socket

print("in client")
serverAddressPort = ("127.0.0.1", 7501)
# bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocketTransmit = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("after socket")

def broadcastID(id):
    print('in broadcast')
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Enable broadcasting on the socket
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Define the broadcast address
    broadcast_address = ('<broadcast>', 7500)

    try:
        # Send the message to the broadcast address
        udp_socket.sendto(id.encode(), broadcast_address)
        print("Message sent successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the socket
        udp_socket.close()

# expecting  equipment code
# equipID = UDPClientSocket.recvfrom(1024)[0]


def sendMessage(bytePair0, bytePair1):  # equipID is the equipmentID of the player who got hit
    # transmit message
    clientMsg = str(bytePair0) + ':' + str(bytePair1)
    bytesToSend = str.encode(clientMsg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    # receive message
    msgFromServer = str(UDPClientSocket.recvfrom(1024)[0])[2:-1]
    msg = "Message from Server {}".format(msgFromServer)
    print(msg)

print('before sendmessage')
print('leaving client')
