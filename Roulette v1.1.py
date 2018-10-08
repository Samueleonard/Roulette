#v1.1 of roulette. this a complete refactor of v1.0
#which was a complete mess. like, really bad.
#BUT it was functional so i am using it as a base
#wish me luck :) started 5/10/18

##################################
#imports
#import modules
import tkinter as tk
import random
import time
#import scripts
import board
import player
import game
##################################
#set up tkinter and sets window info
#creates window
root = board.root
#gives the window a title
root.title('Roulette v1.1 pre-beta')
#sets dimensions of window(TODO: make board wigets scale with window size AND make window work on different screen sizes)
root.geometry('700x500')
#adds buttons, colours, texts etc to the window
board.set_up_board_buttons()
board.set_up_board_texts()
board.set_up_board_circle()
##################################
