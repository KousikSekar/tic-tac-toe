## Welcome Screen

import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("520x470")
window['bg'] = 'white'
window.resizable(0,0)

def areyousure(event):
    response = messagebox.askquestion("Quit",message='Are you sure you want to quit')
    print(response)
    if(response == 'yes'):
        window.destroy()




wel_path = r"D:\learning\Python\tic-tac-toe\welcomescreenpng.png"
tic_path = r"D:\learning\Python\tic-tac-toe\TicTacToe2.png"
startgame_path = r"D:\learning\Python\tic-tac-toe\button_start-game.png"
howtoplay_path = r"D:\learning\Python\tic-tac-toe\button_how-to-play.png"
quit_path = r"D:\learning\Python\tic-tac-toe\button_quit.png"


#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
wel_img = ImageTk.PhotoImage(Image.open(wel_path))
tic_img = ImageTk.PhotoImage(Image.open(tic_path))
startgame = ImageTk.PhotoImage(Image.open(startgame_path))
howtoplay = ImageTk.PhotoImage(Image.open(howtoplay_path))
quit_img = ImageTk.PhotoImage(Image.open(quit_path))



#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
wel_panel = tk.Label(window, image = wel_img,anchor='n',background='white',width=530)
tic_panel = tk.Label(window, image= tic_img,anchor='n',background='white',width=530)

start_btn = tk.Button(window,image=startgame,bd=0,bg='white')
howtoplay_btn = tk.Button(window,image=howtoplay,bd=0,bg='white')
quit_btn = tk.Button(image=quit_img,bd=0,bg='white')
quit_btn.bind('<ButtonRelease-1>',lambda event : areyousure(event))

#done_by = tk.Label(window,text='-by Kousik',font=('Arial Bold',10),width=200,height=1,bd=0,fg='red',anchor='se',bg='white')


#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "bottom", fill = "both", expand = "yes")
wel_panel.grid(row=0)
tic_panel.grid(row=1)
start_btn.grid(row=2,pady=5)
howtoplay_btn.grid(row=3,pady=5)
quit_btn.grid(row=4,pady=5)
#done_by.grid(row=5)



#Start the GUI
window.mainloop()