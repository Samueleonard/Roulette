#this script is in charge of doing everything related to the game
#ie the back end(the dirty stuff)

import random #for the winning num
import board
import tkinter as tk
import player_data as pd

global amount_players
win_num = ''

def set_up_game(amnt):
    global amount_players
    amount_players = amnt #how many players are playing
    global turn_player
    turn_player = amnt #which player is currently having the turn

    print('game is set up')
    print('there is %s players playing and it is currently player %s turn to make a bet'% (amount_players, turn_player))

def gen_rand_int():
    board.spin_wheel_button.config(state=tk.DISABLED)
    global win_num #the number that will win the game
    win_num = str(random.randint(0,36))
    win_num = "1"
    print('the winning number is: ',win_num )
    board.set_circle_text(board.canvas)
    if win_num in pd.player1.bets:
        print("you won")
    

def turn_change(): # when the pass turn button is clicked
    #disables pass turn button
    board.pass_button.config(state = tk.DISABLED)
    #change the text of current player
    board.player_display.set("2 Player Mode : Player 2")
    #change the text of total chips to correct player
    board.chip_display.set("Total Player 2 Chips : " + str(pd.player2.total_chips))

#will run when 1 player or 2 player button is clicked
def def_plng_ply_amnt(amt): # define playing player amount(amount of players)
    if amt == 1:
        print("player 1 button clicked")
        global amount_players
        amount_players = 1
        board.P2_B.config(state = tk.NORMAL)
        board.P1_B.config(state = tk.DISABLED)
        board.pass_button.config(state = tk.DISABLED)
        board.player_display.set("Single Player Mode")
        board.chip_display.set("Total Player 1 Chips: " + str(pd.player1.total_chips))
    elif amt == 2:
        print("player 2 button clicked")
        amount_players = 2
        board.P1_B.config(state = tk.NORMAL)
        board.P2_B.config(state = tk.DISABLED)
        board.pass_button.config(state = tk.NORMAL)
        board.player_display.set("2 Player Mode : Player 1")
    set_up_game(amount_players)            

def spin_wheel():
    if len(pd.player1.bets) == 0 and len(pd.player2.bets) == 0:
        print("you cant do this, you need to place some bets first.")
        return
    else:
        board.spin_wheel_button.config(state=tk.DISABLED)
        gen_rand_int()

