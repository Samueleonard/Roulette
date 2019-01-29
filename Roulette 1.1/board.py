#this script handles all dealings with the board. it will set up the layout of the board(draw all buttons).

import tkinter as tk
root = tk.Tk()
import game
import bet_handler

#sets up numbers and colours
def set_up_board_buttons():

    print('setting up the buttons on the board')                                                                                                      

    row = 0 #row in comparison to the board
    rw = 1 #row in comparison to buttons
    col = 0

    tk.Button(text="0",bg="green",fg="white",padx=10, pady=54, command=lambda: bet_handler.ButtonPressed(0)).grid(rowspan=3, row=1, column=1)#0 button                 

#row 1
    for z in range(9):
        tk.Button(root,text=col+1,bg="red",fg="white",padx=10,pady=10,command=lambda rw=rw, col=col:bet_handler.ButtonPressed(rw,col)).grid(row=rw,column=col+2)
        col+=1
    rw += 1
    col = 0
#row 2
    for z in range(9):
        tk.Button(root,text=col+1,bg="red",fg="white",padx=10,pady=10,command=lambda rw=rw, col=col:bet_handler.ButtonPressed(rw,col)).grid(row=rw,column=col+2)
        col+=1
    rw += 1
    col = 0
#row 3
    for z in range(9):
        tk.Button(root,text=col+1,bg="red",fg="white",padx=10,pady=10,command=lambda rw=rw, col=col:bet_handler.ButtonPressed(rw,col)).grid(row=rw,column=col+2)
        col+=1

    ######sets up non board related buttons (spin wheel, reset bets etc)
    global spin_wheel_button
    spin_wheel_button = tk.Button(root,text="Spin wheel",bg="blue",fg="white",padx=10,pady=10, command=lambda: game.spin_wheel())
    spin_wheel_button.grid(columnspan=2,row=3,column=15)

    tk.Button(root,text="Reset bets",bg="blue",fg="white",padx=12,pady=10, command=lambda: bet_handler.reset_bets()).grid(columnspan=2,row=2,column=15)
    tk.Button(root, text="1st 12",pady=15,padx=55,bg="#bacc39",fg="white",command=lambda: test()).grid(row=4,column=2,columnspan=4)
    tk.Button(root, text="2nd 12",pady=15,padx=60,bg="#bacc39",fg="white",command=lambda: test()).grid(row=4,column=6,columnspan=4)
    tk.Button(root, text="3rd 12",pady=15,padx=60,bg="#bacc39",fg="white",command=lambda: test()).grid(row=4,column=10,columnspan=4)

    global P1_B
    P1_B = tk.Button(root,state=tk.NORMAL, text="1 Player",pady=10,padx=10,bg="#151bb5",fg="white",command=lambda: game.def_plng_ply_amnt(1))
    P1_B.grid(row=2,column=17)
    P1_B.config(state=tk.DISABLED)

    global P2_B
    P2_B = tk.Button(root,state=tk.NORMAL, text="2 Player",pady=10,padx=10,bg="#151bb5",fg="white",command=lambda: game.def_plng_ply_amnt(2))
    P2_B.grid(row=3,column=17)

    global pass_button
    pass_button = tk.Button(root, text="Pass Turn",state=tk.DISABLED,pady=14,padx=14,bg="#f48c42",fg="white",command=lambda: game.turn_change())
    pass_button.grid(row=4,column=16)

    print('success! the buttons on the board has been set up')
        
##############################

def set_circle_text(canvas):
    global circle_text
    circle_text=canvas.create_text(200,200, text=game.win_num,fill="white",font=("Helvetica", 100)) # the text on the circle will be the winning number

##############################
    
def set_up_board_texts():
    print('setting up the texts on the board ')
    global player_display
    player_display = tk.StringVar()
    player_display.set("Single Player Mode")
    tk.Label(root,textvariable= player_display,bg="green",fg="white",font=("Helvetica",25)).grid(row=1,column=19)
    global chip_display
    chip_display = tk.StringVar()
    chip_display.set("Total Player 1 Chips : 1000")
    tk.Label(root,textvariable= chip_display,bg="green",fg="white",font=("Helvetica",25)).grid(row=2,column=19)
    print('success! the text on the board has been set up')

def set_up_board_circle():
    print('setting up the circle on the board ')
    global canvas
    canvas = tk.Canvas(root,width=400,height=400,highlightthickness=0,bd=0,bg="#09681a")
    canvas.grid(row=6,column=19,columnspan=2,rowspan=10)
    canvas.create_oval(0, 0, 400, 400, fill = "black")
    print('success! the circle on the board has been set up')

def test(): #a placeholder function to stop errors
    print('test')
