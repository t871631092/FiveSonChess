"""
@author: liubai01
@description: this is the script for the GUI section, invoke get_inputter here to get the
input-like function.
"""

import matplotlib.pyplot as plt
import numpy as np
import time
import copy
import math


class Fiverow_GUI_v1():
    """
    The class for GUI, if you want to have a inputter-like function specified in app.py
    Please invoke get_inputter() function below.

    TBD: it does not support the PVP. if you start two GUI at the same time,
    there should be some weird bugs. It may be fixed in the future.
    """

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        plt.axis("off")

        self.has_input = False
        self.input_coord = None

        self.fig.canvas.mpl_connect("button_press_event", self.get_on_press())
        plt.ion()

    @staticmethod
    def __cvt_tableList(tableList, p1, p2):
        """

        :param tableList: a python built-in list that generated by ChessApp/table, with elements
                            0 represents the null, p1 represents the chess of player with similar to p2
        :param p1: string the denotes the first player
        :param p2: omit
        :return:
        """
        tableList = copy.deepcopy(tableList)
        col = len(tableList)

        for i in range(col):
            for j in range(col):
                if tableList[i][j] == p1:
                    tableList[i][j] = 1
                elif tableList[i][j] == p2:
                    tableList[i][j] = 2

        return np.array(tableList)

    def get_on_press(self):
        """
        generate the event callback function for the GUI, the wrapper of the GUI inst.
        :return:
        """

        def on_press(event):
            """
            grasp the coordination clicked by the player, the callback function after clicking
            :param event:
            :return:
            """
            if event.button == 1: # left click
                self.input_coord = [math.floor(event.xdata + 0.5) + 1, math.floor(event.ydata + 0.5) + 1]
                self.update()
                self.has_input = True
            # elif event.button == 3: # right click for debugging
            #     print("x, y =", event.xdata, event.ydata)

        return on_press

    def plot_table(self, tableList, p1, p2):
        # transform the table list to the numpy list
        np_tableList = self.__cvt_tableList(tableList, p1, p2)
        # plot the table
        self.ax.imshow(np_tableList, cmap="Blues", vmin=0, vmax=2)
        # set the bandwith of the grid
        plt.xticks(np.arange(0, np_tableList.shape[0], 1))
        plt.yticks(np.arange(0, np_tableList.shape[1], 1))
        self.ax.grid()

    def cla(self):
        """
        clear all the stuff of the GUI
        :return:
        """
        self.ax.cla()

    def wait_until_hasinput(self):
        """
        a busy wait function until there is some input
        :return: the coordination whose index starts with 1, follows the standard of ChessApp.py
        """
        while not self.has_input:
            plt.pause(0.1)
        self.has_input = False

        return self.input_coord

    def update(self):
        """
        all plotting will not work until you do the update
        :return:
        """
        self.fig.canvas.draw()


def get_inputter():
    """
    the function will return a input-like function(refer to app.py if you have any question)
    that provide a GUI.

    Warning: it does not support the PVP. if you start two GUI at the same time,
    there should be some weird bugs. It may be fixed in the future.

    :return:
    """
    gui_inst = Fiverow_GUI_v1()

    def gui_inputer_v1(column, table, tableList, tableStr, lastChess, currentPlayer, p1, p2, currentPlayerName, round):
        gui_inst.cla()
        gui_inst.plot_table(tableList, p1, p2)

        x, y = gui_inst.wait_until_hasinput()
        gui_inst.update()

        return [x, y]

    return gui_inputer_v1
