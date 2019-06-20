"""
@author: liubai01
@description: this is the sanity test which trigger the GUI and have a contest with a random Agent
"""

# fix the problem that cannot find moudule under root directory if you do not specify your
# exe path there.
import sys
import os

test_script_path = os.path.split(os.path.abspath(__file__))[0]
root_path = os.path.split(test_script_path)[0]
sys.path.append(root_path)

import ChessApp
import random
from GUI.v1 import get_inputter


# inputer method-random input x,y
def AiZero(column, table, tableList, tableStr, lastChess, currentPlayer, p1, p2, currentPlayerName, round):
    print(tableStr)

    x = random.randint(1, column)
    y = random.randint(1, column)

    print(str(round) + " : " + currentPlayerName + " chess on [ " + str(x) + "," + str(y) + " ]")

    return [x, y]



gui_v1_input = get_inputter()
chess = ChessApp.start(column=20, inp1=AiZero, inp2=gui_v1_input, p1Name="a1", p2Name="AiOne", autoPrint=False)
