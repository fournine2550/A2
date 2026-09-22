collum = 7
row = 6
cellsize = 80
off_x = 50
off_y = 50

board = []
current_player = 1
gameover = False  
winner = 0

def setup():
    size(700, 600)
    init_board()

def draw():
    background(240)
    draw_grid_2d()

def init_board():
    global board, current_player, gameover, winner 
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
    gameover = False             
    winner = 0

def draw_grid_2d():
    c = 0
    while c < collum:
        r = 0
        while r < row:
            x1 = off_x + c * cellsize
            y1 = off_y + r * cellsize
            x2 = x1 + cellsize
            y2 = y1 + cellsize
            
            center_x = x1 + cellsize / 2
            center_y = y1 + cellsize / 2
            
            stroke(0)
            strokeWeight(2)
            line(x1, y1, x2, y1)  
            line(x1, y2, x2, y2)  
            line(x1, y1, x1, y2)  
            line(x2, y1, x2, y2)  
            
            val = board[c][r]
            if val == 1:
                fill(0)              
                stroke(0)
                ellipse(center_x, center_y, cellsize - 20, cellsize - 20)
            elif val == 2:
                fill(255)            
                stroke(0)
                ellipse(center_x, center_y, cellsize - 20, cellsize - 20)
            
            r += 1  
        c += 1