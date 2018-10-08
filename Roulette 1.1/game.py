#this script is in charge of doing everything related to the game
#ie the back end(the dirty stuff)

import random #for the winning num
import board
import tkinter as tk

global amount_players
win_num = ''

def set_up_game(amnt):
    global amount_players
    amount_players = 1 #how many players are playing
    global turn_player
    turn_player = 1 #which player is currently having the turn

    print('game is set up')
    print('there is %s players playing and it is currently player %s turn to make a bet'% (amount_players, turn_player))

def gen_rand_int():
    global win_num #the number that will win the game
    win_num = str(random.randint(0,36))
    print('the winning number is: ',win_num )
    board.set_circle_text(board.canvas)

def turn_change(): # when the pass turn button is clicked
    if amount_players == 1: # if there is only 1 player playing
        pass # do nothing
    else: # if it is a 2 player game
        if turn_player == 1: # if it is player 1 turn
            turn_player += 1 # sets current player to player 2
            board.player_display.set("Player 2")
            #chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))
        else:
            turn_player = 1 # sets current player to player 1
            board.player_display.set("Player 1")
            #chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))

#will run when 1 player or 2 player button is clicked
def def_plng_ply_amnt(amt): # define playing player amount(amount of players)
    if amt == 1:
        global amount_players
        amount_players = 1
        board.P2_B.config(state = tk.NORMAL)
        board.P1_B.config(state = tk.DISABLED)
        board.pass_button.config(state = tk.DISABLED)
        board.player_display.set("Single Player Mode")
        #chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))
    elif amt == 2:
        amount_players = 2
        board.P1_B.config(state = tk.NORMAL)
        board.P2_B.config(state = tk.DISABLED)
        board.pass_button.config(state = tk.NORMAL)
        board.player_display.set("2 Player Mode")
    else:
        tk.messagebox.showError('ERROR IN GAME.PY. i dont know how you have got to this point to be honest.')
    set_up_game(amount_players)            

def spin_wheel():
    gen_rand_int()
    #board.spin_wheel_button.config(state=tk.DISABLED)DOESNT WORK, SHOULD DISABLE BUTTON AFTER CLICKED
