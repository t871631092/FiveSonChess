class table:
    
    #The chess table array 
    # 棋盘列表（数组）
    __Table=[]

    #Construction_start the game 
    # 构造函数-初始化
    def __init__(self,column):
        self.column=column
        self.__createTable()

    #Method_Create chess table 
    # 方法_创建棋盘
    def __createTable(self):
        self.__Table=[[0 for cell in range(self.column) ] for row in range(self.column)]
        print("初始化棋盘")

    ##Public
    # 公共方法
    #Method_Get Table data
    # 方法 获取 棋盘列表数据
    def getTable(self):
        return self.__Table

    #Method_chess when success return |true|
    # 方法_在输入坐标位置下棋，成功返回true 失败返回false
    def add(self,x,y,z):
        if self.__Table[y-1][x-1]!=0:
            self.__Table[y-1][x-1]=z
            return True
        else:
            return False

    #Method_Check chess info return | 0 / A / B | 
    # 方法_返回输入坐标棋子信息 返回 0 A B
    def check(self,x,y):
        return self.__Table[y-1][x-1]
    
    #Method_Print the table
    # 方法_输出棋盘
    def print(self):
        linestr="   "
        for X in range(self.column):
            linestr=linestr+"+----"
        linestr=linestr+"+"
        for row in range(len(self.__Table)-1,-1,-1):
            line=str(row+1).zfill(2)+" "
            for td in self.__Table[row]:
                if td==0:
                    line=line+"|"+"    "
                else:
                    line=line+"|"+" +td+ "
            line=line+"|"
            print(linestr)
            print(line)
        print(linestr)
        foot="    "
        for tf in range(self.column):
            foot=foot+" "+str(tf+1).zfill(2)+"  "
        print(foot)

    

    
    


class PVP:

    #The chess table array 
    # 棋盘列表（数组）
    Table=[]
    #The number of the row and column in the chess table
    # 棋盘的行（列）数
    column=0
    #Current chess player id (A or B)
    # 当前玩家
    player="A"
    #round- the round of the game
    #当前回合数
    CurrentRound=0
    #Winner - winner
    # 胜利的玩家
    Winner="0"

    #Construction_start the game 
    # 构造函数-初始化
    def __init__(self,column):
        self.column=column
        self.__createTable()
        while self.CurrentRound<=self.column*self.column:
            ok=1
            while ok==1:
                print("输入x")
                x=input()
                print("输入y")
                y=input()
                if self.add(x,y)==1:
                    ok=0
                else:
                    print("请重新输入")


    #Method_Create chess table 
    # 方法_创建棋盘
    def __createTable(self):
        self.Table=[[0 for cell in range(self.column) ] for row in range(self.column)]
        print("初始化棋盘")
        self.print()

    #Method_Add chess to table : input the x,y and player id(A/B) 
    # 方法_在数组上添加棋子
    def __addChess(self,x,y,z):
        self.Table[y-1][x-1]=z

    #Method_Check chess info return | 0 / A / B | 
    # 方法_返回输入坐标棋子信息 返回 0 A B
    def __checkChess(self,x,y):
        return self.Table[y-1][x-1]

        
    ##Private私有方法（函数）
    #Method_Return the last time player 
    # 方法_返回上一次的玩家
    def __lastPlayer(self):
        if self.player=="A":
            return "B"
        elif self.player=="B":
            return "A"

    #Method_Create chess table 
    # 方法_创建棋盘
    def __createTable(self):
        self.Table=[[0 for cell in range(self.column) ] for row in range(self.column)]
        print("初始化棋盘")
        self.print()

    #Method_Add chess to table : input the x,y and player id(A/B) 
    # 方法_在数组上添加棋子
    def __addChess(self,x,y,z):
        self.Table[y-1][x-1]=z

    #Method_Check chess info return | 0 / A / B | 
    # 方法_返回输入坐标棋子信息 返回 0 A B
    def __checkChess(self,x,y):
        return self.Table[y-1][x-1]

    #Method_Is accord with condition when it accord return |true|
    # 方法_判断游戏是否胜利 返回true
    def __checkWin(self,x,y):
        #0 degree
        # 水平
        player=self.__lastPlayer()
        count = 0
        for xx in range(1,self.column+1):
            if self.__checkChess(xx,y)==player: 
                count = count+1
                if count >= 5:
                    #print("0degree")#debug
                    self.Winner=player
                    return True
            else:
                count = 0
        #90 degree
        # 垂直
        count = 0
        for yy in range(1,self.column+1):
            #print(yy)#debug
            #print(x)#debug
            #print(self.__checkChess(x,yy))#debug
            if self.__checkChess(x,yy)==player: 
                count = count+1
                #print(count)#debug
                if count >= 5:
                    #print("90degree")#debug
                    self.Winner=player
                    return True
            else:
                count = 0
        #45 degree
        # 左下到右上
        count = 0
        arr=[]
        ax=x
        ay=y
        bx=x
        by=y
        while ax<=self.column and ay<=self.column:
            arr.append(self.__checkChess(ax,ay))
            ax=ax+1
            ay=ay+1
        while by>0 and bx>0:
            bx=bx-1
            by=by-1
            arr.insert(0,self.__checkChess(bx,by))
        for aaa in arr:
            if aaa==player: 
                # print(aaa)#debug
                # print(arr)#debug
                # print(player)#debug
                count = count+1
                if count >= 5:
                    #print("45degree")#debug
                    self.Winner=player
                    return True
            else:
                count = 0
        #-45 degree
        # 左上到右下
        count = 0
        arrr=[]
        aax=x
        aay=y
        bbx=x
        bby=y
        while aax>0 and aay<=self.column:
            arrr.insert(0,self.__checkChess(aax,aay))
            aax=aax-1
            aay=aay+1
        while bbx<self.column and bby>1:
            bbx=bbx+1
            bby=bby-1
            arrr.append(self.__checkChess(bbx,bby))
        for aaaa in arrr:
            if aaaa==player:
                count = count+1
                if count >= 5:
                    #print("-45degree")#debug
                    self.Winner=player
                    return True
            else:
                count = 0
        return False



    #Method_chess when success return |true|
    # 方法_在输入坐标位置下棋，成功返回true 失败返回false
    def __add(self,x,y):
        if self.__checkChess(x,y)==0:
            if self.player=="A":
                self.__addChess(x,y,"A")
                self.player="B"
            elif self.player=="B":
                self.__addChess(x,y,"B")
                self.player="A"
            return True
        else:
            return False


    ##Public
    # 公共方法

    #Method_chess
    # 方法_下棋
    def add(self,x,y):
        if self.Winner!="0":
            print("Player "+str(self.Winner)+" have been win")
            return
        if self.CurrentRound>self.column*self.column:
            print("棋盘已满")
            return
        if self.__add(x,y)==True:
            self.print()
            print("玩家"+self.__lastPlayer()+"在["+str(x)+","+str(y)+"]下了一颗棋子")
            if self.__checkWin(x,y)==True:
                print("Winner is Player "+str(self.Winner))
    
    #Method_Print the table
    # 方法_输出棋盘
    def print(self):
        linestr="   "
        for X in range(self.column):
            linestr=linestr+"+----"
        linestr=linestr+"+"
        for row in range(len(self.Table)-1,-1,-1):
            line=str(row+1).zfill(2)+" "
            for td in self.Table[row]:
                if td==0:
                    line=line+"|"+"    "
                elif td=="A":
                    line=line+"|"+" 口 "
                elif td=="B":
                    line=line+"|"+" @@ " #在🐴？
            line=line+"|"
            print(linestr)
            print(line)
        print(linestr)
        foot="    "
        for tf in range(self.column):
            foot=foot+" "+str(tf+1).zfill(2)+"  "
        print(foot)

    

