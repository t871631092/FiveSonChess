import random
from main import chess_table

ScoreModel=[(10, (0,1,1,0,0)), #Model of chess 好像没什么卵用?
            (10, (0,0,1,1,0)),
            (20, (1,1,0,1,0)),
            (30, (0,0,1,1,1)),
            (30, (1,1,1,0,0)),
            (50, (0,1,0,1,1,0)),
            (50, (0,1,1,0,1,0)),
            (50, (1,1,1,0,1)),
            (50, (1,1,0,1,1)),
            (50, (1,0,1,1,1)),
            (50, (0,1,1,1,1)),
            (50, (1,1,1,1,0)),
            (100,(0,1,1,1,1,0)),
            (999,(1,1,1,1,1,1))]

score = 0

def scan(tablescore):
    global chess_table
    tablescore = [[[0 for count in range(5)] for x in range(19)] for y in range(19)]
    for a in range(0,19):
        for b in range(0,19):
            #if the location is empty, then begin to scan for eight direction
            if chess_table[a][b] == 0: 
                aa=a
                bb=b
                #upward
                #if upward is empty, then add 0 score
                while bb - 1>=0 and tablescore[aa][bb-1] == 0: #if upward is empty, then do not add score
                    bb -= 1
                    tablescore[a][b][0] += score
                if bb-1 >=0 and tablescore[aa][bb-1] == 2: #if upward is 2, then add 2 score
                    tablescore[a][b][0] += 1
                if bb-1 >=0 and tablescore[aa][bb-1] == 1:
                    tablescore[a][b][0] -= 2
                #dowmward
                aa=a
                bb=b
                while bb + 1<20 and tablescore[aa][bb+1] == 0: 
                    bb += 1
                    tablescore[a][b][0] += score
                if bb+1 <20 and tablescore[aa][bb-1] == 2: #if downward is 2, then add 2 score
                    tablescore[a][b][0] += 1
                if bb+1 <20 and tablescore[aa][bb-1] == 1:
                    tablescore[a][b][0] -= 2
                #liftward
                aa=a
                bb=b
                while aa - 1>=0 and tablescore[aa-1][bb] == 0: 
                    aa -= 1
                    tablescore[a][b][0] += score
                if aa-1 >=0 and tablescore[aa-1][bb] == 2: #if liftward is 2, then add 2 score
                    tablescore[a][b][0] += 1
                if aa+1 >=0 and tablescore[aa-1][bb-1] == 1:
                    tablescore[a][b][0] -= 2
                #rightward
                aa=a
                bb=b
                while aa + 1<20 and tablescore[aa+1][bb] == 0: 
                    aa += 1
                    tablescore[a][b][0] += score
                if aa+1 <20 and tablescore[aa+1][bb] == 2: #if Rightward is 2, then add 2 score
                    tablescore[a][b][0] += 1
                if aa+1 <20 and tablescore[aa+1][bb] == 1:
                    tablescore[a][b][0] -= 2
                #Left-Down

                #Right-Up

                #Left-Up

                #Right-Up

                #score += 0
    return tablescore

tablescore=[]
scan(tablescore)
print(tablescore)