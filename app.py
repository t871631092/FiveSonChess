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

##############################################################################################################################
#                                             e   x   a   m   p   l   e                                                      #
##############################################################################################################################
# inputer method example
def Example(column, table, tableList, tableStr, lastChess, currentPlayer, p1, p2, currentPlayerName, round):
    print(tableStr)
    print("I am Example Inputer")
    ##################################################
    #### Put your code here 
    # you can use (column,table,tableList,tableStr,lastChess,currentPlayer,p1,p2,currentPlayerName,round)
    # you must Assignment to x and y  ;like x=1 y=1
    #
    ##################################################
    x = 1
    y = 1
    print(str(round) + " : " + currentPlayerName + " chess on [ " + str(x) + "," + str(y) + " ]")
    return [x, y]


import ChessApp


# inputer method-Manual input x,y
def inputer(column, table, tableList, tableStr, lastChess, currentPlayer, p1, p2, currentPlayerName, round):
    print(tableStr)
    print("Last chess on [ " + str(lastChess[0]) + "," + str(lastChess[1]) + " ]")
    print("引用外部函数 : 手动输入")
    print("输入x")
    x = int(input())
    print("输入y")
    y = int(input())
    print(str(round) + " : " + currentPlayerName + " chess on [ " + str(x) + "," + str(y) + " ]")
    return [x, y]


import random


# inputer method-random input x,y
def AiZero(column, table, tableList, tableStr, lastChess, currentPlayer, p1, p2, currentPlayerName, round):
    print(tableStr)
    print("引用外部函数 : 随机输入")
    x = random.randint(1, column)
    y = random.randint(1, column)
    print(str(round) + " : " + currentPlayerName + " chess on [ " + str(x) + "," + str(y) + " ]")
    return [x, y]


from AiOne import OnceScan


# inputer method
def AiOne(column, table, tableList, tableStr, lastChess, currentPlayer, p1, p2, currentPlayerName, round):
    Table = table
    if currentPlayer == p1:
        CurrentPlayer = p2
        AgainstPlayer = p1
    else:
        CurrentPlayer = p1
        AgainstPlayer = p2
    maxScore = 0
    print(tableStr)
    print("I am AiOne")
    score = ChessApp.table(column)
    for Xaxis in range(column):
        for Yaxis in range(column):
            if Table.checkbyzero(Xaxis, Yaxis) == 0:
                # set Ai One
                cellScore = []
                cellScore.append(OnceScan(Xaxis, Yaxis, 0, 3, 1, Table, CurrentPlayer, column))
                cellScore.append(OnceScan(Xaxis, Yaxis, 0, 3, 2, Table, AgainstPlayer, column))
                score.set(Xaxis, Yaxis, max(cellScore))
                if max(cellScore) > maxScore:
                    maxScore = max(cellScore)
                    x = Xaxis + 1
                    y = Yaxis + 1
            else:
                score.set(Xaxis, Yaxis, 0)
            pass
        pass
    score.print()  # debug print
    if round == 0:
        x = random.randint(1, column)
        y = random.randint(1, column)
        print(str(round) + " : " + currentPlayerName + " chess on [ " + str(x) + "," + str(y) + " ]")
    else:
        print(str(round) + " : " + currentPlayerName + " chess on [ " + str(x) + "," + str(y) + " ]")
    return [x, y]


# Create the game instance
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


chess = ChessApp.start(column=20, inp1=inputer, inp2=AiOne, p1Name="a1", p2Name="AiOne", autoPrint=False)
