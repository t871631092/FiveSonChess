import os
import random

time=0
player=1
win=""
#method - pring chess table
def print_Table(chesstable):
#    achieve table show 1
#    for row in range(len(chesstable),0,-1):
#        print(str(chesstable[row-1])+"第"+str(row)+"行")

#    achieve table show 2
    for row in range(len(chesstable)-1,-1,-1):
        line=str(row+1).zfill(2)+" "
        for td in chesstable[row]:
            if td==0:
                line=line+"|"+"    "
            elif td==1:
                line=line+"|"+" 口 "
            elif td==2:
                line=line+"|"+" @@ " #在🐴？
        line=line+"|"
        print("   +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+")
        print(line)
    print("   +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+")
    foot="    "
    for tf in range(20):
        foot=foot+" "+str(tf+1).zfill(2)+"  "
    print(foot)


#method - add chess to table
def addchess(x,y):
    global time
    global player
    global win
    #os.system("cls")
    print("玩家"+str(player)+"在["+str(x)+","+str(y)+"]位置添加棋子")
    if player ==1:
        chess_table[y-1][x-1]=1
        if checkwin(x,y)==1:
            time=400
            win=player
        player=2
    else:
        chess_table[y-1][x-1]=2
        if checkwin(x,y)==1:
            time=400
            win=player
        player=1
    print_Table(chess_table)
    
def checkchess(x,y):
    global chess_table
    return chess_table[y-1][x-1]==0

def startPVP():
    global time
    while time<400:
        ok=1
        while ok==1:
             print("输入x")
             xx=input()
             print("输入y")
             yy=input()
             if checkchess(int(xx),int(yy))==1:
                 addchess(int(xx),int(yy))
                 ok=0
             else:
                 print("请重新输入")
        time=time+1
    if win != "":
        print(str(win)+"胜利")

def startPVE():
    global time
    while time<200:
        ok=1
        while ok==1:
             print("输入x")
             xx=input()
             print("输入y")
             yy=input()
             if checkchess(int(xx),int(yy))==1:
                 addchess(int(xx),int(yy))
                 ok=0
             else:
                 print("请重新输入")
        time=time+1
        ai()
    if win != "":
        print(str(win)+"胜利")
        
# start the game with EVE mode
def startEVE():
    global time
    while time < 400:
        ai()
    if win != "":
        print(str(win)+"胜利")

#FakeAI
def ai():
    ok=1
    while ok==1:
        x = random.randint(1,20)
        y = random.randint(1,20)
        if checkchess(int(x),int(y))==1:
            addchess(int(x),int(y))
            ok=0


#Check the is it win ?
def checkwin(x,y):
    global chess_table
    global player
#0°
    count = 0
    for xx in range(0,19):
        if chess_table[y-1][xx]==int(player): 
            count = count+1
            if count >= 5:
                return True
        else:
            count = 0
#90°
    count = 0
    for yy in range(0,19):
        if chess_table[yy][x-1]==int(player): 
            count = count+1
            if count >= 5:
                return True
        else:
            count = 0
#45°
    count = 0
    arr=[]
    ax=x
    ay=y
    bx=x
    by=y
    while ax<21 and ay<21:
        arr.append(chess_table[ay-1][ax-1])
        ax=ax+1
        ay=ay+1
    while by>0 and bx>0:
        bx=bx-1
        by=by-1
        arr.insert(0,chess_table[by-1][bx-1])
    for aaa in arr:
        if aaa==int(player): 
            count = count+1
            if count >= 5:
                return True
        else:
            count = 0
# #-45°
    count = 0
    arrr=[]
    aax=x
    aay=y
    bbx=x
    bby=y
    while aax>0 and aay<21:
        arrr.insert(0,chess_table[aay-1][aax-1])
        aax=aax-1
        aay=aay+1
        print(aax)
        print(aay)
        print(arrr)
    while bbx<20 and bby>1:
        bbx=bbx+1
        bby=bby-1
        arrr.append(chess_table[bby-1][bbx-1])
        print(bbx)
        print(bby)
        print(arrr)
    for aaaa in arrr:
        print(aaaa)
        if aaaa==int(player):
            count = count+1
            if count >= 5:
                return True
        else:
            count = 0

# #45°
#     count = 0
#     if x-y == 0:
#     elif x-y > 0:
#     elif x-y < 0:
#         for ax in range(0, 19):
#             if chess_table[ax][ax] == int(player):
#             count = count+1
#             if count >= 5:
#                 return True
#         else:
#             count = 0



# #-45°        
#     count = 0
    
#     for xx in range(0,19):
#         if chess_table[y][xx]==int(player): 
#             count = count+1
#             if count >= 5:
#                 return True
#         else:
#             count = 0


#create chess table
chess_table=[]
print("初始化棋盘")
while len(chess_table) <20:
     chess_table.append([0 for x in range(20)])

print_Table(chess_table)


#strat the game by
#startPVP()
#startEVE()

startPVE()
