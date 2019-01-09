import player_data as pd

"""
i press 1, it adds 1 to my bets list and . when i press spin wheel, it checks to see if the bet is in the list.
if it is, it gives me money, if not, it subtracts money


"""


def ButtonPressed(text):
    print(text)
    #pd.player1.bets.append(str(text))
    #print(pd.player1.bets)

def reset_bets():
    pd.player1.bets = []
    pd.player.special_bets = []
    pd.player2.bets = []
    pd.player2.special_bets = []
    print(pd.player1.bets)
    print("bets have been reset")
