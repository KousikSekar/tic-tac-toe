import pathlib

print(pathlib.Path().absolute())


class GameImages:
    path = str(pathlib.Path().absolute()) + r"\images"
    wel_path = path + r'\welcomescreenpng.png'
    icon_path = path + r'\TicTacToe2.png'
    startgame_path = path + r"\button_start-game.png"
    howtoplay_path = path + r"\button_how-to-play.png"
    quit_path = path + r"\button_quit.png"
    prev_path = path + r"\left.png"
    next_path = path + r"\right.png"
    rule1_path = path + r"\horizontal.PNG"
    rule2_path = path + r"\vertical.png"
    rule3_path = path + r"\diagonal.PNG"
    gotit_path = path + r"\button_got-it.png"

class Font:
    arial_18 = ('Arial',18)

class Background:
    welcomescreen = 'white'
    how_to_play = 'white'

class Foreground:
    how_to_play = 'Black'



