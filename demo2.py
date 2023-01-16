from tkinter import *
window = Tk()

#add widgets from here

window.geometry("300x200+10+20")
window.title("My First DUI Application")

# Add label Widgets

lbl = Label(window,text = "My DUI", fg = "Red",font =("Verdana",10))
lbl.place(x=100,y=20)

lbl2 = Label(window,text="First Text Field")
lbl2.place(x=5,y=50)

lbl3 = Label(window,text="Second Text Field")
lbl3.place(x=5,y=70)

#Add Button Widgets
btn = Button(window,text="YES",fg="Blue",font=("Verdana",10))
btn.place(x=150,y=100)

btn2 = Button(window,text="NO",fg="Blue",font=("Verdana",10))
btn2.place(x=200,y=100)

#Add Entry Widgets
txtfld = Entry(window,text="This is an Entry Widget",bd=3)
txtfld.place(x=150,y=50)

txtfld2 = Entry(window,text="2nd Entry Widget",bd=3)
txtfld2.place(x=150,y=70)

#Add Radio Button

def sel():
    selection = "You selected option" + str(var.get())
    label.config(text=selection)
var = IntVar()
r1 = Radiobutton(window,text="Male",variable=var,value=1,command=sel)
r1.place(x=150,y=130)

r2 = Radiobutton(window,text="Female",variable=var,value=2,command=sel)
r2.place(x=220,y=130)

label = Label(window)
label.place(x=160,y=150)
window.mainloop()

