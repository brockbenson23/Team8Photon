import os
import python_supabase

## IDEA FOR FILE : Declare player objects when game begins, use these objects
## during the game and update supabase and graphics every interaction
class Team():
    points = 0
    ## will initialize a green and red team
    def __init__(self, color) -> None:
        self.players = []
        self.color = color
    
    def addPlayer(self, player) -> None:
        self.players.append(player)

class Player():
    points = 0
    def __init__(self, pID) -> None:
        ## take data from supabase
        self.playerID = pID
        self.hardwareID = -1 ## implement when we find out what this is
        self.codeName = python_supabase.Database.fetch_name(pID)
        if ((pID % 2) == 1): self.color = "RED" ## IF ID == ODD -> RED TEAM
        else: self.color = "GREEN" ## IF ID == EVEN -> GREEN TEAM
    
    def styleB(self) -> None:
        ## placeholder because idk where to find stylized B
        self.codeName = self.codeName + 'B'
        print("new codeName = {}".format(self.codeName))
        python_supabase.Database.update_data(self.playerID, self.codeName)



class GameInteractions():
    ## player is person who hit someone
    def playerHit(player, team) -> None:
        team.points += 10
        player.points += 10
        return


    ## player hitting base
    def playerBase(player, team) -> None:
        player.styleB()
        team.points += 0 ## PLUG IN POINTS WHEN YOU FIND OUT HOW MANY THEY GET PER BASE
        return