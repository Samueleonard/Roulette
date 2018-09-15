from tkinter import *
root = Tk()
Button(text="0",bg="green",fg="white",padx=10, pady=54, command=lambda: guessnum(int(r))).grid(rowspan=3, row=1, column=1)
r = 0
for c in range(4):
    r = r + 3
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=1,column=int((r/3)+1))
    r = r + 3
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=1,column=int((r/3)+1))
    r = r + 3
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=1,column=int((r/3)+1))
r = -1
for fghfdhd in range(4):
    r = r + 3
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=2,column=int((r+1)/3)+1)
    r = r + 3
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=2,column=int((r+1)/3)+1)
    r = r + 3
    Button(root,text=str(r),highlightbackground="white", bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=2,column=int((r+1)/3)+1)

r = -2
for fghfdhd in range(2):
    r = r + 3
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=3,column=int((r+2)/3)+1)
    r = r + 3
    Button(root,text=str(r),bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=3,column=int((r+2)/3)+1)
    r = r + 3
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=3,column=int((r+2)/3)+1)
    r = r + 3
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=3,column=int((r+2)/3)+1)
    r = r + 3
    Button(root,text=str(r), bg="black",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=3,column=int((r+2)/3)+1)
    r = r + 3
    Button(root,text=str(r), bg="red",fg="white", padx=10, pady=10, command=lambda: guessnum(int(r))).grid(row=3,column=int((r+2)/3)+1)
lol = Canvas(root, width=10, height=10)
lol.grid(row=15,column=15)
img = PhotoImage(file="123.gif")
lol.create_image(image=img)
mainloop()
