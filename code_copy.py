import pathlib
import sys

path = pathlib.Path().absolute()
sys.path.insert(1, path)
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import property_file
import random

class StartApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('527x615')
        self.resizable(0, 0)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=2)
        self.container.grid_columnconfigure(0, weight=2)
        self.theme = property_file.Bright
        self.frames = {}
        self.board = WelcomeScreen(self.container, self, self.theme)

        StartApp.loadframes(self, self.theme, self.container)
        self.show_frame(WelcomeScreen, self.theme)

    def loadframes(self, theme_class, root):
        self.theme = theme_class
        self.frames = {}
        self.container = root
        for F in (TicTacToeBoard, WelcomeScreen, HowToPlay, PlayerSelect, PlayerDetails):
            frame = F(self.container, self, self.theme)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont, theme, *args):
        self.theme = theme
        self.title('Tic-Tac-Toe')
        if str(cont) == "<class '__main__.TicTacToeBoard'>":
            self.board = TicTacToeBoard(self.container, self, self.theme, args[0], args[1], args[2])
            frame = self.board
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()
        else:
            self.title('Tic-Tac-Toe')
            self.board = cont(self.container, self, self.theme)
            frame = self.board
            frame.grid(row=0, column=0, sticky='nsew')
            frame.tkraise()


class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller, theme):
        tk.Frame.__init__(self, parent)
        self['bg'] = theme.Background.welcomescreen
        self.winfo_toplevel().title('Tic-Tac-Toe')
        self.parent = parent
        self.controller = controller

        if str(theme) == "<class 'property_file.Dark'>":
            change_theme = property_file.Bright
        else:
            change_theme = property_file.Dark

        wel_path = theme.GameImages.wel_path
        tic_path = theme.GameImages.icon_path
        startgame_path = theme.GameImages.startgame_path
        howtoplay_path = theme.GameImages.howtoplay_path
        quit_path = theme.GameImages.quit_path

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        self.wel_img = ImageTk.PhotoImage(Image.open(wel_path))
        self.tic_img = ImageTk.PhotoImage(Image.open(tic_path))
        self.startgame = ImageTk.PhotoImage(Image.open(startgame_path))
        self.howtoplay = ImageTk.PhotoImage(Image.open(howtoplay_path))
        self.quit_img = ImageTk.PhotoImage(Image.open(quit_path))

        wel_panel = tk.Label(self, image=self.wel_img, anchor='n', background=theme.Background.welcomescreen,
                             )
        tic_panel = tk.Label(self, image=self.tic_img, anchor='n', background=theme.Background.welcomescreen,
                             width=530)
        start_btn = tk.Button(self, image=self.startgame, bd=0, bg=theme.Background.welcomescreen,
                              activebackground=theme.Background.welcomescreen,
                              command=lambda: controller.show_frame(PlayerSelect, theme))
        howtoplay_btn = tk.Button(self, image=self.howtoplay, bd=0, bg=theme.Background.welcomescreen,
                                  activebackground=theme.Background.welcomescreen,
                                  command=lambda: controller.show_frame(HowToPlay, theme))
        quit_btn = tk.Button(self, image=self.quit_img, bd=0, bg=theme.Background.welcomescreen,
                             activebackground=theme.Background.welcomescreen)
        quit_btn.bind('<ButtonRelease-1>', lambda event: WelcomeScreen.are_you_sure(self))
        space = tk.Label(self, text='***', anchor='n', background=theme.Background.welcomescreen,
                         fg=theme.Background.welcomescreen, width=7)
        self.chng_theme = ImageTk.PhotoImage(Image.open(theme.GameImages.WelcomeScreen_ChangeTheme))
        chng_btn = tk.Button(self, image=self.chng_theme, bd=0, bg=theme.Background.welcomescreen,
                             activebackground=theme.Background.welcomescreen,
                             command=lambda: controller.show_frame(WelcomeScreen, change_theme))
        # StartApp.loadframes(self,property_file.Bright,self.parent)
        wel_panel.grid(row=0)
        tic_panel.grid(row=1)
        start_btn.grid(row=2, pady=5)
        howtoplay_btn.grid(row=3, pady=5)
        quit_btn.grid(row=5, pady=5)
        space.grid(row=6, pady=35)
        chng_btn.grid(row=4, pady=5)

    def are_you_sure(self):
        response = messagebox.askquestion("Quit", message='Are you sure you want to quit')
        if response == 'yes':
            self.quit()


class HowToPlay(tk.Frame):
    def __init__(self, parent, controller, theme):
        tk.Frame.__init__(self, parent)
        self['bg'] = theme.Background.how_to_play
        self.rules = []
        self.rule = 0
        self.labl = tk.Label(self)

        prev_path = theme.GameImages.prev_path
        next_path = theme.GameImages.next_path
        rule1_path = theme.GameImages.rule1_path
        rule2_path = theme.GameImages.rule2_path
        rule3_path = theme.GameImages.rule3_path
        gotit_path = theme.GameImages.gotit_path

        self.prev_img = ImageTk.PhotoImage(Image.open(prev_path))
        self.next_img = ImageTk.PhotoImage(Image.open(next_path))
        self.rule1_img = ImageTk.PhotoImage(Image.open(rule1_path))
        self.rule2_img = ImageTk.PhotoImage(Image.open(rule2_path))
        self.rule3_img = ImageTk.PhotoImage(Image.open(rule3_path))
        self.gotit_img = ImageTk.PhotoImage(Image.open(gotit_path))
        self.rules = [self.rule1_img, self.rule2_img, self.rule3_img]

        ins = tk.Label(self, font=theme.Font.arial_18, text="Place it consecutively to win", width=0,
                       fg=theme.Font.text_color, bg=theme.Background.how_to_play)
        prev_btn = tk.Button(self, anchor='e', image=self.prev_img, bd=0, bg=theme.Background.how_to_play,
                             activebackground=theme.Background.how_to_play)
        prev_btn.bind('<ButtonRelease-1>', lambda event: HowToPlay.rule_change(self, 'prev'))
        next_btn = tk.Button(self, anchor='e', image=self.next_img, bd=0, bg=theme.Background.how_to_play,
                             activebackground=theme.Background.how_to_play, )
        next_btn.bind('<ButtonRelease-1>', lambda event: HowToPlay.rule_change(self, 'next'))
        gotit_btn = tk.Button(self, image=self.gotit_img, bd=0, bg=theme.Background.how_to_play,
                              activebackground=theme.Background.how_to_play,
                              command=lambda: controller.show_frame(WelcomeScreen, theme))
        labl = tk.Label(self, image=self.rules[self.rule])

        space = tk.Button(self, text='      ', bd=0, bg=theme.Background.how_to_play)
        space.grid(row=2, column=0)
        ins.grid(row=0, column=2, pady=20)
        prev_btn.grid(row=1, column=1, padx=5)
        next_btn.grid(row=1, column=3, padx=5)
        labl.grid(row=1, column=2, padx=5, pady=10)
        gotit_btn.grid(row=2, column=2)

    def rule_change(self, cmnd, ):
        if cmnd == 'prev':
            if self.rule > 0:
                self.rule = self.rule - 1
                self.labl = tk.Label(self, image=self.rules[self.rule])
        if cmnd == 'next':
            if self.rule < 2:
                self.rule = self.rule + 1
                self.labl = tk.Label(self, image=self.rules[self.rule])
        self.labl.grid(row=1, column=2)


class PlayerSelect(tk.Frame):
    def __init__(self, parent, controller, theme):
        tk.Frame.__init__(self, parent)
        self.name = []
        self.controller = controller
        self['bg'] = theme.Background.PlayerSelect
        space_top = tk.Label(self, text='*', height=2, bg=theme.Background.PlayerSelect,
                             fg=theme.Background.PlayerSelect)
        head = tk.Label(self, text='Choose your Game Mode', font=("Arial", 20), fg=theme.Font.text_color,
                        bg=theme.Background.PlayerSelect)
        self.player_img = ImageTk.PhotoImage(Image.open(theme.GameImages.PlayerSelect_Player))
        player_btn = tk.Button(self, image=self.player_img, bg=theme.Background.PlayerSelect, bd=0
                               , activebackground=theme.Background.PlayerSelect,
                               command=lambda: controller.show_frame(PlayerDetails, theme))
        self.comp_img = ImageTk.PhotoImage(Image.open(theme.GameImages.PlayerSelect_Computer))
        comp_btn = tk.Button(self, image=self.comp_img, bg=theme.Background.PlayerSelect, bd=0,
                             activebackground=theme.Background.PlayerSelect
                             , command=lambda: PlayerSelect.computer(self))
        space_left = tk.Label(self, text='*****************', fg=theme.Background.PlayerSelect,
                              bg=theme.Background.PlayerSelect)
        self.home_img = ImageTk.PhotoImage(Image.open(theme.GameImages.PlayerSelect_home))
        home = tk.Button(self, image=self.home_img, bd=0, bg=theme.Background.PlayerSelect
                         , activebackground=theme.Background.PlayerSelect,
                         command=lambda: controller.show_frame(WelcomeScreen, theme))

        space_top.grid(row=0, column=0)
        space_left.grid(row=0, column=0)
        head.grid(row=1, column=1, columnspan=2, padx=10, pady=20)
        player_btn.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        comp_btn.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        home.grid(row=5, column=1, columnspan=2, padx=10, pady=20)

    def computer(self):
        messagebox.showwarning("Sorry", "Under construction , see you in next update")


class PlayerDetails(tk.Frame):
    def __init__(self, parent, controller, theme):
        tk.Frame.__init__(self, parent)
        self.theme = theme
        self['bg'] = theme.Background.PlayerDetails
        self.spin = 3
        self.controller = controller
        heading_left = tk.Label(self, text="         Player's", font=('Arial Italic', 30), anchor='ne',
                                fg=theme.Font.Lounge, bg=theme.Background.PlayerDetails, width=9)
        heading_right = tk.Label(self, text="Lounge          ", font=('Arial Italic', 30), anchor='nw',
                                 fg=theme.Font.Lounge, bg=theme.Background.PlayerDetails, width=9)

        line = tk.Label(self, text="=> You're just one step away =>", font=('Arial Italic', 17), anchor='n',
                        bg=theme.Background.PlayerDetails, fg=theme.Font.text_color)
        line1 = tk.Label(self, text='Please enter details below : ', font=('Arial', 12), anchor='nw',
                         bg=theme.Background.PlayerDetails, fg=theme.Font.text_color)
        line2 = tk.Label(self, text='First Player Name :', font=('Arial', 10), anchor='nw',
                         bg=theme.Background.PlayerDetails, fg=theme.Font.text_color)
        line3 = tk.Label(self, text='Second Player Name :', font=('Arial', 10), anchor='nw',
                         bg=theme.Background.PlayerDetails, fg=theme.Font.text_color)
        line4 = tk.Label(self, text='Number of Games to Play :    \nEnter a value between 1 to 10'
                         , font=('Arial', 10), anchor='w', bg=theme.Background.PlayerDetails, fg=theme.Font.text_color)

        self.text2 = tk.Text(self, height=1, width=20)
        self.text3 = tk.Text(self, height=1, width=20)
        self.text4 = tk.Spinbox(self, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), width=10)
        space_left = tk.Label(self, text='**', bg=theme.Background.PlayerDetails,
                              fg=theme.Background.PlayerDetails)
        space_right = tk.Label(self, text='********', bg=theme.Background.PlayerDetails,
                               fg=theme.Background.PlayerDetails)
        space_top = tk.Label(self, text='*', height=1,
                             bg=theme.Background.PlayerDetails, fg=theme.Background.PlayerDetails,
                             )
        self.back_img = ImageTk.PhotoImage(Image.open(theme.GameImages.PlayerDetails_back))
        back = tk.Button(self, image=self.back_img, bd=0,
                         bg=theme.Background.PlayerDetails, activebackground=theme.Background.PlayerDetails,
                         command=lambda: controller.show_frame(PlayerSelect, theme))
        self.begin_img = ImageTk.PhotoImage(Image.open(theme.GameImages.PlayerDetails_begin))
        begin = tk.Button(self, image=self.begin_img, bd=0,
                          bg=theme.Background.PlayerDetails, activebackground=theme.Background.PlayerDetails,
                          command=lambda: PlayerDetails.startgame(self, self.text2.get("1.0", "end-1c")
                                                                  , self.text3.get("1.0", "end-1c"),
                                                                  self.text4.get()))
        self.home_img = ImageTk.PhotoImage(Image.open(theme.GameImages.PlayerDetails_home))
        home = tk.Button(self, image=self.home_img, bd=0,
                         bg=theme.Background.PlayerDetails, activebackground=theme.Background.PlayerDetails,
                         command=lambda: controller.show_frame(WelcomeScreen, theme))
        space_top.grid(row=0)
        space_left.grid(row=1, column=0, padx=10, pady=10)
        space_right.grid(row=1, column=3, padx=10, pady=10)

        heading_left.grid(row=1, column=1, padx=10, pady=0)
        heading_right.grid(row=1, column=2, padx=10, pady=10)
        line.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        line1.grid(row=3, column=1, padx=10, pady=10)
        line2.grid(row=4, column=1, sticky='w', padx=10, pady=10)
        self.text2.grid(row=4, column=2, sticky='w', padx=10, pady=10)
        line3.grid(row=5, column=1, sticky='w', padx=10, pady=10)
        self.text3.grid(row=5, column=2, sticky='w', padx=10, pady=10)
        line4.grid(row=6, column=1, sticky='w', padx=10, pady=10)
        self.text4.grid(row=6, column=2, sticky='w', padx=10, pady=10)
        back.grid(row=7, column=1, padx=10, pady=10)
        begin.grid(row=7, column=2, padx=10, pady=10)
        home.grid(row=8, column=1, columnspan=2, sticky='n')

    def startgame(self, *args):
        pl1_name = args[0]
        pl2_name = args[1]
        matches = PlayerDetails.get_spin(self, args[2])
        self.controller.show_frame(TicTacToeBoard, self.theme, pl1_name, pl2_name, matches)

    def get_spin(self, *args):
        if int(args[0]) > 10:
            self.spin = 10
        elif int(args[0]) < 1:
            self.spin = 1
        else:
            self.spin = args[0]
        return self.spin


class TicTacToeBoard(tk.Frame):
    def __init__(self, parent, controller, theme, *args):
        tk.Frame.__init__(self, parent)
        self['bg'] = theme.Background.TicTacToe
        self.theme = theme
        self.controller = controller
        self.match_no = 1
        self.count = 1
        self.score_1 = 0
        self.score_2 = 0
        self.l = list('a b c d e f g h i'.split())

        try:
            self.player1 = str(args[0])
        except:
            self.player1 = ''

        try:
            self.player2 = str(args[1])
        except:
            self.player2 = ''

        try:
            self.series = int(args[2])
        except:
            self.series = 3

        self.pl1 = TicTacToeBoard.transform(self, self.player1.strip(), 1)
        self.pl2 = TicTacToeBoard.transform(self, self.player2.strip(), 2)
        TicTacToeBoard.board(self, self.pl1, self.pl2)
        TicTacToeBoard.result(self, self.score_1, self.score_2)

    def transform(self, name, position):
        if len(name) > 16:
            name = str(name[:14]) + '..'
        elif (len(name) == 0) | (name == ''):
            name = 'Player-' + str(position)
        else:
            name = name
        return name

    def result(self, score_1, score_2):
        head = tk.Label(self, text='Score Table:', font=('Arial Italic', 13), width='16',
                        height=3, bg=self.theme.TicTacToe.even_box, fg=self.theme.Font.text_color)
        score_1_lb = tk.Label(self, text=self.pl1, font=('Arial Italic', 13),
                              fg=self.theme.Font.text_color, bg=self.theme.Background.TicTacToe)
        score_2_lb = tk.Label(self, text=self.pl2, font=('Arial Italic', 13),
                              fg=self.theme.Font.text_color, bg=self.theme.Background.TicTacToe)
        val1 = tk.Label(self, text=str(score_1), font=('Arial Bold', 20), bg='white', relief='ridge',
                        width='9')
        val2 = tk.Label(self, text=str(score_2), font=('Arial Bold', 20), bg='white', relief='ridge',
                        width='9')

        head.grid(row=0, column=0, rowspan=2)
        score_1_lb.grid(row=0, column=1)
        score_2_lb.grid(row=0, column=2)
        val1.grid(row=1, column=1)
        val2.grid(row=1, column=2)

    def chg(self, event, r, c, f, s, fgf, fgs, pl1, pl2):
        event.widget.grid_forget()
        print('match_no : ',self.match_no)
        # self.count = 1
        # if self.match_no % 2 == 0:
        #     f = 'O'
        #     s = 'X'
        #     fgs = self.theme.TicTacToe.color_O
        #     fgf = self.theme.TicTacToe.color_x
        #     pl1 = player2
        #     pl2 = player1
        # else:
        #     f = 'X'
        #     s = 'O'
        #     fgs = self.theme.TicTacToe.color_x
        #     fgf = self.theme.TicTacToe.color_O
        #     pl1 = player1
        #     pl2 = player2
        if (self.count % 2) == 0:
            print('count at if block in chg :',self.count)
            self.winfo_toplevel().title('Tic-Tac-Toe    Series of ' + str(self.series) + ' game ;  Game :' +
                                        str(self.match_no - 1) + '   ' + str(pl1) + ' turn ')
            b = tk.Label(self, text=s, font=('Arial Bold', 105), width=2, height=1, bd=0, fg=fgf,
                         bg=self.theme.Background.TicTacToe)

            b.grid(row=r, column=c)
            stopper = TicTacToeBoard.validate(self, r, c, pl2)
            if(str(pl1) == 'computer') & (stopper!=2):
                TicTacToeBoard.computer(self, f, s, fgf, fgs, pl1, pl2)


        else:
            print('count at else block in chg :', self.count)
            self.winfo_toplevel().title('Tic-Tac-Toe    Series of ' + str(self.series) + ' game ;  Game :' +
                                        str(self.match_no - 1) + '   ' + str(pl2) + ' turn ')
            b = tk.Label(self, text=f, font=('Arial Bold', 105), width=2, height=1, bd=0, fg=fgs,
                         bg=self.theme.Background.TicTacToe)
            b.grid(row=r, column=c)
            stopper = TicTacToeBoard.validate(self, r, c, pl1)
            print('stopper : ',stopper)

            if (str(pl2) == 'computer')& (self.count>1)& (stopper!=2):
                print('method inside chg executed')
                TicTacToeBoard.computer(self, f, s, fgf, fgs, pl1, pl2)

    def validate(self, r, c, player):
        a = (r - 2) * 3 + c
        self.l[a] = player
        if (((self.l[0] == self.l[1]) & (self.l[1] == self.l[2])) | ((self.l[0] == self.l[4]) &
                                                                     (self.l[4] == self.l[8]))
                | ((self.l[0] == self.l[3]) & (self.l[3] == self.l[6])) | ((self.l[3] == self.l[4]) &
                                                                           (self.l[4] == self.l[5]))
                | ((self.l[1] == self.l[4]) & (self.l[4] == self.l[7])) | ((self.l[2] == self.l[5]) &
                                                                           (self.l[5] == self.l[8]))
                | ((self.l[6] == self.l[7]) & (self.l[7] == self.l[8])) | ((self.l[2] == self.l[4]) &
                                                                           (self.l[4] == self.l[6]))):

            if player == self.pl1:
                self.score_1 += 1
                self.count = 0

            else:
                self.score_2 += 1
                self.count = 0

            TicTacToeBoard.result(self, self.score_1, self.score_2)
            messagebox.showinfo('Congrats', str(player) + ' wins')
            TicTacToeBoard.board(self, self.pl1, self.pl2)
            return 2

        self.count = self.count + 1

        if self.count == 10:
            self.count = 1
            messagebox.showinfo('Tie', 'That is a tie , well played')
            TicTacToeBoard.board(self, self.pl1, self.pl2)
            return 2

    def board(self, player1, player2):
        self.l = list('a b c d e f g h i'.split())
        self.stopper = 0
        if self.match_no % 2 == 0:
            f = 'O'
            s = 'X'
            fgs = self.theme.TicTacToe.color_O
            fgf = self.theme.TicTacToe.color_x
            pl1 = player2
            pl2 = player1
        else:
            f = 'X'
            s = 'O'
            fgs = self.theme.TicTacToe.color_x
            fgf = self.theme.TicTacToe.color_O
            pl1 = player1
            pl2 = player2

        def series_end():
            self.winfo_toplevel().title('Tic-Tac-Toe    Series of ' + str(self.series) + ' game')
            if self.score_1 > self.score_2:
                message = str(player1) + ' wins the series'
            elif self.score_2 > self.score_1:
                message = str(player2) + ' wins the series'
            else:
                message = 'The series is a draw'
            messagebox.showinfo('Congrats to Champion', message)
            self.controller.show_frame(WelcomeScreen, self.theme)

        def endgame(event):
            response = messagebox.askquestion("Quit", message='Are you sure you want to end this series, '
                                                              'you will be navigated back to home screen')
            if response == 'yes':
                series_end()

        self.match_no += 1
        self.winfo_toplevel().title('Tic-Tac-Toe    Series of ' + str(self.series) +
                                    ' game ;  Game :' + str(self.match_no - 1) + '   ' + str(pl1) + ' turn ')
        if self.match_no >= self.series + 2:
            series_end()
            print('series end executed')
            self.stopper = 2
            return 0

        b00 = tk.Button(self, bg=self.theme.TicTacToe.odd_box, bd=0, width=24, height=10)
        b00.grid(row=2, column=0)
        b00.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 2, 0, f, s, fgf, fgs, pl1, pl2))

        b01 = tk.Button(self, bg=self.theme.TicTacToe.even_box, bd=0, width=24, height=10)
        b01.grid(row=2, column=1)
        b01.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 2, 1, f, s, fgf, fgs, pl1, pl2))

        b02 = tk.Button(self, bg=self.theme.TicTacToe.odd_box, bd=0, width=24, height=10)
        b02.grid(row=2, column=2)
        b02.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 2, 2, f, s, fgf, fgs, pl1, pl2))

        b10 = tk.Button(self, bg=self.theme.TicTacToe.even_box, bd=0, width=24, height=10)
        b10.grid(row=3, column=0)
        b10.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 3, 0, f, s, fgf, fgs, pl1, pl2))

        b11 = tk.Button(self, bg=self.theme.TicTacToe.odd_box, bd=0, width=24, height=10)
        b11.grid(row=3, column=1)
        b11.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 3, 1, f, s, fgf, fgs, pl1, pl2))

        b12 = tk.Button(self, bg=self.theme.TicTacToe.even_box, bd=0, width=24, height=10)
        b12.grid(row=3, column=2)
        b12.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 3, 2, f, s, fgf, fgs, pl1, pl2))

        b20 = tk.Button(self, bg=self.theme.TicTacToe.odd_box, bd=0, width=24, height=10)
        b20.grid(row=4, column=0)
        b20.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 4, 0, f, s, fgf, fgs, pl1, pl2))

        b21 = tk.Button(self, bg=self.theme.TicTacToe.even_box, bd=0, width=24, height=10)
        b21.grid(row=4, column=1)
        b21.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 4, 1, f, s, fgf, fgs, pl1, pl2))

        b22 = tk.Button(self, bg=self.theme.TicTacToe.odd_box, bd=0, width=24, height=10)
        b22.grid(row=4, column=2)
        b22.bind('<Button-1>', lambda event: TicTacToeBoard.chg(self, event, 4, 2, f, s, fgf, fgs, pl1, pl2))

        end_game = tk.Button(self, width=43, height=2, text='End Game', font=('Arial Bold', 15), bd=3,
                             fg=self.theme.Font.text_color, bg=self.theme.TicTacToe.score_board,
                             activebackground=self.theme.TicTacToe.score_board,
                             activeforeground=self.theme.Font.text_color)
        end_game.grid(row=5, column=0, columnspan=3)
        end_game.bind('<ButtonRelease-1>', lambda event: endgame(event))
        if(self.match_no%2 !=0)&(self.stopper!=2):
            print('method inside board executed')
            self.count = self.count + 1
            TicTacToeBoard.computer(self, f, s, fgf, fgs, pl1, pl2)



    def computer(self, f, s, fgf, fgs, pl1, pl2):
        print('f',f)
        print('s',s)
        print('count at computer',self.count)
        print(self.l)
        main_list = self.l
        compute = []
        for i in main_list:
            if (i == 'a') | (i == 'b') | (i == 'c') | (i == 'd') | (i == 'e') | (i == 'f') | (i == 'g') | (i == 'h') | (
                    i == 'i'):
                compute.append(i)
        write = random.choice(compute)
        print('compute',write)
        row_col = main_list.index(write)
        print('rowcol',row_col)
        r = (row_col//3) + 2
        c = row_col%3
        a = (r - 2) * 3 + c
        if (self.count%2 !=0)|(self.count==0):
            b = tk.Label(self, text=f, font=('Arial Bold', 105), width=2, height=1, bd=0, fg=fgs,
                         bg=self.theme.Background.TicTacToe)
            b.grid(row=r, column=c)
            TicTacToeBoard.validate(self, r, c, pl1)
            self.winfo_toplevel().title('Tic-Tac-Toe    Series of ' + str(self.series) + ' game ;  Game :' +
                                        str(self.match_no - 1) + '   ' + str(pl2) + ' turn ')

        else:
            b = tk.Label(self, text=s, font=('Arial Bold', 105), width=2, height=1, bd=0, fg=fgf,
                             bg=self.theme.Background.TicTacToe)
            b.grid(row=r, column=c)
            TicTacToeBoard.validate(self, r, c, pl2)
            self.winfo_toplevel().title('Tic-Tac-Toe    Series of ' + str(self.series) + ' game ;  Game :' +
                                        str(self.match_no - 1) + '   ' + str(pl1) + ' turn ')



        print('\n computer executed')
        pass


print('Developed by Kousik \n DEVELOPED BY KOUSIK')
app = StartApp()
app.mainloop()
