import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from PIL import ImageTk, Image

LARGE_FONT = ('Arial', 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Tic-Tac-Toe')
        self.geometry('520x470')

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=2)


        self.frames = {}

        for F in (WelcomeScreen, HowToPlay, PlayerSelect):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomeScreen)

    def show_frame(self, cont,*args):
        frame = self.frames[cont]
        frame.tkraise()



class WelcomeScreen(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
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
                              command = lambda : controller.show_frame(PlayerSelect))
        howtoplay_btn = tk.Button(self, image=self.howtoplay, bd=0, bg='white',
                                  command = lambda : controller.show_frame(HowToPlay))
        #howtoplay_btn.bind('<ButtonRelease-1>', lambda event: change())
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
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self['bg'] = 'white'

        self.rules = []
        #global rule
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

            #global rule
            global labl
            #global labl
            if (cmnd == 'prev'):
                if (self.rule > 0):
                    self.rule = self.rule - 1
                    labl = tk.Label(self,image=self.rules[self.rule])
            if (cmnd == 'next'):
                if (self.rule < 2):
                    self.rule = self.rule + 1
                    labl = tk.Label(self,image=self.rules[self.rule])
            labl.grid(row=1, column=2)

        ins = tk.Label(self, font=('Arial', 18), text="Place it consecutively to win", width=0, fg='black',
                       bg='white')

        prev_btn = tk.Button(self, anchor='e', image=self.prev_img, bd=0, bg='white')
        prev_btn.bind('<ButtonRelease-1>', lambda event: rule_change(event, 'prev'))

        next_btn = tk.Button(self, anchor='e', image=self.next_img, bd=0, bg='white')
        next_btn.bind('<ButtonRelease-1>', lambda event: rule_change(event, 'next'))

        gotit_btn = tk.Button(self, image=self.gotit_img, bd=0, bg='white',
                              command = lambda : controller.show_frame(WelcomeScreen) )

        labl = tk.Label(self, image=self.rules[self.rule])

        space = tk.Button(self, text='      ', bd=0)
        space.grid(row=2, column=0)
        ins.grid(row=0, column=2, pady=20)
        prev_btn.grid(row=1, column=1, padx=5)
        next_btn.grid(row=1, column=3, padx=5)
        labl.grid(row=1, column=2, padx=5, pady=10)
        gotit_btn.grid(row=2, column=2)

class PlayerSelect(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self['bg'] = 'white'
        def getname(event, arg):
            spin_val = spin.get()
            if (int(spin_val) > 10):
                spin_val = 10
            elif (int(spin_val) < 1):
                spin_val = 1

            print(spin_val)
            name = []
            for i in range(0,2):
                print(i)
                self.a = simpledialog.askstring("Player Name", "Please enter Player-"+str(i+1)+" name")
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
        begin = tk.Button(self,text='Begin Game',font=("Arial", 15))

        space.grid(row=0, column=0)
        head.grid(row=0, column=1, columnspan=2)
        matches.grid(row=1, column=1)
        spin.grid(row=1, column=2, pady=10)
        player_btn.grid(row=2, column=1, columnspan=2)
        comp_btn.grid(row=3, column=1, columnspan=2)
        begin.grid(row=4,column=1,columnspan=2)


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