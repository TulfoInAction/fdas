from tkinter import *
from tkinter import messagebox

my_list = []

class Employees:
    def __init__(self, name, department, position, rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate

def display_name():
    a = e2.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    my_list.append(Employees(a,b,c,d))
    messagebox.showinfo("DIALOG BOX", Successful)
    
    
def add():
    messagebox.showinfo("DIALOG BOX", Employees)
        
    
    

master = Tk()
Label(master, text="NAME: ").grid(row=0, padx=20, pady=10)
Label(master, text="DEPARTMENT: ").grid(row=1, padx=20, pady=10)
Label(master, text="POSITION: ").grid(row=2, padx=20, pady=10)
Label(master, text="RATE: ").grid(row=3, padx=20, pady=10)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1, padx=20, pady=10)
e2.grid(row=1, column=1, padx=20, pady=10)
e3.grid(row=2, column=1, padx=20, pady=10)
e4.grid(row=3, column=1, padx=20, pady=10)

b1 = Button(master, text="ADD", command=display_name)
b1.grid(row=4, column=1, padx=20, pady=10)

b2 = Button(master, text="SHOW", command=add)
b2.grid(row=5, column=1, padx=20, pady=10)

mainloop()
