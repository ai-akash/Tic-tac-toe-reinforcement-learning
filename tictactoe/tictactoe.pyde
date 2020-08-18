
from board import Board
from players import Human, FoolComputer,GreedyComputer,LearnerComputer
state = 0
SIZE = 300
AUTO = 1000#0 for human Mode and any number for the number of training
board = Board(SIZE,AUTO)

def setup():
    global board,player1,player2
    player1 = FoolComputer("Fool Computer","O",board,player_color=color(150,20,10))
    # player1 = Human("Akash","X",board,player_color=color(55,0,100))
    # player1 = Human("Akash","O",board,player_color=color(150,30,45))
    # player1 = GreedyComputer("Greedy Computer","X",board,player_color=color(55,0,100))
    player2 = LearnerComputer("Learner Computer","X",board,player_color=color(55,0,100),exp_rate=0)
    # player2 = FoolComputer("Learner Computer","O",board,player_color=color(5,255,55))
    player1.setOpponent(player2)
    player2.setOpponent(player1)
    size(SIZE+300,SIZE)
    background(255)
    board.set_player(player1,player2)
    board.print_board()
    board.start()
    frameRate(300)
    
    
def draw():
    background(255)
    board.print_board()
    draw_()
    if board.is_end() == -1:
        pass
        # print("Draw")
    elif board.is_end() :
        pass
        # print("{} is winner".format(board.is_end().name))
        # print("{}:{}".format(player1.name,player1.score))
        # print("{}:{}".format(player2.name,player2.score))
    if board.update():
        player2.savePolicy()
        noLoop()
    
    
def draw_():
    
    fill(player1.player_color)
    textSize(30)
    textAlign(CENTER)
    text(player1.name,3*SIZE/2,30)
    fill(200,15,60)
    text("V/S",3*SIZE/2,60)
    fill(player2.player_color)
    text(player2.name,3*SIZE/2,90)
    textAlign(LEFT)
    textSize(20)
    text("{} : {} ".format(player2.name,player2.score),SIZE+20,height-10)
    fill(player1.player_color)
    text("{} : {} ".format(player1.name,player1.score),SIZE+20,height-30)
    fill(0)
    text("Round : {} ".format(board.game_count),SIZE+20,height-50)

    
        
    
def keyReleased():
        
    if not AUTO and board.is_end():
        board.reset()
        loop()
        
    
    
    
