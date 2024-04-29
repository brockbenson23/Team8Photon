import socket
localIP = ""
receivePort = 7501
broadcastPort = 7500
bufferSize = 1024

class Socket:

    def __init__(self) -> None:
        # Setting up broadcast socket
        self.UDPBroadcastSocket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)
        self.UDPBroadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Create a datagram socket for receiving
        self.UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDPServerSocket.bind((localIP, receivePort))
        print("UDP server up and listening")

    def recvfrom(self):
        return self.UDPServerSocket.recvfrom(bufferSize)
    
    def transmitCode(self, code):
        bytesToSend = str.encode(code)
        self.UDPBroadcastSocket.sendto(bytesToSend, ('<broadcast>', broadcastPort))
        self.UDPBroadcastSocket.close()

    def transmitCode(self, code):
        bytesToSend = str.encode(code)
        self.UDPBroadcastSocket.sendto(bytesToSend, ('<broadcast>', broadcastPort))
        self.UDPBroadcastSocket.close()

    def transmitCode(self, code):
        bytesToSend = str.encode(code)
        self.UDPBroadcastSocket.sendto(bytesToSend, ('<broadcast>', broadcastPort))
        self.UDPBroadcastSocket.close()

def decipherMsg(self, serverMsg):
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
if __name__ == "__main__":
    s = Socket()
# Listen for incoming datagrams
while (True):
    bytesAddressPair = s.recvfrom()

    # deciper message
    serverMsg = str(bytesAddressPair[0])
    address = bytesAddressPair[1]  # may need to stringify
    print("Message from Client:{}".format(serverMsg))
    print("Client IP Address:{}".format(address))

    # separate message "1:2" into str1 = 1 and str2 = 2
    str1, str2 = decipherMsg(serverMsg)

    s.transmitCode(str1)



