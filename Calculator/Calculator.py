from tkinter import *

root=Tk()
root.title("Simple Calculator")
# size of calculator
root.geometry('332x550') 
root.minsize(332,550)
root.maxsize(332,550)
#creating a entry to display input numbers and return value
e=Entry(root, width=17 , borderwidth=5,font=("arial",25))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#Main Logic to make a simple calculator
def button_click():
    None

def button_sign():
    None

def button_equal():
    None

def button_clear():
    None

#add calculator buttons
button_1=Button(root, text="1",padx=45, pady=25,borderwidth=4, command=lambda:button_click(1))
button_2=Button(root, text="2",padx=45, pady=25,borderwidth=4, command=lambda:button_click(2))
button_3=Button(root, text="3",padx=45, pady=25,borderwidth=4, command=lambda:button_click(3))
button_4=Button(root, text="4",padx=45, pady=25,borderwidth=4, command=lambda:button_click(4))
button_5=Button(root, text="5",padx=45, pady=25,borderwidth=4, command=lambda:button_click(5))
button_6=Button(root, text="6",padx=45, pady=25,borderwidth=4, command=lambda:button_click(6))
button_7=Button(root, text="7",padx=45, pady=25,borderwidth=4, command=lambda:button_click(7))
button_8=Button(root, text="8",padx=45, pady=25,borderwidth=4, command=lambda:button_click(8))
button_9=Button(root, text="9",padx=45, pady=25,borderwidth=4, command=lambda:button_click(9))
button_0=Button(root, text="0",padx=45, pady=25,borderwidth=4, command=lambda:button_click(0))
button_point=Button(root, text=".",padx=45, pady=25,borderwidth=4, command=lambda:button_click("."))

button_add=Button(root, text="+",padx=45, pady=25,borderwidth=4, command=lambda:button_sign("+"))
button_subtract=Button(root, text="-",padx=45, pady=25,borderwidth=4, command=lambda:button_sign("-"))
button_divide=Button(root, text="/",padx=45, pady=25,borderwidth=4, command=lambda:button_sign("/"))
button_multiply=Button(root, text="*",padx=45, pady=25,borderwidth=4, command=lambda:button_sign("*"))

button_clear=Button(root, text="clear",padx=45, pady=25,borderwidth=4, command=button_clear)
button_equal=Button(root, text="=",padx=45, pady=25,borderwidth=4, command=button_equal)

#Display Buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_point.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_add.grid(row=5,column=0)
button_subtract.grid(row=5,column=1)
button_divide.grid(row=5,column=2)
button_multiply.grid(row=6,column=0,columnspan=2)

button_clear.grid(row=6,column=1,columnspan=2)
root.mainloop()
