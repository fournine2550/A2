collum = 7
row = 6
size = 80
off_x = 50
off_y = 50

board = []
current_player = 1
gameover = Flase
winner = 0
def setup():
    size(600,600)
    
def draw():
    background(240)

def init_board():
    global board, current_player, game_over, winner
    board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    current_player = 1                            
    game_over = False                             
    winner = 0