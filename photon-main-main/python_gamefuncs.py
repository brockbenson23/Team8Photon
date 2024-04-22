import os
import python_supabase

class Team():
    points = 0
    ## will initialize a green and red team
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

class Player():
    points = 0
    def __init__(self, pID) -> None:
        ## take data from supabase
        data = python_supabase.Database.fetch_playerData(pID)
        self.hasBase = data[0]['hasBase']
        self.playerID = pID
        self.equipmentID = data[0]['equipment_id']
        self.codeName = data[0]['codename']
        if ((int(pID) % 2) == 1): self.color = "RED" ## IF ID == ODD -> RED TEAM
        else: self.color = "GREEN" ## IF ID == EVEN -> GREEN TEAM
    
    def styleB(pID) -> None:
        playerdata = python_supabase.Database.fetch_playerData(pID)
        if playerdata[0]['hasBase'] == False:
            print("player has hit base")
            python_supabase.Database.update_data(pID, "B " + playerdata[0]['codename'], playerdata[0]['equipment_id'], True, playerdata[0]['points'])
        else:
            print("player has already hit base")   

    def onHit(pID) -> None:
        playerdata = python_supabase.Database.fetch_playerData(pID)
        print("player has hit opponent")
        python_supabase.Database.update_data(pID, playerdata[0]['codename'], playerdata[0]['equipment_id'], playerdata[0]['hasBase'], playerdata[0]['points'] + 10)

    def badOnHit(pID) -> None:
        playerdata = python_supabase.Database.fetch_playerData(pID)
        print("player has hit teammate")
        python_supabase.Database.update_data(pID, playerdata[0]['codename'], playerdata[0]['equipment_id'], playerdata[0]['hasBase'], playerdata[0]['points'] - 10)

