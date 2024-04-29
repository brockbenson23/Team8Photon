import socket
import errno


def transmitCode(code):
    bytesToSend = str.encode(code)
    UDPBroadcastSocket.sendto(bytesToSend, ('<broadcast>', broadcastPort))
    UDPBroadcastSocket.close()


def Start():
    localIP = ""
    receivePort = 7501
    broadcastPort = 7500
    bufferSize = 1024

# Setting up broadcast socket
    UDPBroadcastSocket = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM)
    UDPBroadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Create a datagram socket for receiving
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, receivePort))

    print("UDP server up and listening")

    def transmitCode(code):
        bytesToSend = str.encode(code)
        UDPBroadcastSocket.sendto(bytesToSend, ('<broadcast>', broadcastPort))
        UDPBroadcastSocket.close()

    def decipherMsg(serverMsg):
        colon = serverMsg.find(':')
        str1 = serverMsg[2:colon]  # starts at 2 because str1 starts with b'
        str2 = serverMsg[colon+1:-1]  # leaves out ' at the end

        print(f"str1 = {str1}")
        print(f"str2 = {str2}")
        # check whether str2 is a base hit or an equipmentID
        if str2 == '53':
            print("red base has been scored")
        elif str2 == '43':
            print("green base has been scored")
        else:
            print("player with id {} has hit player with id {}".format(str1, str2))

        return str1, str2

# Listen for incoming datagrams
    while (True):

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        # deciper message
        serverMsg = str(bytesAddressPair[0])
        address = bytesAddressPair[1]  # may need to stringify
        clientMsg = "Message from Client:{}".format(serverMsg)
        clientIP = "Client IP Address:{}".format(address)
        # separate message "1:2" into str1 = 1 and str2 = 2
        str1, str2 = decipherMsg(serverMsg)

        transmitCode(str1)


if __name__ == "__main__":
    Start()
