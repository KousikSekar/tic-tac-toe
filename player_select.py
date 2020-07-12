import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("520x470")
window['bg'] = 'white'
window.resizable(0,0)


head = tk.Label(window,text='VS',font=("Arial",50),bg='white')
player_btn = tk.Button(window,text='Player',font=("Arial ",50),bg='white',fg='Black',width='10',bd=10)
comp_btn = tk.Button(window,text='Computer',font=("Arial ",50),bg='Black',fg='white',width='10',bd=10)

head.pack()
player_btn.pack()
comp_btn.pack()




window.mainloop()