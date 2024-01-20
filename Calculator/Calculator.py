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
root.mainloop()
