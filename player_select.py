import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("520x470")
window['bg'] = 'white'
window.resizable(0,0)

def getname(event,arg):
    spin_val = spin.get()
    if(int(spin_val)>10):
        spin_val = 10
    elif(int(spin_val)<1):
        spin_val = 1

    print(spin_val)

    name = simpledialog.askstring("Player Name","Please enter Player1 name")
    print(name)


head = tk.Label(window,text='VS',font=("Arial",50),bg='white')
player_btn = tk.Button(window,text='Player',font=("Arial ",50),bg='white',fg='Black',width='10',bd=10)
player_btn.bind('<Button-1>',lambda event: getname(event,'player'))

comp_btn = tk.Button(window,text='Computer',font=("Arial ",50),bg='Black',fg='white',width='10',bd=10)
comp_btn.bind('<Button-1>',lambda event : getname(event,'computer'))

spin = tk.Spinbox(window,values=(1,2,3,4,5,6,7,8,9,10),width=5)
space = tk.Label(window,text='*********',fg='white',bg='white')
matches = tk.Label(window,text='Number of matches (1 to 10) :',font=("Arial",15),bg='white')

space.grid(row=0,column=0)
head.grid(row=0,column=1,columnspan=2)
matches.grid(row=1,column=1)
spin.grid(row=1,column=2,pady=10)
player_btn.grid(row=2,column=1,columnspan=2)
comp_btn.grid(row=3,column=1,columnspan=2)



# print(spin.get())


window.mainloop()