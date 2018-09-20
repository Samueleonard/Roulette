from tkinter import *
import roulette

totalMoney = roulette.total_money

def set_up_prefs():
    root.title("Roulette - 0.18a")
    root.geometry("900x700")
    root.iconbitmap(r'C:\Users\Samuel\Documents\GitHub\Roulette\icon.jpg')

def create_canvas():
    canvas = Canvas(root,width=400,height=400,highlightthickness=0,bd=0,bg="#09681a")
    canvas.grid(row=40,column=40)
    canvas.create_oval(0, 0, 400, 400, fill = "black")
    canvas.create_text(200,200, text="hi",fill="white",font=("Helvetica", 100))

def create_roulette_board():
    Button(text="0",bg="green",fg="white",padx=10, pady=54, command=lambda: guessnum()).grid(rowspan=3, row=1, column=1)
    r = 0
    root.configure(bg="#09681a")
    for c in range(4):
        r = r + 3
        Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=1,column=int((r/3)+1))
        r = r + 3
        Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=1,column=int((r/3)+1))
        r = r + 3
        Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=1,column=int((r/3)+1))
    r = -1
    for fghfdhd in range(4):
        r = r + 3
        Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=2,column=int((r+1)/3)+1)
        r = r + 3
        Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=2,column=int((r+1)/3)+1)
        r = r + 3
        Button(root,text=str(r),highlightbackground="white", bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=2,column=int((r+1)/3)+1)

    r = -2
    for fghfdhd in range(2):
        r = r + 3
        Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=3,column=int((r+2)/3)+1)
        r = r + 3
        Button(root,text=str(r),bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=3,column=int((r+2)/3)+1)
        r = r + 3
        Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=3,column=int((r+2)/3)+1)
        r = r + 3
        Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=3,column=int((r+2)/3)+1)
        r = r + 3
        Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=3,column=int((r+2)/3)+1)
        r = r + 3
        Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum()).grid(row=3,column=int((r+2)/3)+1)

def guessnum():
    roulette.__init__(totalMoney)
    
root = Tk()
set_up_prefs()
create_roulette_board()
create_canvas()
mainloop()



