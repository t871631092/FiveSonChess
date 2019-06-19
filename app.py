import ChessApp
import random


##inputer()
# type : method
# Argument :
# -column             ---type:int
# -table              ---type:list
# -lastChess          ---type:list
# -currentPlayer      ---type:string
# -p1                 ---type:string
# -p2                 ---type:string
# -currentPlayerName  ---type:string
# -round              ---type:int
# -tableStr           ---type:string
# Return [x,y]        ---x axis , y axi

#inputer method
def inputer(column,table,lastChess,currentPlayer,p1,p2,currentPlayerName,round,tableStr):
    print("引用外部函数")
    print("输入x")
    x=int(input())
    print("输入y")
    y=int(input())
    return [x,y]

#inputer method
def AiZero(column,table,lastChess,currentPlayer,p1,p2,currentPlayerName,round,tableStr):
    print(tableStr)
    x = random.randint(1,column)
    y = random.randint(1,column)
    print(str(round)+" : "+currentPlayerName+" chess on [ "+str(x)+","+str(y)+" ]")
    return [x,y]

#inputer method
def AiOne(column,table,lastChess,currentPlayer,p1,p2,currentPlayerName,round,tableStr):
    print("I am AiOne")
    x = random.randint(1,column)
    y = random.randint(1,column)
    return [x,y]


#Create the game instance
# Argument :
# column      default:20          type:int     ----- [int] (necessary) set the column of the gobang checkerboard
# p1          default:" 口 "      type:string  ----- set the chess name of player 1 in the checkerboard
# p2          default:" @@ "      type:string  ----- set the chess name of player 2 in the checkerboard
# p1Name      default:"p1"        type:string  ----- set the player 1 name
# p2Name      default:"p2"        type:string  ----- set the player 2 name
# inp1        default:"inputer"   type:Method  ----- set the player 1 input method see ##inputer
# inp2        default:"inputer"   type:Method  ----- set the player 1 input method see ##inputer
# clean       default:False       type:bool    ----- set whether to clear the last print in console/terminal 
# autoPrint   default:True        type:bool    ----- set whether to print in the function 
# Method :

chess=ChessApp.start(inp1=AiZero,inp2=AiZero,p1Name="AiZero-1",p2Name="AiZero-2",autoPrint=False)
