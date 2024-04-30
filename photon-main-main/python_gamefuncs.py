import os
import python_supabase
import python_udpserver  # Import the UDP server module
import threading


def listen_for_messages():
    last_message = ''
    while True:
        try:
            # Receive a message from the server
            message = receive_message()
            if message is not None and message != last_message:
                print('in gamefuncs - message:', message)
                last_message = message
        except Exception as e:
            print("Error receiving message:", e)


def receive_message():
    global python_udpserver
    text = python_udpserver.received_message
    python_udpserver.received_message = ''
    if text == '':
        return text
    else:
        # split up b'str1:str2' into str1, str2
        colon = text.find(':')
        str1 = text[2:colon]  # starts at 2 because str1 starts with b'
        str2 = text[colon+1:-1]  # leaves out ' at the end
        if str2 == '53':
            print("red base has been scored in gamefuncs")
            Player.styleB(str1)
        elif str2 == '43':
            print("green base has been scored in gamefuncs")
            Player.styleB(str1)
        elif (str1 != '') and (str2 != ''):
            print("player with id {} has hit player with id {} in gamefuncs".format(str1, str2))
            Player.onHit(str1)
        return str1 + ':' + str2


class Team():
    points = 0
    # will initialize a green and red team

    def __init__(self) -> None:
        self.players = []

    def addPlayer(self, player) -> None:
        self.players.append(player)

    def print(self) -> None:
        for player in self.players:
            player.print()
            print("team has {} points".format(self.points))

    def updatePoints(self) -> None:
        for player in self.players:
            self.points += player.points

    def getPlayers(self):
        return self.players

class Player():
    points = 0

    def __init__(self, pID) -> None:
        # take data from supabase
        data = python_supabase.Database.fetch_playerData(pID)
        self.hasBase = data[0]['hasBase']
        self.playerID = pID
        self.equipmentID = data[0]['equipment_id']
        self.codeName = data[0]['codename']
        if ((int(pID) % 2) == 1):
            self.color = "RED"  # IF ID == ODD -> RED TEAM
        else:
            self.color = "GREEN"  # IF ID == EVEN -> GREEN TEAM

    def styleB(hID) -> None:
        playerdata = python_supabase.Database.HID_fetch_playerData(hID)
        if playerdata[0]['hasBase'] is False:
            print("player has hit base")
            python_supabase.Database.update_data(
                playerdata[0]['id'], "🅑 " + playerdata[0]['codename'], hID, True, playerdata[0]['points'])
        else:
            print("player has already hit base")

    def onHit(hID) -> None:
        playerdata = python_supabase.Database.HID_fetch_playerData(hID)
        print(f"player {playerdata} has hit opponent")
        python_supabase.Database.update_data(
            playerdata[0]['id'], playerdata[0]['codename'], hID, playerdata[0]['hasBase'], playerdata[0]['points'] + 10)

    def badOnHit(hID) -> None:
        playerdata = python_supabase.Database.HID_fetch_playerData(hID)
        print(f"player {playerdata} has hit teammate")
        python_supabase.Database.update_data(
            playerdata[0]['id'], playerdata[0]['codename'], hID, playerdata[0]['hasBase'], playerdata[0]['points'] - 10)


def start():
    print("in game funcs")
    server_thread = threading.Thread(
        target=python_udpserver.createSocket)
    server_thread.start()
    message_listener_thread = threading.Thread(
        target=listen_for_messages)
    message_listener_thread.start()
