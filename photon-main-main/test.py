import python_supabase
import python_gamefuncs

def test() -> None:
    print("it works")
    testplayer = python_gamefuncs.Player(42069)
    testteam = python_gamefuncs.Team("RED")
    testteam.addPlayer(testplayer)
    print("codename before B is {}".format(testplayer.codeName))
    testplayer.styleB()
    print("codename after B is {}".format(testplayer.codeName))

    print("team name is {}".format(testplayer.team))
    print("player has {} points".format(testplayer.points))
    print("team has {} points".format(testteam.points))
    python_gamefuncs.GameInteractions.playerHit(testplayer, testteam)
    print("player has {} points".format(testplayer.points))
    print("team has {} points".format(testteam.points))
    
    pass
    