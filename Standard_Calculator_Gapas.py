from tkinter import *
window = Tk()

# add widgets from here
window.geometry("229x250+760+400")
window.title("Calculator")
# label widget
lbl = Label(window, text="0", fg="black", font=("Serif",15))
lbl.place(x=180, y=3)

# 1st line
mc = Button(window,text="MC", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
mc.place(x=12, y=35)
mr = Button(window, text="MR", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
mr.place(x=65, y=35)
msubtract = Button(window, text="M-", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
msubtract.place(x=118, y=35)
madd = Button(window, text="M+", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
madd.place(x=173, y=35)

# 2nd line
ac = Button(window, text="AC", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
ac.place(x=12, y=65)
sqrtx = Button(window, text="√x", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
sqrtx.place(x=65, y=65)
percent = Button(window, text="%", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
percent.place(x=118, y=65)
divide = Button(window, text="÷", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
divide.place(x=173, y=65)

# 3rd line
seven = Button(window, text="7", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
seven.place(x=12, y=95)
eight = Button(window, text="8", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
eight.place(x=65, y=95)
nine = Button(window, text="9", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
nine.place(x=118, y=95)
multiply = Button(window, text="x", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
multiply.place(x=173, y=95)

# 4th line
four = Button(window, text="4", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
four.place(x=12, y=125)
five = Button(window, text="5", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
five.place(x=65, y=125)
six = Button(window, text="6", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
six.place(x=118, y=125)
subtract = Button(window, text="-", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
subtract.place(x=173, y=125)

# 5th line
one = Button(window, text="1", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
one.place(x=12, y=155)
two = Button(window, text="2", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
two.place(x=65, y=155)
three = Button(window, text="3", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
three.place(x=118, y=155)
add = Button(window, text="+", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
add.place(x=173, y=155)

# 6th line
zero = Button(window, text="0", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
zero.place(x=12, y=185)
dot = Button(window, text=".", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
dot.place(x=65, y=185)
adddividesubtract = Button(window, text="+/-", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
adddividesubtract.place(x=118, y=185)
equal = Button(window, text="=", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
equal.place(x=173, y=185)

# 7th line
pi = Button(window, text="π", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
pi.place(x=12, y=215)
xsqr = Button(window, text="x^2", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
xsqr.place(x=65, y=215)
r2 = Button(window, text="R2", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
r2.place(x=118, y=215)
r0 = Button(window, text="R0", font=("Serif", 10), bd=2, height=1, width=4, fg="darkblue")
r0.place(x=173, y=215)

window.mainloop()