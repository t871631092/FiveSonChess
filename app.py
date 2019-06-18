import ChessApp
import random
#New a instance of ChessAPP
#创建一个ChessAPP的实例

#column can be set
# Use 
#chess=ChessApp.PVP(column=10,p1="  A ",p2="  B ",inp1=inputer,inp2=raninpter)
#default :
# column=20
# p1="  A "
# p2="  B "
# inp1=inputer
# inp2=inputer

def inputer(a):
    print("引用外部函数")
    print("输入x")
    x=int(input())
    print("输入y")
    y=int(input())
    return [x,y]

def raninpter(a):
    print("引用随机函数")
    x = random.randint(1,a)
    y = random.randint(1,a)
    return [x,y]


chess=ChessApp.PVP(inp1=raninpter,inp2=inputer)
