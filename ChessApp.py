class StartGame:

    #The chess table array
    Table=[]
    #The number of the row and column in the chess table
    column=0
    #Current chess player id (A or B)
    player="A"


    #Construction_start the game
    #mode=0:PVP
    #mode=1:PVE
    #mode=2:EVE
    def __init__(self,column,mode):
        self.column=column
        self.__createTable()



        
    ##Private
    #Method_Return the last time player
    def __lastPlayer(self):
        if self.player=="A":
            return "B"
        elif self.player=="B":
            return "A"

    #Method_Create chess table
    def __createTable(self):
        self.Table=[[0 for cell in range(self.column) ] for row in range(self.column)]
        print("初始化棋盘")
        self.print()

    #Method_Add chess to table : input the x,y and player id(A/B)
    def __addChess(self,x,y,z):
        self.Table[y-1][x-1]=z

    #Method_Check chess info return | 0 / A / B |
    def __checkChess(self,x,y):
        return self.Table[y-1][x-1]

    #Method_
        
    #Method_Is accord with condition when it accord return |true|
    def __checkWin(self,x,y):
        #0 degree
        player=self.__lastPlayer()
        count = 0
        for xx in range(1,self.column):
            if self.__checkChess(xx,y)==player: 
                count = count+1
                if count >= 5:
                    print("0degree")#debug
                    return True
            else:
                count = 0
        #90 degree
        count = 0
        for yy in range(1,self.column):
            if self.__checkChess(x,yy)==player: 
                count = count+1
                if count >= 5:
                    print("90degree")#debug
                    return True
            else:
                count = 0
        #45 degree
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
                    print("45degree")#debug
                    return True
            else:
                count = 0
        #-45 degree
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
                    print("-45degree")#debug
                    return True
            else:
                count = 0
        return False



    #Method_chess when success return |true|
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

    #Method_chess
    def add(self,x,y):
        if self.__add(x,y)==True:
            self.print()
            print("玩家"+self.__lastPlayer()+"在["+str(x)+","+str(y)+"]下了一颗棋子")
            if self.__checkWin(x,y)==True:
                print("Winner is Player "+self.player)
    
    #Method_Print the table
    def print(self):
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
            print("   +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+")
            print(line)
        print("   +----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+")
        foot="    "
        for tf in range(20):
            foot=foot+" "+str(tf+1).zfill(2)+"  "
        print(foot)

    

