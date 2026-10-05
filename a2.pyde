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
    global current_player, gameover
    
    if gameover == True:
        init_board()
        return
        
    if mouseX >= off_x and mouseX < off_x + collum * cellsize:
        col = int((mouseX - off_x) / cellsize)
        if drop_disc(col) == True:
            check_game_over()
            if gameover == False:
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
    global gameover, winner, black_score, white_score
    if check_board_win() == True:
        gameover = True
        winner = current_player
        
        if winner == 1:
            black_score += 1
        elif winner == 2:
            white_score += 1
            
    elif check_full_board():
        gameover = True
        winner = 0

def check_full_board():
    c = 0
    while c < collum:
        if board[c][0] == 0:
            return False
        c += 1
    return True

def check_board_win():
    c = 0
    while c < collum:
        r = 0
        while r < row:
            p = board[c][r]
            if p != 0:
                if (check_direction(c, r, 1, 0, p) or 
                    check_direction(c, r, 0, 1, p) or 
                    check_direction(c, r, 1, 1, p) or 
                    check_direction(c, r, 1, -1, p)):
                    return True
            r += 1
        c += 1
    return False
def check_direction(c, r, dc, dr, player):
    step = 0
    while step < 4:
        nc = c + dc * step
        nr = r + dr * step
        if nc < 0 or nc >= collum or nr < 0 or nr >= row:
            return False
        if board[nc][nr] != player:
            return False
        step += 1
    return True

def save_game():
    global board, current_player, gameover, black_score, white_score

    board_string = ""
    c = 0
    while c < collum:
        r = 0
        while r < row:
            board_string += str(board[c][r])
            r += 1
        c += 1
            
    save_data = board_string + "|" + str(current_player) + "|" + str(black_score) + "|" + str(white_score)
    
    save_path = sketchPath("c4_save.txt")
    
    with open(save_path, "w") as f:
        f.write(save_data)
    print("[ระบบ]: บันทึกเกมและคะแนนสำเร็จแล้ว!")

def load_game():
    global board, current_player, gameover, winner, black_score, white_score
    
    save_path = sketchPath("c4_save.txt")
    
    if not os.path.exists(save_path):
        print("[ระบบ]: ไม่พบไฟล์เซฟ")
        return
        
    try:
        with open(save_path, "r") as f:
            save_data = f.read()
            
        parts = save_data.split("|")
        board_part = parts[0]
        current_player = int(parts[1])
        
        if len(parts) >= 4:
            black_score = int(parts[2])
            white_score = int(parts[3])
            
        gameover = False
        winner = 0
        
        new_board = []
        idx = 0
        c = 0
        while c < collum:
            col_data = []
            r = 0
            while r < row:
                col_data.append(int(board_part[idx]))
                idx += 1
                r += 1
            new_board.append(col_data)
            c += 1
            
        board = new_board
        print("[ระบบ]: โหลดเกมและคะแนนสำเร็จแล้ว!")
        
    except Exception as e:
        print("[ข้อผิดพลาด]: ไฟล์เซฟเสียหาย:", e)

def keyPressed():
    if key == 's' or key == 'S':
        save_game()
    elif key == 'l' or key == 'L':
        load_game()