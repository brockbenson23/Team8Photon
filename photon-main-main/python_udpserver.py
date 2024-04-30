import socket
import selectors
localIP = ""
receivePort = 7501
broadcastPort = 7500
bufferSize = 1024
UDPBroadcastSocket = None
UDPServerSocket = None
received_message = None

# set up selector
sel = selectors.DefaultSelector()


def transmitCode(code):
    global UDPBroadcastSocket
    print('in transmit: ', code)
    bytesToSend = str.encode(code)
    bytes_sent = UDPBroadcastSocket.sendto(
        bytesToSend, ('127.0.0.1', broadcastPort))
    if bytes_sent == len(bytesToSend):
        print("Broadcast successful")
    else:
        print("Broadcast failed")

def receive(sock, mask):
    global received_message
    serverMsg = str(sock.recvfrom(1024)[0])
    str1, str2 = decipherMsg(serverMsg)
    # answer client
    transmitCode(str2)
    received_message = serverMsg

def decipherMsg(serverMsg):
    colon = serverMsg.find(':')
    str1 = serverMsg[2:colon]  # starts at 2 because str1 starts with b'
    str2 = serverMsg[colon+1:-1]  # leaves out ' at the end

    # check whether str2 is a base hit or an equipmentID
    if str2 == '53':
        print("red base has been scored")
    elif str2 == '43':
        print("green base has been scored")
    elif (str1 != '') and (str2 != ''):
        print("player with id {} has hit player with id {}".format(str1, str2))
    return str1, str2

def createSocket():
    global UDPBroadcastSocket
    global UDPServerSocket
    localIP = '127.0.0.1'

    # Set up broadcast socket
    UDPBroadcastSocket = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM)
    UDPBroadcastSocket.setsockopt(
        socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Set up receive socket
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, receivePort))
    UDPServerSocket.setblocking(False)

    # Setting up selector stuff
    sel.register(UDPServerSocket, selectors.EVENT_READ, receive)
    print("UDP server up and listening")

    while True:
        # if graphics needs to send code, s.transmitCode will be called?
        print('in while loop')
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)
