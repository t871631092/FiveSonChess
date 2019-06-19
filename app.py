##inputer()
# type : method
# Argument :
# -column             ---type:int
# -table              ---type:instance    see  ##table
# -tableList          ---type:list
# -lastChess          ---type:list     x=lastChess[0] y=lastChess[1]
# -currentPlayer      ---type:string
# -p1                 ---type:string
# -p2                 ---type:string
# -currentPlayerName  ---type:string
# -round              ---type:int
# -tableStr           ---type:string
# Return [x,y]        ---x axis , y axi

##table
# Method :
#  getTable()         : | return type:list -- list of checkerboard
#  add(x,y,z)         : x = x axis, y = y axis, z = the string of the chess name | return type:bool --when chessing success return true / fail return false 
#  check(x,y)         : x = x axis, y = y axis | return the string of the current x,y in checkerboard
#  printStr()         : return the string of Processing checkerboard-list
#  ptint()            : print the Processing checkerboard-list
#  checkWinByXY(x,y)  : x = x axis, y = y axis | return false/string --return string of position if the input position player is win

import ChessApp
import random

#inputer method-Manual input x,y
def inputer(column,table,tableList,tableStr,lastChess,currentPlayer,p1,p2,currentPlayerName,round):
    print(tableStr)
    print("Last chess on [ "+str(lastChess[0])+","+str(lastChess[1])+" ]")
    print("引用外部函数 : 手动输入")
    print("输入x")
    x=int(input())
    print("输入y")
    y=int(input())
    print(str(round)+" : "+currentPlayerName+" chess on [ "+str(x)+","+str(y)+" ]")
    return [x,y]

#inputer method-random input x,y
def AiZero(column,table,tableList,tableStr,lastChess,currentPlayer,p1,p2,currentPlayerName,round):
    print(tableStr)    
    print("引用外部函数 : 随机输入")
    x = random.randint(1,column)
    y = random.randint(1,column)
    print(str(round)+" : "+currentPlayerName+" chess on [ "+str(x)+","+str(y)+" ]")
    return [x,y]


def scanHplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanHplus(sX+1,sY,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanHplus(sX+1,sY,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS
def scanHminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanHminus(sX-1,sY,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanHminus(sX-1,sY,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS
def scanVplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanVplus(sX,sY+1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanVplus(sX,sY+1,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS
def scanVminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanVminus(sX,sY-1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanVminus(sX,sY-1,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS
def scanLDplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLDplus(sX+1,sY+1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLDplus(sX+1,sY+1,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS
def scanLDminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLDminus(sX-1,sY-1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLDminus(sX-1,sY-1,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS
def scanLTplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLTplus(sX+1,sY-1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLTplus(sX+1,sY-1,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS
def scanLTminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLTminus(sX-1,sY+1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLTminus(sX-1,sY+1,sZ+1,t,sS,sTable,sPlayer,column)
    else:
        return sS


#inputer method
def AiOne(column,table,tableList,tableStr,lastChess,currentPlayer,p1,p2,currentPlayerName,round):
    Table=table
    CurrentPlayer=currentPlayer


    print(tableStr)    
    print("I am AiOne")
    score=ChessApp.table(column)
    for Xaxis in range(column):
        for Yaxis in range(column):
            if Table.checkbyzero(Xaxis,Yaxis)==0:
                cellScore=scanHplus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)+scanHminus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)+scanVplus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)+scanVminus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)+scanLDplus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)+scanLDminus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)+scanLTplus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)+scanLTminus(Xaxis,Yaxis,0,4,0,Table,CurrentPlayer,column)
                score.set(Xaxis,Yaxis,cellScore)
            else:
                score.set(Xaxis,Yaxis,0)
            pass
        pass
    score.print()
    x = random.randint(1,column)
    y = random.randint(1,column)
    print(str(round)+" : "+currentPlayerName+" chess on [ "+str(x)+","+str(y)+" ]")
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

chess=ChessApp.start(column=10,inp1=AiOne,inp2=AiOne,p1Name="AiZero-1",p2Name="AiOne",autoPrint=False)
