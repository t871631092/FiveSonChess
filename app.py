import ChessApp
import random
#New a instance of ChessAPP
#创建一个ChessAPP的实例
#
#
# Use 
#chess=ChessApp.PVP(column=10,p1="  A ",p2="  B ",inp1=inputer,inp2=raninpter)
#default :
# column=20
# p1="  A "
# p2="  B "
# inp1=inputer
# inp2=inputer

def inputer(column,table,currentPlayer,p1,p2):
    print("引用外部函数")
    print("输入x")
    x=int(input())
    print("输入y")
    y=int(input())
    return [x,y]

def raninpter(column,table,currentPlayer,p1,p2):
    print("引用随机函数")
    x = random.randint(1,column)
    y = random.randint(1,column)
    return [x,y]


chess=ChessApp.start(inp1=raninpter,inp2=inputer)
