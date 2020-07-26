import pathlib

print(pathlib.Path().absolute())

# Button colour 101ccc
# dark mode #050940\
# box2 = #151E94
# box1 = #444A92
# box2_bright = #CECCCC
#score_table_bright = #D5D5D5
class Dark:
    class GameImages:
        path = str(pathlib.Path().absolute()) + r"\images"
        wel_path = path + r'\welcome_dark.png'
        icon_path = path + r'\TicTacToe2_dark.png'
        startgame_path = path + r"\button_start-game_dark.png"
        howtoplay_path = path + r"\button_how-to-play_dark.png"
        quit_path = path + r"\button_quit_dark.png"
        prev_path = path + r"\left_dark.png"
        next_path = path + r"\right_dark.png"
        rule1_path = path + r"\horizontal.PNG"
        rule2_path = path + r"\vertical.png"
        rule3_path = path + r"\diagonal.PNG"
        gotit_path = path + r"\button_got-it_dark.png"
        WelcomeScreen_ChangeTheme = path + r"\button_change-theme_dark.png"
        PlayerSelect_home = path + r"\button_home_dark.png"
        PlayerSelect_Player = path + r"\button_player_dark.png"
        PlayerSelect_Computer = path + r"\button_computer_dark.png"
        PlayerDetails_back = path + r"\button_back_dark.png"
        PlayerDetails_begin = path + r"\button_begin-game_dark.png"
        PlayerDetails_home = path + r"\button_home_dark.png"


    class Font:
        arial_18 = ('Arial',18)
        text_color = 'white'
        Lounge = '#74DB8F'

    class Background:
        welcomescreen = '#050940'
        how_to_play = '#050940'
        PlayerSelect = '#050940'
        PlayerDetails = '#050940'
        TicTacToe = '#050940'

    class Foreground:
        how_to_play = 'Black'

    class TicTacToe:
        odd_box = '#444A92'
        even_box = '#151C81'
        score_board = '#151E94'
        color_O = '#B7DC24'
        color_x = '#CACEB8'



class Bright:
    class GameImages:
        path = str(pathlib.Path().absolute()) + r"\images"
        wel_path = path + r'\welcome_dark.png'
        icon_path = path + r'\TicTacToe2.png'
        startgame_path = path + r"\button_start-game.png"
        howtoplay_path = path + r"\button_how-to-play.png"
        quit_path = path + r"\button_quit.png"
        prev_path = path + r"\left.png"
        next_path = path + r"\right.png"
        rule1_path = path + r"\horizontal.PNG"
        rule2_path = path + r"\vertical.png"
        rule3_path = path + r"\diagonal.PNG"
        gotit_path = path + r"\button_got-it_bright.png"
        WelcomeScreen_ChangeTheme = path + r"\button_change-theme_bright.png"
        PlayerSelect_home = path + r"\button_home_bright.png"
        PlayerSelect_Player = path + r"\button_player_bright.png"
        PlayerSelect_Computer = path + r"\button_computer_bright.png"
        PlayerDetails_back = path + r"\button_back_bright.png"
        PlayerDetails_begin = path + r"\button_begin-game_bright.png"
        PlayerDetails_home = path + r"\button_home_bright.png"

    class Font:
        arial_18 = ('Arial', 18)
        text_color = 'black'
        Lounge = '#6A7D1F'

    class Background:
        welcomescreen = 'white'
        how_to_play = 'white'
        PlayerSelect = 'white'
        PlayerDetails = 'white'
        TicTacToe = 'white'

    class Foreground:
        how_to_play = 'Black'

    class TicTacToe:
        odd_box = 'white'
        even_box = '#CECCCC'
        score_board = '#D5D5D5'
        color_O = 'red'
        color_x = 'black'







