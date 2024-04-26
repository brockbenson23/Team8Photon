import socket
import python_gamefuncs

localIP = "127.0.0.1"
receivePort = 7501
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, receivePort))

print("UDP server up and listening")


def transmitID(ID, address):  # call this method after receiving equipID from player screen
    serverMsg = ID
    bytesToSend = str.encode(serverMsg)
    UDPServerSocket.sendto(bytesToSend, address)


# Listen for incoming datagrams
while (True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    serverMsg = str(bytesAddressPair[0])
    address = bytesAddressPair[1]  # may need to stringify
    clientMsg = "Message from Client:{}".format(serverMsg)
    clientIP = "Client IP Address:{}".format(address)

    # separate message "1:2" into str1 = 1 and str2 = 2
    colon = serverMsg.find(':')
    str1 = serverMsg[2:colon]  # starts at 2 because str1 starts with b'
    str2 = serverMsg[colon+1:-1]  # leaves out ' at the end

    print(f"str1 = {str1}")
    print(f"str2 = {str2}")
    # check whether str2 is a base hit or an equipmentID
    if str2 == '53':
        print("red base has been scored")
        python_gamefuncs.Player.styleB(str1)
    elif str2 == '43':
        print("green base has been scored")
        python_gamefuncs.Player.styleB(str1)
    else:
        # checks if players are on same team
        if ((int(str1) % 2 == 1) and (int(str2) % 2 == 1)) or ((int(str1) % 2 == 0) and (int(str2) % 2 == 0)):
            match int(str1) % 2:  # ^^ check which team player is on, badOnHit means they hit a teammate and onHit means they hit an opposing player
                case 0:
                    python_gamefuncs.Player.badOnHit(str1)
                case 1:
                    python_gamefuncs.Player.badOnHit(str1)
        else:
            match int(str1) % 2:
                case 0:
                    python_gamefuncs.Player.onHit(str1)
                case 1:
                    python_gamefuncs.Player.onHit(str1)
        print("player with id {} has hit player with id {}".format(str1, str2))

    # respond to client
    transmitID(str1, address)
