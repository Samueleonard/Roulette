import tkinter as tkinter
import functions

f

actualnum = 1
def guessnum(num):
    if num == actualnum:
        print("You win!")



root = tkinter.Tk()
button1 = tkinter.Button(root, text="1", command=lambda: guessnum(int(1)))
button2 = tkinter.Button(root, text="2")
button3 = tkinter.Button(root, text="3")
button4 = tkinter.Button(root, text="4")
button5 = tkinter.Button(root, text="5")
button6 = tkinter.Button(root, text="6")
button7 = tkinter.Button(root, text="7")
button8 = tkinter.Button(root, text="8")
button9 = tkinter.Button(root, text="9")
button10 = tkinter.Button(root, text="10")

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()

root.mainloop()


