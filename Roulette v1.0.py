#Hello, this is currently a working version of roulette with most buttons inculded and a money system in place. Some buttons need to be added and more than one user ability, eg. One player bets on their things then other does, then spin is hit
#The GUI doesn't look great but it is functional, I will not be making it look much better any time soon due to the need to put it into classes and frames which is annoying
#Bug testing is needed, so grab some idiot to test and try to break
#I am calling this version 1.0 since it works
#Some explanation for code has been added, rest will be added at later date
#Multiplayer note - Create dicts of the data needed for each player, then on needed functions assign the data as the dict value of which player it is. Have button to end turn
#Make it so they have ot bet "if len(bets) == 0" sort of thing
from tkinter import *
import random
import time
###############################
player_data = {1: {'total_chips': 1000, 'bets': {}, 'special_bets': {}},
               2: {'total_chips': 1000, 'bets': {}, 'special_bets': {}}
               }

player_am = 1
player_turn = 1

###############################

def player_am_define(am):
    global player_am
    global player_data
    if am == 1:
        player_am = 1
        ply2_button.config(state = NORMAL)
        ply1_button.config(state = DISABLED)
        pass_button.config(state = DISABLED)
        player_display.set("Single Player Mode")
        chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))
    else:
        global player_turn
        player_turn = 1
        player_am = 2
        ply1_button.config(state = NORMAL)
        ply2_button.config(state = DISABLED)
        pass_button.config(state = NORMAL)
        player_display.set("Player 1")
    player_data = {1: {'total_chips': 1000, 'bets': {}, 'special_bets': {}},
               2: {'total_chips': 1000, 'bets': {}, 'special_bets': {}}}
    chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))


def turn_change():
    global player_turn
    global player_am
    if player_am == 1:
        pass
    else:
        if player_turn == 1:
            player_turn += 1
            player_display.set("Player 2")
            chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))
        else:
            player_turn = 1
            player_display.set("Player 1")
            chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))
            
        
    
            


bets = {}
total_chips = 1000
special_bets = {}
real_num = 12
root = Tk()
win_texts = ['you won', 'you won, gg in the chat', '#1 victory royale Keepo']

#Inactive, not needed at moment and not sure if needed later
class Player():

    def __init__(self,total_chips,total_bets):
        self.total_chips = total_chips
        self.total_bets = total_bets
#This runs on the click of the "spin" button. It gens a random int, displays it, works out if a winning condition is met and money is given if so.
def start_spin():
    
    global player_data      #global variable assignment is used inside functions due to the problems caused with them believing that they are local, it makes it much easier to have a global money as can't return money in most places
    
    real_num = random.randint(0,36)   #random int
    canvas.itemconfig(a,text=real_num)  #changes int in circle
    #real_num = 12 #  Used for testing purposes
    lis = [1,2]
    for player in lis: 
        win = False
        loss_msg = False
        if len(player_data[player]['special_bets']) != 0:
            if str(real_num // 12) in player_data[player]['special_bets'] and real_num != 0:
                player_data[player]['total_chips'] += int((player_data[player]['special_bets'][str(real_num//12)]) * 1.5)
                chip_display.set("Total Chips: " + str(player_data[player]['total_chips']))
                messagebox.askokcancel("Player " + str(player), "You win!")
                win = True
            elif (real_num == 12 and '0' in player_data[player]['special_bets']) or (real_num == 24 and '1' in player_data[player]['special_bets']) or (real_num == 36 and '2' in player_data[player]['special_bets']):
                player_data[player]['total_chips'] += int(player_data[player]['special_bets'][str((real_num//12)-1)] * 1.5)
                messagebox.askokcancel(random.choice(win_texts), "You win!")
                chip_display.set("Total Chips: " + str(player_data[player]['total_chips']))
            else:
                loss_msg = True
                messagebox.askokcancel("Player " + str(player), "You lost, try again next time")
        #print(str(player_data[player]['bets']))
        if str(real_num) in player_data[player]['bets']:
            player_data[player]['total_chips'] += (player_data[player]['bets'][str(real_num)] * 3)
            chip_display.set("Total Chips: " + str(player_data[player]['total_chips']))
            if win != True:
                messagebox.askokcancel("Player " + str(player), "You win!")
        elif len(player_data[player]['bets']) == 0:
            pass
        else:
            if loss_msg == False:
                messagebox.askokcancel("Player " + str(player), "You lost, try again next time")
        player_data[player]['bets'].clear()
        player_data[player]['special_bets'].clear()
    chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))



#This function retrieves the int from button and places bet into the dictionary       
def guessnum(rw,col):
    global player_data
    if player_data[player_turn]['total_chips'] < 20:#stops lack of funds from betting
        var2.set("Not enough chips to bet")#sets to a tkinter label
    else:
        player_data[player_turn]['total_chips'] -= 20#20 chips for bet
        chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))#displays money to gui
        widget = root.grid_slaves(row=int(rw),column=int(col))[0]#figures out what the text on button is via the pos on grid of button.
        a = widget['text']#assigns the text of button widget to a
    
        if a in player_data[player_turn]['bets']:#to avoid double assigning to dictionary or error, searches if the key is already there
            player_data[player_turn]['bets'][a] += 20
        else:
            player_data[player_turn]['bets'][a] = 20
        var2.set("You have bet " + str(player_data[player_turn]['bets'][a]) + " chips on number:" + a)#assigns to tkitner label
        
    
#This function is activated by "reset bets" button and gives money back for made bets, resets both bet dictionaries
def reset_bets():
    global player_data
    bet_type = [player_data[player_turn]['bets'], player_data[player_turn]['special_bets']]#creates list of dictionaries for use in "for" loop
    for self in bet_type:#goes thru both dicts in list
        for keys in self:#goes thru each key in dict
            player_data[player_turn]['total_chips'] += int(self[keys])#adds val of chips in key to total chips
    chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))#tkinter label
    player_data[player_turn]['bets'].clear()#clears bet dict
    player_data[player_turn]['special_bets'].clear()#clears special count dict


#Creates bet for special win conditions, same as guessnum, currently for dozens only, insert an if statement "if dozen ==0 or 1 or 2" to add other condi..
def special_bet(dozen):
    global player_data
    if player_data[player_turn]['total_chips'] < 20:
        var2.set("Not enough chips to bet")
    else:
        player_data[player_turn]['total_chips'] -= 20
        chip_display.set("Total Chips: " + str(player_data[player_turn]['total_chips']))
        if str(dozen) in player_data[player_turn]['special_bets']:#checks if key is alreeady there, if button has been clicked before
            player_data[player_turn]['special_bets'][str(dozen)] += 20
            
        else:
            player_data[player_turn]['special_bets'][str(dozen)] = 20
        var2.set("You have bet " + str(player_data[player_turn]['special_bets'][str(dozen)]) + " chips on dozen " + str(dozen + 1))

def valid_spin():
    global player_data
    if player_am == 1:
        start_spin()
    else:
        if len(player_data[1]['special_bets'])+len(player_data[1]['bets']) == 0 or len(player_data[2]['special_bets'])+len(player_data[2]['bets']) == 0:
            var2.set("Both players have to bet to spin. Try again.")
            reset_bets()
        else:
            start_spin()
                            
Button(text="0",bg="green",fg="white",padx=10, pady=54, command=lambda: guessnum(1,1)).grid(rowspan=3, row=1, column=1)                                                                                                                      
r = 0
root.configure(bg="#09681a")
rw = 1
for c in range(4):
    r = r + 3
    col = (r/3)+1
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = (r/3)+1
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = (r/3)+1
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    
r = -1
rw = 2
for fghfdhd in range(4):
    r = r + 3
    col = ((r+1)/3)+1
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = ((r+1)/3)+1
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = ((r+1)/3)+1
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))

r = -2
rw = 3
for fghfdhd in range(2):
    r = r + 3
    col = ((r+2)/3)+1
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = ((r+2)/3)+1
    Button(root,text=str(r),bg="black",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = ((r+2)/3)+1
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = ((r+2)/3)+1
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = ((r+2)/3)+1
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))
    r = r + 3
    col = ((r+2)/3)+1
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda rw=rw, col=col: guessnum(rw,col)).grid(row=rw,column=int(col))

Button(root,text="Spin wheel",bg="blue",fg="white",padx=10,pady=10, command=lambda: valid_spin()).grid(columnspan=2,row=3,column=15)
Button(root,text="Reset bets",bg="blue",fg="white",padx=12,pady=10, command=lambda: reset_bets()).grid(columnspan=2,row=2,column=15)
chip_display = StringVar()
Label(root,textvariable= chip_display,bg="green",fg="white",font=("Helvetica",25)).grid(row=2,column=19)
var = StringVar()
var2 = StringVar()
betmsg = Label(root,textvariable= var2,bg="#09681a",padx=10,pady=10,fg="white", font=(14)).grid(row=5,column=1,columnspan=9)
root.title("Roulette - 1.0 Alpha Version")
root.geometry('1300x700')
canvas = Canvas(root,width=400,height=400,highlightthickness=0,bd=0,bg="#09681a")
canvas.grid(row=6,column=19,columnspan=2,rowspan=10)
canvas.create_oval(0, 0, 400, 400, fill = "black")
a=canvas.create_text(200,200, text=real_num,fill="white",font=("Helvetica", 100))
chip_display.set("Total Chips: " + str(total_chips))
Button(root, text="1st 12",pady=15,padx=55,bg="#bacc39",fg="white",command=lambda: special_bet(0)).grid(row=4,column=2,columnspan=4)
Button(root, text="2nd 12",pady=15,padx=60,bg="#bacc39",fg="white",command=lambda: special_bet(1)).grid(row=4,column=6,columnspan=4)
Button(root, text="3rd 12",pady=15,padx=60,bg="#bacc39",fg="white",command=lambda: special_bet(2)).grid(row=4,column=10,columnspan=4)
ply1_button = Button(root,state=DISABLED, text="1 Player",pady=10,padx=10,bg="#151bb5",fg="white",command=lambda: player_am_define(1))
ply1_button.grid(row=2,column=17)
ply2_button = Button(root,state=NORMAL, text="2 Player",pady=10,padx=10,bg="#151bb5",fg="white",command=lambda: player_am_define(2))
ply2_button.grid(row=3,column=17)
pass_button = Button(root, text="Pass Turn",state=DISABLED,pady=14,padx=14,bg="#f48c42",fg="white",command=lambda: turn_change())
pass_button.grid(row=4,column=16)
player_display = StringVar()
player_display.set("Single Player Mode")
#login = Entry(root,show="*", textvariable= retrieve_input,bd=5,bg="white")
#login.grid(column=20,row=16,columnspan=2)
retrieve_input = StringVar()
Label(root,textvariable= player_display,bg="green",fg="white",font=("Helvetica",25)).grid(row=1,column=19)
mainloop()



