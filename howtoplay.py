# how to play

import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("520x470")
window['bg'] = 'white'
window.resizable(0,0)

global rule
global rules
global labl
rule = 0

prev_path = r"D:\learning\Python\tic-tac-toe\left.png"
next_path = r"D:\learning\Python\tic-tac-toe\right.png"
rule1_path = r"D:\learning\Python\tic-tac-toe\horizontal.PNG"
rule2_path = r"D:\learning\Python\tic-tac-toe\vertical.png"
rule3_path = r"D:\learning\Python\tic-tac-toe\diagonal.PNG"



prev_img = ImageTk.PhotoImage(Image.open(prev_path))
next_img = ImageTk.PhotoImage(Image.open(next_path))
rule1_img = ImageTk.PhotoImage(Image.open(rule1_path))
rule2_img = ImageTk.PhotoImage(Image.open(rule2_path))
rule3_img = ImageTk.PhotoImage(Image.open(rule3_path))
rules = [rule1_img,rule2_img,rule3_img]


def rule_change(event,cmnd):
    global rule
    global rules
    global labl
    if(cmnd == 'prev'):
        if (rule>0):
            rule = rule - 1
            labl = tk.Label(window,image=rules[rule])
    if(cmnd == 'next'):
        if(rule<2):
            rule = rule + 1
            labl = tk.Label(window,image=rules[rule])
    labl.grid(row=1,column=2)
    


ins = tk.Label(window,font=('Arial Bold',18),text = "Place it consecutively to win",width=0,fg='black',bg='white')

prev_btn = tk.Button(window,anchor='e',image=prev_img,bd=0,bg='white')
prev_btn.bind('<Button-1>',lambda event : rule_change(event,'prev'))

next_btn = tk.Button(window,anchor='e',image=next_img,bd=0,bg='white')
next_btn.bind('<Button-1>',lambda event : rule_change(event,'next'))

labl = tk.Label(window,image=rules[rule])
    

ins.grid(row=0,column=2,pady=20)
prev_btn.grid(row=1,column=1,padx=10)
next_btn.grid(row=1,column=3,padx=5)
labl.grid(row=1,column=2,padx=5)


window.mainloop()