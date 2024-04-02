import os
import python_supabase

## IDEA FOR FILE : Declare player objects when game begins, use these objects
## during the game and update supabase and graphics every interaction

class Player():
    def __init__(self, pID) -> None:
        ## take data from supabase
        playerID = pID
        hardwareID = -1 ## implement when we find out what this is
        codeName = python_supabase.Database.fetch_name(pID)
    
    def styleB(self) -> None:
        ## placeholder because idk where to find stylized B
        self.codeName = self.codeName + 'B'
        print("new codeName = {}".format(self.codeName))
        python_supabase.Database.update_data(self.playerID, self.codeName)



class GameInteractions():
    ## player hitting player parameters = (playerID of victim, playerID of shooter)
    def playerHit(ID1, ID2) -> None:
        return


    ## player hitting base
    def playerBase(ID) -> None:
        return