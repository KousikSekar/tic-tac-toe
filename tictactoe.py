import tkinter
from tkinter import messagebox


def tic(series,player1,player2):
    #  class that contains the GUI and game responses
    global count , match_no , l , score_1 , score_2
    match_no = 1
    count = 1
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
        head = tkinter.Label(window,text='Score Table:',font=('Arial Italic',13),bg='#D5D5D5',width='16',height=3)
        score_1_lb = tkinter.Label(window,text=player1,font=('Arial Italic',13))
        score_2_lb = tkinter.Label(window, text=player2, font=('Arial Italic', 13))
        val1 = tkinter.Label(window,text=str(score_1), font=('Arial Bold', 20), bg='white',relief='ridge',width='10')
        val2 = tkinter.Label(window,text=str(score_2), font=('Arial Bold', 20), bg='white',relief='ridge',width='10')

        head.grid(row=0,column=0,rowspan=2)
        score_1_lb.grid(row=0,column=1)
        score_2_lb.grid(row=0,column=2)
        val1.grid(row=1,column=1)
        val2.grid(row=1,column=2)

    
    def chg(event,r,c,f,s,fgf,fgs,pl1,pl2):
    # method to responds after a click event
        event.widget.grid_forget()
        global count
        #print('count at chg',count)
        if ((count%2)==0):
            window.title('Tic-Tac-Toe    Series :'+str(series)+'  Game :'+str(match_no-1)+'   '+str(pl1)+' turn ')
            b = tkinter.Label(window,text=s,font=('Arial Bold',105),width=2,height=1,bd=0,fg=fgf)
            #b = tkinter.Button(window, text='X',font=('Arial Bold',50),fg='black', bg='#CECCCC', bd=0, width=0, height=0)
            b.grid(row=r,column=c)
            validate(r,c,pl2)
        else:
            window.title('Tic-Tac-Toe    Series :'+str(series)+'  Game :'+str(match_no-1)+'   '+str(pl2)+' turn ')
            b = tkinter.Label(window,text=f,font=('Arial Bold',105),width=2,height=1,bd=0,fg=fgs)
            #b = tkinter.Button(window, text='O',font=('Arial Bold',50), fg='red', bg='#CECCCC', bd=0, width=0, height=0)
            b.grid(row=r,column=c)
            validate(r,c,pl1)

        
        
    def validate(r,c,player):
        a = (r-2)*3+c
        global l
        global count
        global score_1
        global score_2
        l[a] = player
        if(((l[0]==l[1])&(l[1]==l[2]))| ((l[0]==l[4])&(l[4]==l[8]))| ((l[0]==l[3])&(l[3]==l[6]))| ((l[3]==l[4])&(l[4]==l[5]))| ((l[1]==l[4])&(l[4]==l[7]))|   ((l[2]==l[5])&(l[5]==l[8]))| ((l[6]==l[7])&(l[7]==l[8]))| ((l[2]==l[4])&(l[4]==l[6]))):

            if(player == player1):
                score_1+= 1
                count = 0
            else:
                score_2+= 1
                count = 0

            #window.destroy()
            result(score_1,score_2)
            messagebox.showinfo('Congrats', str(player) + ' wins')
            board(player1, player2)

        count = count + 1

        if (count==10):
            count = 1
            messagebox.showinfo('Tie', 'That is a tie , well played')
            board(player1, player2)
            #window.destroy()
        
    def board(player1,player2):

        global l
        global match_no
        l = l = list('a b c d e f g h i'.split())
        if(match_no%2 == 0):
            f = 'O'
            s = 'X'
            fgs = 'red'
            fgf = 'black'
            pl1 = player2
            pl2 = player1
        else:
            f = 'X'
            s = 'O'
            fgs = 'black'
            fgf = 'red'
            pl1 = player1
            pl2 = player2



        def series_end():
                if(score_1>score_2):
                    winner = player1
                    message = str(player1)+' wins the series'
                elif(score_2>score_1):
                    winner = player2
                    message = str(player2) + ' wins the series'
                else:
                    message = 'The series is a draw'
                messagebox.showinfo('Congrats to Champion',message)
                window.destroy()
        def endgame(event):
            response = messagebox.askquestion("Quit", message='Are you sure you want to end this series, you will be navigated back to home screen')
            #print(response)
            if(response=='yes'):
                series_end()

        match_no += 1
        window.title('Tic-Tac-Toe    Series :' + str(series) + '  Game :' + str(match_no - 1) + '   ' + str(pl1) + ' turn ')
        if(match_no>=series+2):
            series_end()



        #print("Count at board",count)
        b00 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
        b00.grid(row=2,column=0)
        b00.bind('<Button-1>',lambda event : chg(event,2,0,f,s,fgf,fgs,pl1,pl2))


        b01 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10)
        b01.grid(row=2,column=1)
        b01.bind('<Button-1>',lambda event : chg(event,2,1,f,s,fgf,fgs,pl1,pl2))

        b02 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
        b02.grid(row=2,column=2)
        b02.bind('<Button-1>',lambda event : chg(event,2,2,f,s,fgf,fgs,pl1,pl2))

        b10 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10)
        b10.grid(row=3,column=0)
        b10.bind('<Button-1>',lambda event : chg(event,3,0,f,s,fgf,fgs,pl1,pl2))

        b11 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
        b11.grid(row=3,column=1)
        b11.bind('<Button-1>',lambda event : chg(event,3,1,f,s,fgf,fgs,pl1,pl2))

        b12 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10)
        b12.grid(row=3,column=2)
        b12.bind('<Button-1>',lambda event : chg(event,3,2,f,s,fgf,fgs,pl1,pl2))

        b20 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
        b20.grid(row=4,column=0)
        b20.bind('<Button-1>',lambda event : chg(event,4,0,f,s,fgf,fgs,pl1,pl2))

        b21 = tkinter.Button(window,fg='white',bg='#CECCCC',bd=0,width=24,height=10)
        b21.grid(row=4,column=1)
        b21.bind('<Button-1>',lambda event : chg(event,4,1,f,s,fgf,fgs,pl1,pl2))

        b22 = tkinter.Button(window,fg='white',bg='white',bd=0,width=24,height=10)
        b22.grid(row=4,column=2)
        b22.bind('<Button-1>',lambda event : chg(event,4,2,f,s,fgf,fgs,pl1,pl2))

        end_game = tkinter.Button(window,width=43,height=2,text='End Game',font=('Arial Bold',15),bd=3,relief='ridge')
        end_game.grid(row=5,column=0,columnspan=3)
        end_game.bind('<Button-1>',lambda event : endgame(event))

    board(player1,player2)
    result(score_1,score_2)

    window.mainloop()
    
if __name__ == '__main__':
    player1 = 'Donald Trump'
    player2 = 'Vladimir Putin'

    def transform(name,position):
        if(len(name)>16):
            name = str(name[:14])+'..'
        elif(len(name)==0):
            name = 'Player-'+str(position)
        else:
            name = name
        return name
    pl1 = transform(player1.strip(),1)
    pl2 = transform(player2.strip(),2)
    tic(5,pl1,pl2)

    




