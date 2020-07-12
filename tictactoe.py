import tkinter
from tkinter import messagebox

def tic():
    #  class that contains the GUI and game responses  
    global count
    count = 1
    global l
    global score_1
    global score_2
    score_1 = 0
    score_2 = 0
    l = list('a b c d e f g h i'.split())
    global window
    window = tkinter.Tk()
    #window.geometry("520x540")
    window.title("Tic Tac Toe")
    window.resizable(0,0)
    #window.geometry('438x472') for all 9 squares and #146x158 for each square 

    def result(score_1,score_2):
        head = tkinter.Label(window,text='Score Table:',font=('Arial Italic',15),bg='#D5D5D5',width='15',height=3)
        score_1_lb = tkinter.Label(window,text='Player1',font=('Arial Bold',20),bg='white',relief='ridge',width='10')
        score_2_lb = tkinter.Label(window, text='Player2', font=('Arial Bold', 20), bg='white', relief="ridge", width=10)
        val1 = tkinter.Label(window,text=str(score_1), font=('Arial Bold', 20), bg='white',relief='ridge',width='10')
        val2 = tkinter.Label(window,text=str(score_2), font=('Arial Bold', 20), bg='white',relief='ridge',width='10')

        head.grid(row=3,column=0,rowspan=2)
        score_1_lb.grid(row=3,column=1)
        score_2_lb.grid(row=3,column=2)
        val1.grid(row=4,column=1)
        val2.grid(row=4,column=2)

    
    def chg(event,r,c): 
    # method to responds after a click event
        event.widget.grid_forget()
        global count
        if ((count%2)==0):
            b = tkinter.Label(window,text='O',font=('Arial Bold',105),width=2,height=1,bd=0,fg='red')
            #b = tkinter.Button(window, text='X',font=('Arial Bold',50),fg='black', bg='#CECCCC', bd=0, width=0, height=0)
            b.grid(row=r,column=c)
            validate(r,c,2)
        else:
            b = tkinter.Label(window,text='X',font=('Arial Bold',105),width=2,height=1,bd=0,fg='black')
            #b = tkinter.Button(window, text='O',font=('Arial Bold',50), fg='red', bg='#CECCCC', bd=0, width=0, height=0)
            b.grid(row=r,column=c)
            validate(r,c,1)

        
        
    def validate(r,c,player):
        a = r*3+c
        global l
        global count
        global score_1
        global score_2
        l[a] = player
        if(((l[0]==l[1])&(l[1]==l[2]))| ((l[0]==l[4])&(l[4]==l[8]))| ((l[0]==l[3])&(l[3]==l[6]))| ((l[3]==l[4])&(l[4]==l[5]))| ((l[1]==l[4])&(l[4]==l[7]))|   ((l[2]==l[5])&(l[5]==l[8]))| ((l[6]==l[7])&(l[7]==l[8]))| ((l[2]==l[4])&(l[4]==l[6]))):
            messagebox.showinfo('Congrats','Player '+str(player)+' wins' )
            if(player == 1):
                score_1+= 1
            else:
                score_2+= 1

            #window.destroy()
            count=1
            result(score_1,score_2)
            
        count = count + 1
        if (count==10):
            messagebox.showinfo('Tie','That is a tie , well played')
            window.destroy()
        

    b00 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
    b00.grid(row=0,column=0)
    b00.bind('<Button-1>',lambda event : chg(event,0,0))


    b01 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10)
    b01.grid(row=0,column=1)
    b01.bind('<Button-1>',lambda event : chg(event,0,1))

    b02 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10) 
    b02.grid(row=0,column=2)
    b02.bind('<Button-1>',lambda event : chg(event,0,2))

    b10 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10)
    b10.grid(row=1,column=0)
    b10.bind('<Button-1>',lambda event : chg(event,1,0))

    b11 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
    b11.grid(row=1,column=1)
    b11.bind('<Button-1>',lambda event : chg(event,1,1))
    
    b12 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10) 
    b12.grid(row=1,column=2)
    b12.bind('<Button-1>',lambda event : chg(event,1,2))

    b20 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
    b20.grid(row=2,column=0)
    b20.bind('<Button-1>',lambda event : chg(event,2,0))
    
    b21 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10)
    b21.grid(row=2,column=1)
    b21.bind('<Button-1>',lambda event : chg(event,2,1))
    
    b22 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10) 
    b22.grid(row=2,column=2)
    b22.bind('<Button-1>',lambda event : chg(event,2,2))

    window.mainloop()
    
if __name__ == '__main__':
	tic()
    




