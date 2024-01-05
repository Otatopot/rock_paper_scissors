import random

def run():
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    options = list((rock, paper, scissors))    
    x = random.randrange(0, 3) #remember range doesn't include last figure
    y = random.randrange(0, 3) 
    print(x,y)
    signx = options[x]
    signy = options[y]
    print("Player 1 chose " + signx + " and Player 2 chose " + signy)
    #while y != 2:
    if x == y+1:
        print(signx + " beats "  + signy + " Player 1 Wins!!!")
    elif y == 2 and x == 0:
        print(signx + " beats "  + signy + " Player 1 Wins!!!")
    elif y == x+1:
        print(signy + " beats "  + signx + " Player 2 Wins!!!")
    elif x == 2 and y == 0:
        print(signy + " beats "  + signx + " Player 2 Wins!!!")
    else:
        print("It's a TIE!!!!")

run()
    

        
    
    