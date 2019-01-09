from tkinter import *
root=Tk()

rw = 1
col = 0

#row 1
Button(root,text=col+1).grid(row=rw, column=col)
col += 1
Button(root, text=col+1).grid(row=rw, column=col)
col += 1
Button(root,text=col+1).grid(row=rw, column=col)
col += 1
Button(root,text=col+1).grid(row=rw, column=col)
col += 1
Button(root,text=col+1).grid(row=rw, column=col)
rw += 1
col = 0

#row 2
Button(root,text="B1").grid(row=rw, column=col)
col += 1
Button(root, text="B2").grid(row=rw, column=col)
col += 1
Button(root,text="B3").grid(row=rw, column=col)
col += 1
Button(root,text="B4").grid(row=rw, column=col)
col += 1
Button(root,text="B5").grid(row=rw, column=col)
rw += 1
col = 0


#row3
Button(root,text="B1").grid(row=rw, column=col)
col += 1
Button(root, text="B2").grid(row=rw, column=col)
col += 1
Button(root,text="B3").grid(row=rw, column=col)
col += 1
Button(root,text="B4").grid(row=rw, column=col)
col += 1
Button(root,text="B5").grid(row=rw, column=col)

widget = root.grid_slaves(row=int(rw),column=int(col))[0]
a = widget["text"]
print(a)
root.mainloop()
