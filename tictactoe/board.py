import random
import time


class Board:
    global win_pos
    win_pos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    def __init__(self,board_s,auto = False):
        global board_size
        board_size = board_s
        self.state = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.auto = auto
        self.game_count =0
    def set_player(self,player1,player2):
        self.player_1 = player1
        self.player_2 = player2
        self.turn = random.choice([self.player_1,self.player_2])
    def print_board(self,stroke_weight = 3,stroke_color=color(255) ):
        fill(0)
        rect(0,0,board_size,board_size)
        strokeWeight(stroke_weight)
        stroke(stroke_color)
        line(0,board_size/3,board_size,board_size/3)
        line(0,2*board_size/3,board_size,2*board_size/3)
        line(board_size/3,0,board_size/3,board_size)
        line(2*board_size/3,0,2*board_size/3,board_size)
        for i,x in enumerate(self.state):
            for j,y in enumerate(x):
                textSize(board_size/3)
                textAlign(CENTER,TOP)
                if y==0:
                    pass
                elif y ==self.player_1:
                    fill(self.player_1.player_color)
                    text(self.player_1.sign,j*board_size/3+board_size/6,i*board_size/3)
                elif y ==self.player_2:
                    fill(self.player_2.player_color)
                    text(self.player_2.sign,j*board_size/3+board_size/6,i*board_size/3)
                    
    def update(self):
        
        if not self.is_end():
            k = self.turn.select_one()
            try:
                x = k/3
                y = k%3
                if self.state[x][y] == 0:
                    self.state[x][y] = self.turn
                    self.print_board()
                    self.turn = self.player_2 if self.turn == self.player_1 else self.player_1
            except:
                pass
        else:
            if not self.auto and self.is_end():
                print("Over")
                return True

            elif self.auto and self.is_end():
                self.auto-=1
                self.reset()
            else:
                pass
    def reset(self):
        if self.is_end() == self.player_1:
            self.player_1.giveReward(1)
            self.player_2.giveReward(-1)
        elif self.is_end() == self.player_2:
            self.player_1.giveReward(-1)
            self.player_2.giveReward(1)
        elif self.is_end() == -1:
            self.player_1.giveReward(0)
            self.player_2.giveReward(0)
        self.state = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.start()
        
    def get_blank(self):
        try:
            return [(i,j) for i,y in enumerate(self.state) for j,x in enumerate(y) if x == 0]
        except:
            return None
    def is_end(self,temp_board =None):
        global win_pos
        for pos in win_pos:
            if self.state[pos[0]/3][pos[0]%3] == self.state[pos[1]/3][pos[1]%3] == self.state[pos[2]/3][pos[2]%3] == self.player_1:
                print(self.player_1.name,pos)
                return self.player_1
            elif self.state[pos[0]/3][pos[0]%3] == self.state[pos[1]/3][pos[1]%3] == self.state[pos[2]/3][pos[2]%3] == self.player_2:
                print(self.player_2.name,pos)
                return self.player_2
        if len(self.get_blank()) == 0:
            print("blank",self.state)
            return -1
        return False   
    def start(self):
        self.game_count+=1
        self.update()
            
            
            
            
                    
                    
                    
                 
        
        
        
        
        
        
        
        
        
        
        
