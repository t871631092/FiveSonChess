# Class table
# use to create the table-instance for the gobang
# Argument :
# column  -----[int] (necessary) set the column of the gobang checkerboard
# Method :
#  getTable()         : | return type:list -- list of checkerboard
#  add(x,y,z)         : x = x axis, y = y axis, z = the string of the chess name | return type:bool --when chessing success return true / fail return false
#  check(x,y)         : x = x axis, y = y axis | return the string of the current x,y in checkerboard
#  printStr()         : return the string of Processing checkerboard-list
#  ptint()            : print the Processing checkerboard-list
#  checkWinByXY(x,y)  : x = x axis, y = y axis | return false/string --return string of position if the input position player is win

import os


class table:
    # The chess table array
    # 棋盘列表（数组）
    __Table = []

    # Construction_start the game
    # 构造函数-初始化
    def __init__(self, column):
        self.column = column
        self.__createTable()

    # Method_Create chess table
    # 方法_创建棋盘
    def __createTable(self):
        self.__Table = [[0 for cell in range(self.column)] for row in range(self.column)]

    ##Public
    # 公共方法
    # Method_Get Table data
    # 方法 获取 棋盘列表数据
    def getTable(self):
        return self.__Table

    # Method_chess when success return |true|
    # 方法_在输入坐标位置下棋，成功返回true 失败返回false
    def add(self, x, y, z):
        if self.__Table[y - 1][x - 1] == 0:
            self.__Table[y - 1][x - 1] = str(z)
            return True
        else:
            return False

    # Method_chess when success return |true|
    # 方法_在输入坐标位置下棋，成功返回true 失败返回false
    def set(self, x, y, z):
        self.__Table[y][x] = str(z)

    # Method_Check chess info return | 0 / A / B |
    # 方法_返回输入坐标棋子信息 返回 0 A B
    def check(self, x, y):
        return self.__Table[y - 1][x - 1]

    # Method_Check chess info return | 0 / A / B |
    # 方法_返回输入坐标棋子信息 返回 0 A B
    def checkbyzero(self, x, y):
        return self.__Table[y][x]

    # Methos_Get Print string
    # 方法_输出棋盘显示的字符串
    def printStr(self):
        tableStr = ""
        linestr = "   "
        for x in range(self.column):
            x = x
            linestr = linestr + "+----"
        linestr = linestr + "+"
        for row in range(len(self.__Table) - 1, -1, -1):
            line = str(row + 1).zfill(2) + " "
            for td in self.__Table[row]:
                if td == 0:
                    line = line + "|" + "    "
                else:
                    line = line + "|" + td
            line = line + "|"
            tableStr = tableStr + linestr + os.linesep
            tableStr = tableStr + line + os.linesep
        tableStr = tableStr + linestr + os.linesep
        foot = "    "
        for tf in range(self.column):
            foot = foot + " " + str(tf + 1).zfill(2) + "  "
        tableStr = tableStr + foot + os.linesep
        return tableStr

    # Method_Print the table
    # 方法_输出棋盘
    def print(self):
        linestr = "   "
        for x in range(self.column):
            x = x
            linestr = linestr + "+----"
        linestr = linestr + "+"
        for row in range(len(self.__Table) - 1, -1, -1):
            line = str(row + 1).zfill(2) + " "
            for td in self.__Table[row]:
                if td == 0:
                    line = line + "|" + "    "
                else:
                    line = line + "|" + td
            line = line + "|"
            print(linestr)
            print(line)
        print(linestr)
        foot = "    "
        for tf in range(self.column):
            foot = foot + " " + str(tf + 1).zfill(2) + "  "
        print(foot)

    # Method scan the xy return win or not
    # 方法 判断当前X Y 是否取得胜利
    def checkWinByXY(self, x, y):
        # 0 degree
        # 水平
        player = self.check(x, y)
        count = 0
        for xx in range(1, self.column + 1):
            if self.check(xx, y) == player:
                count = count + 1
                if count >= 5:
                    # print("0degree")#debug
                    return player
            else:
                count = 0
        # 90 degree
        # 垂直
        count = 0
        for yy in range(1, self.column + 1):
            # print(yy)#debug
            # print(x)#debug
            # print(self.__checkChess(x,yy))#debug
            if self.check(x, yy) == player:
                count = count + 1
                # print(count)#debug
                if count >= 5:
                    # print("90degree")#debug
                    return player
            else:
                count = 0
        # 45 degree
        # 左下到右上
        count = 0
        arr = []
        ax = x
        ay = y
        bx = x
        by = y
        while ax <= self.column and ay <= self.column:
            arr.append(self.check(ax, ay))
            ax = ax + 1
            ay = ay + 1
        while by > 0 and bx > 0:
            bx = bx - 1
            by = by - 1
            arr.insert(0, self.check(bx, by))
        for aaa in arr:
            if aaa == player:
                # print(aaa)#debug
                # print(arr)#debug
                # print(player)#debug
                count = count + 1
                if count >= 5:
                    # print("45degree")#debug
                    return player
            else:
                count = 0
        # -45 degree
        # 左上到右下
        count = 0
        arrr = []
        aax = x
        aay = y
        bbx = x
        bby = y
        while aax > 0 and aay <= self.column:
            arrr.insert(0, self.check(aax, aay))
            aax = aax - 1
            aay = aay + 1
        while bbx < self.column and bby > 1:
            bbx = bbx + 1
            bby = bby - 1
            arrr.append(self.check(bbx, bby))
        for aaaa in arrr:
            if aaaa == player:
                count = count + 1
                if count >= 5:
                    # print("-45degree")#debug
                    return player
            else:
                count = 0
        return False


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

##inputer()
# type : method
# Argument :
# -column             ---type:int
# -table              ---type:instance
# -tableLsit          ---type:list
# -tableStr           ---type:string
# -lastChess          ---type:list
# -currentPlayer      ---type:string
# -p1                 ---type:string
# -p2                 ---type:string
# -currentPlayerName  ---type:string
# -round              ---type:int
# Return [x,y]        ---x axis , y axis

# for example
# #input method
# def AiOne(column,table,lastChess,currentPlayer,p1,p2,currentPlayerName,round,tableStr):
#     print("I am AiOne")
#     x = random.randint(1,column)
#     y = random.randint(1,column)
#     return [x,y]

class start:

    def inputer(self):
        print("输入x")
        x = int(input())
        print("输入y")
        y = int(input())
        return [x, y]

    def __init__(self, column=20, p1=" 口 ", p2=" @@ ", p1Name="p1", p2Name="p2", inp1="inputer", inp2="inputer",
                 clean=False, autoPrint=True):
        self.lastChess = [0, 0]
        self.p1 = p1
        self.p2 = p2
        self.column = column
        self.Table = table(column)
        self.maxRounds = column * column
        self.round = 0
        self.winner = 0
        self.currentPlayer = p1
        self.inp1 = self.inputer
        self.inp2 = self.inputer
        self.currentPlayerName = ""
        if inp1 != "inputer":
            self.inp1 = inp1
        if inp2 != "inputer":
            self.inp2 = inp2
        while self.winner == 0 and self.round != self.maxRounds:
            if self.currentPlayer == p1:
                self.currentPlayerName = p1Name
                self.inp = self.inp1
            elif self.currentPlayer == p2:
                self.currentPlayerName = p2Name
                self.inp = self.inp2
            if clean == True:
                os.system("cls")
            if autoPrint == True:
                self.Table.print()
                print(str(self.round) + ": Player ", self.currentPlayerName + " round")
            while self.ADD(self.currentPlayer, self.inp, autoPrint) == False:
                pass
            if self.currentPlayer == p1:
                self.currentPlayer = p2
                pass
            else:
                self.currentPlayer = p1
                pass
            self.round += 1
        if clean == True:
            os.system("cls")
        self.Table.print()
        print("Game Over")
        if self.winner != 0:
            print("The winner is %s" % (self.winner))

    def ADD(self, player, inp, autoPrint):
        isOK = False
        while isOK == False:
            arr = inp(self.column, self.Table, self.Table.getTable(), self.Table.printStr(), self.lastChess,
                      self.currentPlayer, self.p1, self.p2, self.currentPlayerName, self.round)
            x = arr[0]
            y = arr[1]
            isOK = self.Table.add(x, y, player)
            if isOK == False:
                print("重新输入:")
                pass
            pass
        self.lastChess = [x, y]
        if autoPrint == True:
            print("player %s chess on %s , %s" % (player, x, y))
        self.winner = self.Table.checkWinByXY(x, y)

    def getTable(self):
        return self.Table.getTable()
