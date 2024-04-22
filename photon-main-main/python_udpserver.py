import socket
import python_gamefuncs

localIP = "127.0.0.1"
receivePort = 7501
broadcastPort = 7500
bufferSize = 1024



# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, receivePort))

print("UDP server up and listening")

def transmitID(equipID): # call this method after receiving equipID from player screen
    serverMsg = equipID
    bytesToSend = str.encode(serverMsg)
    UDPServerSocket.sendto(bytesToSend, broadcastPort)

# Listen for incoming datagrams
while (True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    serverMsg = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(serverMsg)
    clientIP = "Client IP Address:{}".format(address)

    # separate message "1:2" into str1 = 1 and str2 = 2
    colon = serverMsg.find(':')
    str1 = serverMsg[:colon]
    str2 = serverMsg[colon:]

    # check whether str2 is a base hit or an equipmentID

    if str2 == '53':
        print("red base has been scored")
    elif str2 == '43':
        print("green base has been scored")
    else:
        print("player with id {} has hit player with id {}".format(str1, str2))



    print(serverMsg)
    print(clientIP)


    
