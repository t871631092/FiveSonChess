#Instance 
# StartGame(column,mode)
# return the object of chess game

#parameter
# column (int): the column of the table row
# mode (int):the mode of the game like PVP PVE EVE
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
import ChessApp as chessapp

chess=chessapp.StartGame(5,0)
chess.add(1,1)
chess.add(2,2)
chess.add(1,2)
chess.add(3,3)
chess.add(1,3)
chess.add(4,4)
chess.add(1,4)
chess.add(5,5)
chess.add(1,5)
chess.add(4,2)
chess.add(1,5)
#print(chess.Table)