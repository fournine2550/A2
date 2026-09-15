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

def create_1darray(length):
    if length <=0:
        return []
    return[0]+create_1darray(length-1)

def create_2darray(cols, rows):
    if cols <= 0:
        return []                                 
    return [create_1darray(rows)] + create_2d_array(cols - 1, rows)