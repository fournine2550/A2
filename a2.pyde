collum = 7
row = 6
cellsize = 80
off_x = 50
off_y = 50

board = []
current_player = 1
gameover = False  
winner = 0

black_score = 0
white_score = 0

def setup():
    size(700, 600)
    init_board()

def draw():
    background(240)
    draw_grid_2d()
    draw_ui()

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

def draw_ui():
    textSize(18)
    
    textAlign(LEFT, BOTTOM)
    fill(0)
    text("SCORE - Black: " + str(black_score) + " | White: " + str(white_score), off_x, off_y - 15)

    textAlign(LEFT, CENTER)
    if gameover == False:
        if current_player == 1:
            fill(0)
            text("Turn: Black Player | Press 'S' to Save, 'L' to Load", off_x, off_y + row * cellsize + 35)
        else:
            fill(120)
            text("Turn: White Player | Press 'S' to Save, 'L' to Load", off_x, off_y + row * cellsize + 35)
    else:
        if winner == 1:
            fill(0)
            text("BLACK WINS! (Click to restart)", off_x, off_y + row * cellsize + 35)
        elif winner == 2:
            fill(120)
            text("WHITE WINS! (Click to restart)", off_x, off_y + row * cellsize + 35)
        else:
            fill(80)
            text("DRAW GAME! (Click to restart)", off_x, off_y + row * cellsize + 35)

def mousePressed():
    global current_player, game_over
    
    if game_over == True:
        init_board()
        return
        
    if mouseX >= off_x and mouseX < off_x + collum * cellsize:
        col = int((mouseX - off_x) / cellsize)
        if drop_disc(col) == True:
            check_game_over()
            if game_over == False:
                if current_player == 1:
                    current_player =2
                else:
                    current_player = 1

def drop_disc(col):
    r = row - 1
    while r >= 0:
        if board[col][r] == 0:
            board[col][r] = current_player
            return True
        r -= 1
    return False

def check_game_over():
    global game_over, winner, black_score, white_score
    if check_board_win() == True:
        game_over = True
        winner = current_player
        
        if winner == 1:
            black_score += 1
        elif winner == 2:
            white_score += 1
            
    elif check_full_board():
        game_over = True
        winner = 0

def check_full_board():
    c = 0
    while c < GRID_COLS:
        if board[c][0] == 0:
            return False
        c += 1
    return True