import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from PIL import ImageTk, Image

LARGE_FONT = ('Arial', 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Tic-Tac-Toe')


        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=2)

        self.frames = {}

        for F in (WelcomeScreen, HowToPlay, PlayerSelect, TicTacToeBoard):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomeScreen)

    def show_frame(self, cont, *args):
        frame = self.frames[cont]
        frame.tkraise()


class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = 'white'

        def areyousure(event):
            response = messagebox.askquestion("Quit", message='Are you sure you want to quit')
            print(response)
            if (response == 'yes'):
                self.quit()

        wel_path = r"D:\learning\Python\tic-tac-toe\welcomescreenpng.png"
        tic_path = r"D:\learning\Python\tic-tac-toe\TicTacToe2.png"
        startgame_path = r"D:\learning\Python\tic-tac-toe\button_start-game.png"
        howtoplay_path = r"D:\learning\Python\tic-tac-toe\button_how-to-play.png"
        quit_path = r"D:\learning\Python\tic-tac-toe\button_quit.png"

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        self.wel_img = ImageTk.PhotoImage(Image.open(wel_path))
        self.tic_img = ImageTk.PhotoImage(Image.open(tic_path))
        self.startgame = ImageTk.PhotoImage(Image.open(startgame_path))
        self.howtoplay = ImageTk.PhotoImage(Image.open(howtoplay_path))
        self.quit_img = ImageTk.PhotoImage(Image.open(quit_path))

        wel_panel = tk.Label(self, image=self.wel_img, anchor='n', background='white', width=530)
        tic_panel = tk.Label(self, image=self.tic_img, anchor='n', background='white', width=530)
        start_btn = tk.Button(self, image=self.startgame, bd=0, bg='white',
                              command=lambda: controller.show_frame(PlayerSelect))
        howtoplay_btn = tk.Button(self, image=self.howtoplay, bd=0, bg='white',
                                  command=lambda: controller.show_frame(HowToPlay))
        # howtoplay_btn.bind('<ButtonRelease-1>', lambda event: change())
        quit_btn = tk.Button(self, image=self.quit_img, bd=0, bg='white')
        quit_btn.bind('<ButtonRelease-1>', lambda event: areyousure(event))

        # The Pack geometry manager packs widgets in rows or columns.
        # panel.pack(side = "bottom", fill = "both", expand = "yes")
        wel_panel.grid(row=0)
        tic_panel.grid(row=1)
        start_btn.grid(row=2, pady=5)
        howtoplay_btn.grid(row=3, pady=5)
        quit_btn.grid(row=4, pady=5)


class HowToPlay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = 'white'

        self.rules = []
        # global rule
        self.rule = 0
        global labl

        prev_path = r"D:\learning\Python\tic-tac-toe\left.png"
        next_path = r"D:\learning\Python\tic-tac-toe\right.png"
        rule1_path = r"D:\learning\Python\tic-tac-toe\horizontal.PNG"
        rule2_path = r"D:\learning\Python\tic-tac-toe\vertical.png"
        rule3_path = r"D:\learning\Python\tic-tac-toe\diagonal.PNG"
        gotit_path = r"D:\learning\Python\tic-tac-toe\button_got-it.png"

        self.prev_img = ImageTk.PhotoImage(Image.open(prev_path))
        self.next_img = ImageTk.PhotoImage(Image.open(next_path))
        self.rule1_img = ImageTk.PhotoImage(Image.open(rule1_path))
        self.rule2_img = ImageTk.PhotoImage(Image.open(rule2_path))
        self.rule3_img = ImageTk.PhotoImage(Image.open(rule3_path))
        self.gotit_img = ImageTk.PhotoImage(Image.open(gotit_path))
        self.rules = [self.rule1_img, self.rule2_img, self.rule3_img]

        def rule_change(event, cmnd):

            # global rule
            global labl
            # global labl
            if (cmnd == 'prev'):
                if (self.rule > 0):
                    self.rule = self.rule - 1
                    labl = tk.Label(self, image=self.rules[self.rule])
            if (cmnd == 'next'):
                if (self.rule < 2):
                    self.rule = self.rule + 1
                    labl = tk.Label(self, image=self.rules[self.rule])
            labl.grid(row=1, column=2)

        ins = tk.Label(self, font=('Arial', 18), text="Place it consecutively to win", width=0, fg='black',
                       bg='white')

        prev_btn = tk.Button(self, anchor='e', image=self.prev_img, bd=0, bg='white')
        prev_btn.bind('<ButtonRelease-1>', lambda event: rule_change(event, 'prev'))

        next_btn = tk.Button(self, anchor='e', image=self.next_img, bd=0, bg='white')
        next_btn.bind('<ButtonRelease-1>', lambda event: rule_change(event, 'next'))

        gotit_btn = tk.Button(self, image=self.gotit_img, bd=0, bg='white',
                              command=lambda: controller.show_frame(WelcomeScreen))

        labl = tk.Label(self, image=self.rules[self.rule])

        space = tk.Button(self, text='      ', bd=0)
        space.grid(row=2, column=0)
        ins.grid(row=0, column=2, pady=20)
        prev_btn.grid(row=1, column=1, padx=5)
        next_btn.grid(row=1, column=3, padx=5)
        labl.grid(row=1, column=2, padx=5, pady=10)
        gotit_btn.grid(row=2, column=2)


class PlayerSelect(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['bg'] = 'white'

        def getname(event, arg):
            spin_val = spin.get()
            if (int(spin_val) > 10):
                spin_val = 10
            elif (int(spin_val) < 1):
                spin_val = 1

            print(spin_val)
            name = []
            for i in range(0, 2):
                print(i)
                self.a = simpledialog.askstring("Player Name", "Please enter Player-" + str(i + 1) + " name")
                if self.a is None:
                    break
                name.append(self.a)
            print(name)

        head = tk.Label(self, text='VS', font=("Arial", 50), bg='white')
        player_btn = tk.Button(self, text='Player', font=("Arial ", 50), bg='white', fg='Black', width='10', bd=10)
        player_btn.bind('<ButtonRelease-1>', lambda event: getname(event, 'player'))

        comp_btn = tk.Button(self, text='Computer', font=("Arial ", 50), bg='Black', fg='white', width='10', bd=10)
        comp_btn.bind('<ButtonRelease-1>', lambda event: getname(event, 'computer'))

        spin = tk.Spinbox(self, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), width=5)
        space = tk.Label(self, text='*********', fg='white', bg='white')
        matches = tk.Label(self, text='Number of matches (1 to 10) :', font=("Arial", 15), bg='white')
        begin = tk.Button(self, text='Begin Game', font=("Arial", 15),
                          command=lambda: controller.show_frame(TicTacToeBoard))

        space.grid(row=0, column=0)
        head.grid(row=0, column=1, columnspan=2)
        matches.grid(row=1, column=1)
        spin.grid(row=1, column=2, pady=10)
        player_btn.grid(row=2, column=1, columnspan=2)
        comp_btn.grid(row=3, column=1, columnspan=2)
        begin.grid(row=4, column=1, columnspan=2)


class TicTacToeBoard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # global count, match_no, l, score_1, score_2

        self.match_no = 1
        self.count = 1
        self.score_1 = 0
        self.score_2 = 0
        self.l = list('a b c d e f g h i'.split())
        self.series = 3

        self.player1 = 'Donald Trump'
        self.player2 = 'Vladimir Putin'

        def transform(name, position):
            if (len(name) > 16):
                name = str(name[:14]) + '..'
            elif (len(name) == 0):
                name = 'Player-' + str(position)
            else:
                name = name
            return name

        self.pl1 = transform(self.player1.strip(), 1)
        self.pl2 = transform(self.player2.strip(), 2)

        # tic(5, pl1, pl2)

        def result(score_1, score_2):
            head = tk.Label(self, text='Score Table:', font=('Arial Italic', 13), bg='#D5D5D5', width='16',
                            height=3)
            score_1_lb = tk.Label(self, text=self.player1, font=('Arial Italic', 13))
            score_2_lb = tk.Label(self, text=self.player2, font=('Arial Italic', 13))
            val1 = tk.Label(self, text=str(score_1), font=('Arial Bold', 20), bg='white', relief='ridge',
                            width='10')
            val2 = tk.Label(self, text=str(score_2), font=('Arial Bold', 20), bg='white', relief='ridge',
                            width='10')

            head.grid(row=0, column=0, rowspan=2)
            score_1_lb.grid(row=0, column=1)
            score_2_lb.grid(row=0, column=2)
            val1.grid(row=1, column=1)
            val2.grid(row=1, column=2)

        def chg(event, r, c, f, s, fgf, fgs, pl1, pl2):
            # method to responds after a click event
            event.widget.grid_forget()
            #global count
            # print('count at chg',count)
            if ((self.count % 2) == 0):
                self.winfo_toplevel().title('Tic-Tac-Toe    Series :' + str(self.series) + '  Game :' +
                                            str(self.match_no - 1) + '   ' + str(pl1) + ' turn ')
                b = tk.Label(self, text=s, font=('Arial Bold', 105), width=2, height=1, bd=0, fg=fgf)

                b.grid(row=r, column=c)
                validate(r, c, pl2)
            else:
                self.winfo_toplevel().title('Tic-Tac-Toe    Series :' + str(self.series) + '  Game :' +
                                            str(self.match_no - 1) + '   ' + str(pl2) + ' turn ')
                b = tk.Label(self, text=f, font=('Arial Bold', 105), width=2, height=1, bd=0, fg=fgs)

                b.grid(row=r, column=c)
                validate(r, c, pl1)

        def validate(r, c, player):
            a = (r - 2) * 3 + c
            # global l
            # global count
            # global score_1
            # global score_2
            self.l[a] = player
            if (((self.l[0] == self.l[1]) & (self.l[1] == self.l[2])) | ((self.l[0] == self.l[4]) &
                                                                         (self.l[4] == self.l[8]))
                    | ((self.l[0] == self.l[3]) & (self.l[3] == self.l[6])) | ((self.l[3] == self.l[4]) &
                                                                               (self.l[4] == self.l[5]))
                    | ((self.l[1] == self.l[4]) & (self.l[4] == self.l[7])) | ((self.l[2] == self.l[5]) &
                                                                               (self.l[5] == self.l[8]))
                    | ((self.l[6] == self.l[7]) & (self.l[7] == self.l[8])) | ((self.l[2] == self.l[4]) &
                                                                               (self.l[4] == self.l[6]))):

                if (player == self.player1):
                    self.score_1 += 1
                    self.count = 0
                else:
                    self.score_2 += 1
                    self.count = 0

                # window.destroy()
                result(self.score_1, self.score_2)
                messagebox.showinfo('Congrats', str(player) + ' wins')
                board(self.player1, self.player2)

            self.count = self.count + 1

            if (self.count == 10):
                self.count = 1
                messagebox.showinfo('Tie', 'That is a tie , well played')
                board(self.player1, self.player2)
                # window.destroy()

        def board(player1, player2):

            # global l
            # global match_no
            self.l = list('a b c d e f g h i'.split())
            if self.match_no % 2 == 0:
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
                if self.score_1 > self.score_2:
                    winner = player1
                    message = str(player1) + ' wins the series'
                elif self.score_2 > self.score_1:
                    winner = player2
                    message = str(player2) + ' wins the series'
                else:
                    message = 'The series is a draw'
                messagebox.showinfo('Congrats to Champion', message)
                self.quit()

            def endgame(event):
                response = messagebox.askquestion("Quit", message='Are you sure you want to end this series, '
                                                                  'you will be navigated back to home screen')
                # print(response)
                if response == 'yes':
                    series_end()

            self.match_no += 1
            self.winfo_toplevel().title('Tic-Tac-Toe    Series :' + str(self.series) +
                                        '  Game :' + str(self.match_no - 1) + '   ' + str(pl1) + ' turn ')
            if self.match_no >= self.series + 2:
                series_end()

            # print("Count at board",count)
            b00 = tk.Button(self, fg='white', bg='white', bd=0, width=24, height=10)
            b00.grid(row=2, column=0)
            b00.bind('<Button-1>', lambda event: chg(event, 2, 0, f, s, fgf, fgs, pl1, pl2))

            b01 = tk.Button(self, fg='white', bg='#CECCCC', bd=0, width=24, height=10)
            b01.grid(row=2, column=1)
            b01.bind('<Button-1>', lambda event: chg(event, 2, 1, f, s, fgf, fgs, pl1, pl2))

            b02 = tk.Button(self, fg='white', bg='white', bd=0, width=24, height=10)
            b02.grid(row=2, column=2)
            b02.bind('<Button-1>', lambda event: chg(event, 2, 2, f, s, fgf, fgs, pl1, pl2))

            b10 = tk.Button(self, fg='white', bg='#CECCCC', bd=0, width=24, height=10)
            b10.grid(row=3, column=0)
            b10.bind('<Button-1>', lambda event: chg(event, 3, 0, f, s, fgf, fgs, pl1, pl2))

            b11 = tk.Button(self, fg='white', bg='white', bd=0, width=24, height=10)
            b11.grid(row=3, column=1)
            b11.bind('<Button-1>', lambda event: chg(event, 3, 1, f, s, fgf, fgs, pl1, pl2))

            b12 = tk.Button(self, fg='white', bg='#CECCCC', bd=0, width=24, height=10)
            b12.grid(row=3, column=2)
            b12.bind('<Button-1>', lambda event: chg(event, 3, 2, f, s, fgf, fgs, pl1, pl2))

            b20 = tk.Button(self, fg='white', bg='white', bd=0, width=24, height=10)
            b20.grid(row=4, column=0)
            b20.bind('<Button-1>', lambda event: chg(event, 4, 0, f, s, fgf, fgs, pl1, pl2))

            b21 = tk.Button(self, fg='white', bg='#CECCCC', bd=0, width=24, height=10)
            b21.grid(row=4, column=1)
            b21.bind('<Button-1>', lambda event: chg(event, 4, 1, f, s, fgf, fgs, pl1, pl2))

            b22 = tk.Button(self, fg='white', bg='white', bd=0, width=24, height=10)
            b22.grid(row=4, column=2)
            b22.bind('<Button-1>', lambda event: chg(event, 4, 2, f, s, fgf, fgs, pl1, pl2))

            end_game = tk.Button(self, width=43, height=2, text='End Game', font=('Arial Bold', 15), bd=3,
                                 relief='ridge')
            end_game.grid(row=5, column=0, columnspan=3)
            end_game.bind('<Button-1>', lambda event: endgame(event))

        board(self.player1, self.player2)
        result(self.score_1, self.score_2)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        startgame_path = r"D:\learning\Python\tic-tac-toe\button_start-game.png"
        startgame = ImageTk.PhotoImage(Image.open(startgame_path))
        button1 = tk.Button(self, image=startgame,
                            command=lambda: controller.show_frame(StartPage))

        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = SeaofBTCapp()

app.mainloop()
