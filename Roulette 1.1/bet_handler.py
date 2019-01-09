import player_data as pd
import board
"""
i press 1, it adds 1 to my bets list and . when i press spin wheel, it checks to see if the bet is in the list.
if it is, it gives me money, if not, it subtracts money


"""
root = board.root

def ButtonPressed(rw,col):
    widget = root.grid_slaves(row=int(rw),column=int(col))[0]
    a = widget['text']
    pd.player1.bets.append(str(a))

    #print(pd.player1.bets)

def reset_bets():
    pd.player1.bets = []
    pd.player.special_bets = []
    pd.player2.bets = []
    pd.player2.special_bets = []
    print(pd.player1.bets)
    print("bets have been reset")
