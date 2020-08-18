import random
import json

#A Base Class for all types of player
class Player:
    def __init__(self,name,sign,board,player_color= color(255)):
        self.name = name
        self.sign = sign
        self.player_color = player_color
        self.board = board
        self.score = 0
    def select_one(self):
        pass
    def giveReward(self,reward):
        print("score update")
        if reward == 1:
            self.score+=1
    def setOpponent(self,opponent):
        self.opponent = opponent
    def savePolicy(self):
        pass
#humans are most intelligent known species on universe 
class Human(Player):
    def __init__(self,name,sign,board,player_color= color(255),board_size =300):
        Player.__init__(self,name,sign,board,player_color= player_color)
        self.board_size = board_size
    
    def select_one(self):
            if mousePressed:
                x,y = mouseX ,mouseY
                if x < self.board_size/3 and y<self.board_size/3:
                    return 0
                elif x < 2*self.board_size/3 and y<self.board_size/3:
                    return 1
                elif x < self.board_size and y<self.board_size/3:
                    return 2
                elif x < self.board_size/3 and y<2*self.board_size/3:
                    return 3
                elif x < 2*self.board_size/3 and y<2*self.board_size/3:
                    return 4
                elif x < self.board_size and y<2*self.board_size/3:
                    return 5
                elif x < self.board_size/3 and y<self.board_size:
                    return 6
                elif x < 2*self.board_size/3 and y<self.board_size:
                    return 7
                elif x < self.board_size and y<self.board_size:
                    return 8
            return None
                
        
#only random guesses A fool Computer    
class FoolComputer(Player):
    def __init__(self,name,sign,board,player_color= color(255)):
        Player.__init__(self,name,sign,board,player_color= player_color)
    
    
    def select_one(self):
        try:
            _ = random.choice(self.board.get_blank())
        except:
            _ = (0,0)
        return 3*_[0] +_[1]

    
        
#greedy computer always want to win for winning check each and every possible option ,this make it slow       
class GreedyComputer(Player):
    def __init__(self,name,sign,board,player_color= color(255)):
        Player.__init__(self,name,sign,board,player_color= player_color)
    
    def select_one(self):
        _ = self.board.get_blank()
        if len(_) == 9:
            print(len(_))
            _ = random.choice(self.board.get_blank())
            return 3*_[0]+_[1]
        return self.find_best_move(self.board)
    
    
    def find_best_move(self,board):
        moves = board.get_blank()    
        _ = random.choice(moves) 
        best_move = 3*_[0]+_[1]
        
        i = 0
        best_score = -1000
        for x in moves:
            i+=1
            board.state[x[0]][x[1]] = self
            score = self.minimax(board,0,False)
            board.state[x[0]][x[1]] = 0
            if score > best_score: 
                # print(3*x[0] +x[1], score)
                best_move = (3*x[0] +x[1])
                best_score = score
        return best_move
    def minimax(self,board,depth,isMax):
        board.print_board()
        if board.is_end():
            if board.is_end() == -1:
                return 0
            elif board.is_end() ==self:
                return 10 
            elif board.is_end() ==self.opponent:
                return -10
                
        else:
            if isMax == True:
                best = -1000
                moves = board.get_blank()
                for x in moves:
                    board.state[x[0]][x[1]] = self
                    isMax = False
                    best = max(best,self.minimax(board,depth+1,isMax))
                    board.state[x[0]][x[1]] = 0
                return best
            else:
                best = 1000
                moves = board.get_blank()
                for x in moves:
                    board.state[x[0]][x[1]] = self.opponent
                    isMax = True
                    best = min(best,self.minimax(board,depth+1,isMax))
                    board.state[x[0]][x[1]] = 0
                return best
            
            
        

        
                
                        
                                
                                        
                                                
#like human this computer can learn from experiences, will save each experience in memory                                                        
class LearnerComputer(Player):
    def __init__(self,name,sign,board,exp_rate=0.3,player_color= color(255)):
        Player.__init__(self,name,sign,board,player_color= player_color)
        self.states = []  # record all positions taken
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.9
        a = open("policy.json","r")
        self.states_value = json.load(a)
        a.close()
        print(self.states_value)
    def select_one(self):
        if random.random()<=self.exp_rate:
            try:
                _ = random.choice(self.board.get_blank())
            except:
                _ = (0,0)
            action =  _
        else:
            blank_position = self.board.get_blank()
            value_max = -1000
            for p in blank_position:
                self.board.state[p[0]][p[1]] = self
                board_hash = self.getHash()
                self.board.state[p[0]][p[1]] = 0
                value = 0 if self.states_value.get(board_hash) is None else self.states_value.get(board_hash)
                # print(board_hash,value)
                if value >= value_max:
                    value_max = value
                    action = p
        self.board.state[action[0]][action[1]] = self
        self.states.append(self.getHash())
        self.board.state[action[0]][action[1]] = 0
        return 3*action[0]+action[1]   
    def getHash(self):
        hash = ""
        for row in self.board.state:
            for y in row:
                if y ==self:
                    hash+="+"
                elif y == self.opponent:
                    hash+="-"
                elif y ==0:
                    hash+="."
        return hash
    def giveReward(self,r):
        if r==1:
            reward = 1
            self.score+=1 
        elif r==-1:
            reward = -1
        elif r==0:
            reward =0.5
        for st in reversed(self.states):
            if self.states_value.get(st) is None:
                self.states_value[st] = 0
            self.states_value[st]+=self.lr*(reward - self.states_value[st])
            reward = self.decay_gamma * reward
            reward = self.states_value[st]
        self.states = [] 
        
    def savePolicy(self):
        a = open("policy.json","w")
        json.dump(self.states_value,a)
        a.close()
        print("policy saved")
