#Instance 
# StartGame(column,mode)
# return the object of chess game

#parameter
# column (int): the column of the table row
#For example 
# chess=chess.StartGame(20,0)

#public method of ChessApp
# add(x,y) to chess a son on [x,y] start by 1 if chess return true else return false
# print()  to print the table with human style

#public proeretdrgfd of ChessApp
# .Table   get the array of the game 
# .Player  get the current player of chessing    
#For example 
# print(chess.Table) 
# print(chess.player)
import ChessApp as app

chess=app.table(20)
chess.add(1,1,"A")
chess.add(2,2,"A")
chess.add(1,2,"B")
chess.add(3,3,"B")
chess.add(1,3,"B")
chess.add(4,4,"B")
chess.add(1,4,"B")
chess.add(5,5,"B")
chess.add(1,5,"B")
chess.add(4,2,"B")
chess.add(1,5,"B")
chess.print()
#print(chess.Table)


# mode (int):the mode of the game like PVP PVE EVE

    #mode=0:PVP
    # 模式0
    #mode=1:PVE
    # 模式1
    #mode=2:EVE
    # 模式2w


