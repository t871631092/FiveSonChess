import random
from colour import colour

black6 =          [['empty', 'black', 'black', 'black', 'black','empty'],
                   ['empty', 'black', 'black', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'black', 'black','empty'],
                   ['empty', 'black', 'black', 'empty', 'black','empty'],
                   ['empty', 'black', 'empty', 'black', 'black','empty'],
                   ['empty', 'empty', 'black', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'empty', 'black','empty'],
                   ['empty', 'black', 'empty', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'empty', 'empty','empty'],
                   ['empty', 'empty', 'empty', 'black', 'empty','empty']]
black6s = [99999,10000,10000,1000,1000,100,100,100,10,10]

black5 =          [['black', 'black', 'black', 'black', 'black'],
                   ['black', 'black', 'black', 'black', 'empty'],
                   ['empty', 'black', 'black', 'black', 'black'],
                   ['black', 'black', 'empty', 'black', 'black'],
                   ['black', 'empty', 'black', 'black', 'black'],
                   ['black', 'black', 'black', 'empty', 'black']]
black5s = [999999,10000,10000,10000,10000,10000]

white6 =          [['empty', 'white', 'white', 'white', 'white','empty'],
                   ['empty', 'white', 'white', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'white', 'white','empty'],
                   ['empty', 'white', 'white', 'empty', 'white','empty'],
                   ['empty', 'white', 'empty', 'white', 'white','empty'],
                   ['empty', 'empty', 'white', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'empty', 'white','empty'],
                   ['empty', 'white', 'empty', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'empty', 'empty','empty'],
                   ['empty', 'empty', 'empty', 'white', 'empty','empty']]
white6s = [99999,10000,10000,1000,1000,100,100,100,10,10]

white5 =          [['white', 'white', 'white', 'white', 'white'],
                   ['white', 'white', 'white', 'white', 'empty'],
                   ['empty', 'white', 'white', 'white', 'white'],
                   ['white', 'white', 'empty', 'white', 'white'],
                   ['white', 'empty', 'white', 'white', 'white'],
                   ['white', 'white', 'white', 'empty', 'white']]
white5s = [999999,10000,10000,10000,10000,10000]

def enumcolour(vector): # Change colour.white to “white”
    chessmodel = []
    for chess in vector:
        if chess == colour.black:
            chessmodel.append('black')
        elif chess == colour.white:
            chessmodel.append('white')
        else:
            chessmodel.append('empty')
    
    return chessmodel

def analyze_vector(vector): # Return score for vector
    chessmodel = enumcolour(vector)
    score = {'white': 0, 'black': 0}
    length = len(chessmodel)

    if length == 5:
        for i in range(len(white5)):
            if white5[i] == chessmodel:
                score['white'] += white5s[i]
            if black5[i] == chessmodel:
                score['black'] += black5s[i]
        return score

    for i in range(length - 5):
        t = [chessmodel[i], chessmodel[i + 1], chessmodel[i + 2], chessmodel[i + 3], chessmodel[i + 4]]
        for i in range(len(white5)):
            if white5[i] == t:
                score['white'] += white5s[i]
            if black5[i] == t:
                score['black'] += black5s[i]

    for i in range(length - 6):
        t = [chessmodel[i],chessmodel[i + 1], chessmodel[i + 2], chessmodel[i + 3], chessmodel[i + 4], chessmodel[i + 5]]
        for i in range(len(white6)):
            if white6[i] == t:
                score['white'] += white5s[i]
            if black6[i] == t:
                score['black'] += black5s[i]
    return score

def firststep():
    x = 8
    y = 8
    return [x, y]

#Check if there are any chess around 检查周围是否存在棋子
#True means that there are chess around here.
def checkaround(tablelist,column,x,y):
    offset = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1), (1, -1)], [(-1, -1), (1, 1)]]
    for axis in offset:
            for (xoffset, yoffset) in axis:
                if xoffset != 0 and (x + xoffset < 0 or x + xoffset >= column):
                    break
                if yoffset != 0 and (y + yoffset < 0 or y + yoffset >= column):
                    break

                if tablelist[x + xoffset][y + yoffset] != colour.empty:
                    return True

                if xoffset != 0 and (x + xoffset * 2 < 0 or y + xoffset * 2 >= column):
                    break

                if yoffset != 0 and (x + yoffset * 2 < 0 or y + yoffset * 2 >= column):
                    break

                if tablelist[x + yoffset * 2][y + xoffset * 2] != colour.empty:
                    return True
    return False

def axiscount(x,y,xoffset,yoffset,column,count,tablelist,currentPlayer):
    count = 0
    for time in range(1,5):
        if xoffset != 0 and (x + xoffset * time < 0 or x + xoffset * time >= column):
            break
        if yoffset != 0 and (y + yoffset * time < 0 or y + yoffset * time >= column):
            break
        if tablelist[x + xoffset * time][y + yoffset * time] == currentPlayer:
            count += 1
        else:
            break
    return count

def evaluate(column,tablelist,currentPlayer):
    vector = []
    tablescore = 0
    for xx in range(column):
        vector.append(tablelist[xx])
    for yy in range(column):
        vector.append([tablelist[xx][yy] for xx in range(column)])

        vector.append([tablelist[x][x] for x in range(column)])
        for xx in range(1, column - 4):
            v = [tablelist[x][x - xx] for x in range(xx, column)]
            vector.append(v)
            v = [tablelist[y - xx][y] for y in range(xx, column)]
            vector.append(v)

        vector.append([tablelist()[x][column - x - 1] for x in range(column)])

        for xx in range(4, column - 1):
            v = [tablelist[x][xx - x] for x in range(xx, -1, -1)]
            vector.append(v)
            v = [tablelist[x][column - x + column - xx - 2]
                 for x in range(column - xx - 1, column)]
            vector.append(v)

        for v in vector:
            score = analyze_vector(v)
            if currentPlayer == colour.white:
                tablescore += score['black'] - score['white']
            else:
                tablescore += score['white'] - score['black']
        return tablescore
    
def aichess(column,tablelist,x,y):
    for a in range(column):
        for b in range(column):
            if tablelist[a][b] != colour.empty:
                continue
            
            if not checkaround(tablelist,column,x,y):
                continue
        break
    pass
            
            





print('在🐴')





# from main import chess_table


# ScoreModel=[(10, (0,1,1,0,0)), #Model of chess 好像没什么卵用?
#             (10, (0,0,1,1,0)),
#             (20, (1,1,0,1,0)),
#             (30, (0,0,1,1,1)),
#             (30, (1,1,1,0,0)),
#             (50, (0,1,0,1,1,0)),
#             (50, (0,1,1,0,1,0)),
#             (50, (1,1,1,0,1)),
#             (50, (1,1,0,1,1)),
#             (50, (1,0,1,1,1)),
#             (50, (0,1,1,1,1)),
#             (50, (1,1,1,1,0)),
#             (100,(0,1,1,1,1,0)),
#             (999,(1,1,1,1,1,1))]

# score = 0

# def scan(tablescore):
#     global chess_table
#     tablescore = [[[0 for count in range(5)] for x in range(19)] for y in range(19)]
#     for a in range(0,19):
#         for b in range(0,19):
#             #if the location is empty, then begin to scan for eight direction
#             if chess_table[a][b] == 0: 
#                 aa=a
#                 bb=b
#                 #upward
#                 #if upward is empty, then add 0 score
#                 while bb - 1>=0 and tablescore[aa][bb-1] == 0: #if upward is empty, then do not add score
#                     bb -= 1
#                     tablescore[a][b][0] += score
#                 if bb-1 >=0 and tablescore[aa][bb-1] == 2: #if upward is 2, then add 2 score
#                     tablescore[a][b][0] += 1
#                 if bb-1 >=0 and tablescore[aa][bb-1] == 1:
#                     tablescore[a][b][0] -= 2
#                 #dowmward
#                 aa=a
#                 bb=b
#                 while bb + 1<20 and tablescore[aa][bb+1] == 0: 
#                     bb += 1
#                     tablescore[a][b][0] += score
#                 if bb+1 <20 and tablescore[aa][bb-1] == 2: #if downward is 2, then add 2 score
#                     tablescore[a][b][0] += 1
#                 if bb+1 <20 and tablescore[aa][bb-1] == 1:
#                     tablescore[a][b][0] -= 2
#                 #liftward
#                 aa=a
#                 bb=b
#                 while aa - 1>=0 and tablescore[aa-1][bb] == 0: 
#                     aa -= 1
#                     tablescore[a][b][0] += score
#                 if aa-1 >=0 and tablescore[aa-1][bb] == 2: #if liftward is 2, then add 2 score
#                     tablescore[a][b][0] += 1
#                 if aa+1 >=0 and tablescore[aa-1][bb-1] == 1:
#                     tablescore[a][b][0] -= 2
#                 #rightward
#                 aa=a
#                 bb=b
#                 while aa + 1<20 and tablescore[aa+1][bb] == 0: 
#                     aa += 1
#                     tablescore[a][b][0] += score
#                 if aa+1 <20 and tablescore[aa+1][bb] == 2: #if Rightward is 2, then add 2 score
#                     tablescore[a][b][0] += 1
#                 if aa+1 <20 and tablescore[aa+1][bb] == 1:
#                     tablescore[a][b][0] -= 2
#                 #Left-Down

#                 #Right-Up

#                 #Left-Up

#                 #Right-Up

#                 #score += 0
#     return tablescore

# tablescore=[]
# scan(tablescore)
# print(tablescore)