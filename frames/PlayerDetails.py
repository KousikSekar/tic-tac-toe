import tkinter as tk

root = tk.Tk()
heading = tk.Text(height=2,wrap='none')

heading_left = tk.Label(root, text="         Player's", font=('Arial Italic', 25), anchor='ne',
                        fg='Black',bg='white', width=9)
heading_right = tk.Label(root, text="Lounge          ", font=('Arial Italic', 25), anchor='nw',
                        fg='green',bg='white',width=9)

line = tk.Label(root, text="=> You're just one step away =>", font=('Arial Italic', 17), anchor='n')
line1 = tk.Label(root, text='Please enter details below : ', font=('Arial', 12), anchor='nw')
line2 = tk.Label(root, text='First Player Name :', font=('Arial', 10), anchor='nw')
line3 = tk.Label(root, text='Second Player Name :', font=('Arial', 10), anchor='nw')
line4 = tk.Label(root, text='Number of Games to Play :    \nEnter a value between 1 to 10'
                 , font=('Arial', 10), anchor='w')

text2 = tk.Text(root, height=1, width=20)
text3 = tk.Text(root, height=1, width=20)
text4 = tk.Spinbox(root, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), width=10)
space_left = tk.Label(text = '        ')
space_right = tk.Label(text = '        ')
space_top = tk.Label(text = ' ',height=1)
back = tk.Button(root,text="<-Back",bd=2,width = 15, height=3 )
begin = tk.Button(root,text="Begin game->",bd=2,width = 15, height=3 )
home = tk.Button(root,text="Home",bd=2,width = 20, height=3)
space_top.grid(row=0)
space_left.grid(row=1,column=0,padx=10,pady=10)
space_right.grid(row=1,column=3,padx=10,pady=10)


heading_left.grid(row=1, column=1,padx=10,pady=0)
heading_right.grid(row=1, column=2,padx=10,pady=10)
line.grid(row=2, column=1,columnspan=2,padx=10,pady=10)
line1.grid(row=3, column=1,padx=10,pady=10)
line2.grid(row=4, column=1,sticky='w',padx=10,pady=10)
text2.grid(row=4, column=2,sticky='w',padx=10,pady=10)
line3.grid(row=5, column=1,sticky='w',padx=10,pady=10)
text3.grid(row=5, column=2,sticky='w',padx=10,pady=10)
line4.grid(row=6, column=1,sticky='w',padx=10,pady=10)
text4.grid(row=6, column=2,sticky='w',padx=10,pady=10)
back.grid(row=7,column=1,padx=10,pady=10)
begin.grid(row=7,column=2,padx=10,pady=10)
home.grid(row=8,column=1, columnspan=2,sticky='n')

root.mainloop()
