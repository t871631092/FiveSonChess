import ChessApp
import random
#New a instance of ChessAPP
#创建一个ChessAPP的实例
# For example 
#chess=ChessApp.PVP(column=20,p1=" 口 ",p2=" @@ ",p1Name="p1",p2Name="p2",inp1="inputer",inp2="inputer",clean=False,autoPrint=True)
#default :
# column=20       
# p1="  A "
# p2="  B "
# p1Name="p1"
# p2Name="p2"
# inp1=inputer
# inp2=inputer
# clean=False
# autoPrint=True

def inputer(column,table,lastChess,currentPlayer,p1,p2,currentPlayerName,round,tableStr):
    print("引用外部函数")
    print("输入x")
    x=int(input())
    print("输入y")
    y=int(input())
    return [x,y]

def AiZero(column,table,lastChess,currentPlayer,p1,p2,currentPlayerName,round,tableStr):
    print(tableStr)
    x = random.randint(1,column)
    y = random.randint(1,column)
    print(str(round)+" : "+currentPlayerName+" chess on [ "+str(x)+","+str(y)+" ]")
    return [x,y]

def AiOne(column,table,lastChess,currentPlayer,p1,p2,currentPlayerName,round,tableStr):
    print("I am AiOne")
    x = random.randint(1,column)
    y = random.randint(1,column)
    return [x,y]

chess=ChessApp.start(inp1=AiZero,inp2=AiZero,p1Name="AiZero-1",p2Name="AiZero-2",autoPrint=False)
