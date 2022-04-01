from math import sqrt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from csv import reader
from math import sqrt
import random
import pygame
import random
import sys
import math
# region SearchAlgorithms
class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    def __init__(self, value):
        self.value = value
        self.id=value
class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    Matrix_board = []
    visited=[]
    not_visited = []
    starting_id = 0
    ending_id = 0
    def __init__(self, mazeStr):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        id = 0
        Matrix_board_1 =[]
        for item in mazeStr:
            if(item==','):
                continue
            if(item==' '):
                self.Matrix_board.append(Matrix_board_1)
                Matrix_board_1=[]
                continue
            else:
                if(item=='S'):
                    n = Node(id)
                    Matrix_board_1.append(n)
                    self.starting_id=id
                    id+=1
                elif (item == 'E'):
                    n = Node(id)
                    Matrix_board_1.append(n)
                    self.ending_id=id
                    id+=1
                elif(item=='.'):
                    n = Node(id)
                    Matrix_board_1.append(n)
                    id+=1
                else:
                    n = Node(-1)
                    Matrix_board_1.append(n)
        self.Matrix_board.append(Matrix_board_1)
        pass
    def getdirect (self,node_id):
        direci=0
        direcj=0
        for i in range(len(self.Matrix_board)):
            for j in range(len(self.Matrix_board[i])):
                if(self.Matrix_board[i][j].id==node_id):
                    direci=i
                    direcj=j
        return direci,direcj
    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        # self.path should contain the direct path from start node to goal node
        starti=1
        startj=1
        for i in range(len(self.Matrix_board)):
            for j in range(len(self.Matrix_board[i])):
                if(self.Matrix_board[i][j].id==self.starting_id):
                    starti=i
                    startj=j
        self.Matrix_board[starti][startj].previousNode =0
        for i in range(len(self.Matrix_board)):
            for j in range(len(self.Matrix_board[i])):
                if self.Matrix_board[i][j].id != -1:
                    if (i == 0 or i != 0):
                        if (i == 0):
                            self.Matrix_board[i][j].up = 0
                        else:
                            if (self.Matrix_board[i - 1][j].id != -1):
                                self.Matrix_board[i][j].up = 1


                            else:
                                self.Matrix_board[i][j].up = 0

                    if (i == len(self.Matrix_board) - 1 or i != len(self.Matrix_board) - 1):
                        if (i == len(self.Matrix_board) - 1):
                            self.Matrix_board[i][j].down = 0
                        else:
                            if (self.Matrix_board[i + 1][j].id != -1):
                                self.Matrix_board[i][j].down = 1
                            else:
                                self.Matrix_board[i][j].down = 0

                    if (j == 0 or j != 0):
                        if (j == 0):
                            self.Matrix_board[i][j].left = 0
                        else:
                            if (self.Matrix_board[i][j - 1].id != -1):
                                self.Matrix_board[i][j].left = 1
                            else:
                                self.Matrix_board[i][j].left = 0

                    if (j == len(self.Matrix_board[i]) - 1 or j != len(self.Matrix_board[i]) - 1):
                        if (j == len(self.Matrix_board[i]) - 1):
                            self.Matrix_board[i][j].right = 0
                        else:
                            if (self.Matrix_board[i][j + 1].id != -1):
                                self.Matrix_board[i][j].right = 1
                            else:
                                self.Matrix_board[i][j].right = 0


        '''for i in range(len(self.Matrix_board)):
            for j in range(len(self.Matrix_board[i])):
                if(i == 0 and j==0):
                    self.Matrix_board[i][j].up=0
                    if (self.Matrix_board[i + 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].down = 1
                        if(self.Matrix_board[i + 1][j].previousNode == None):
                            self.Matrix_board[i + 1][j].previousNode=self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].left = 0
                    if (self.Matrix_board[i][j + 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].right = 1
                        if (self.Matrix_board[i ][j+1].previousNode == None):
                            self.Matrix_board[i ][j+1].previousNode = self.Matrix_board[i][j].id
                elif (i == len(self.Matrix_board)-1 and j == len(self.Matrix_board[i])-1):
                    if (self.Matrix_board[i - 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].up = 1
                        if (self.Matrix_board[i - 1][j].previousNode == None):
                            self.Matrix_board[i - 1][j].previousNode = self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].down = 0
                    if (self.Matrix_board[i][j - 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].left = 1
                        if (self.Matrix_board[i ][j-1].previousNode == None):
                            self.Matrix_board[i ][j-1].previousNode = self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].right = 0
                elif (i == 0 and j == len(self.Matrix_board[i])-1):
                    self.Matrix_board[i][j].up = 0
                    if (self.Matrix_board[i + 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].down = 1
                        if (self.Matrix_board[i + 1][j].previousNode == None):
                            self.Matrix_board[i + 1][j].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i][j - 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].left = 1
                        if (self.Matrix_board[i ][j-1].previousNode == None):
                            self.Matrix_board[i ][j-1].previousNode = self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].right = 0
                elif (i == len(self.Matrix_board)-1 and j == 0):
                    if (self.Matrix_board[i - 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].up = 1
                        if (self.Matrix_board[i-1 ][j].previousNode == None):
                            self.Matrix_board[i-1 ][j].previousNode = self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].down = 0
                    self.Matrix_board[i][j].left = 0
                    if (self.Matrix_board[i][j + 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].right = 1
                        if (self.Matrix_board[i ][j+1].previousNode == None):
                            self.Matrix_board[i ][j+1].previousNode = self.Matrix_board[i][j].id
                elif(i==0):
                    self.Matrix_board[i][j].up = 0
                    if (self.Matrix_board[i + 1][j].id != 0 and self.Matrix_board[i][j].id !=0):
                        self.Matrix_board[i][j].down = 1
                        if (self.Matrix_board[i+1 ][j].previousNode == None):
                            self.Matrix_board[i+1 ][j].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i ][j-1].id != 0 and self.Matrix_board[i][j].id !=0):
                        self.Matrix_board[i][j].left = 1
                        if (self.Matrix_board[i ][j-1].previousNode == None):
                            self.Matrix_board[i ][j-1].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i ][j+1].id != 0 and self.Matrix_board[i][j].id !=0):
                        self.Matrix_board[i][j].right = 1
                        if (self.Matrix_board[i ][j+1].previousNode == None):
                            self.Matrix_board[i ][j+1].previousNode = self.Matrix_board[i][j].id
                elif ( j == 0):
                    if (self.Matrix_board[i - 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].up = 1
                        if (self.Matrix_board[i-1 ][j].previousNode == None):
                            self.Matrix_board[i-1 ][j].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i + 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].down = 1
                        if (self.Matrix_board[i+1 ][j].previousNode == None):
                            self.Matrix_board[i+1 ][j].previousNode = self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].left = 0
                    if (self.Matrix_board[i][j + 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].right = 1
                        if (self.Matrix_board[i ][j+1].previousNode == None):
                            self.Matrix_board[i ][j+1].previousNode = self.Matrix_board[i][j].id
                elif ( i == len(self.Matrix_board) - 1):
                    if (self.Matrix_board[i - 1][j].id != 0 or self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].up = 1
                        if (self.Matrix_board[i-1 ][j].previousNode == None):
                            self.Matrix_board[i-1][j].previousNode = self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].down = 0
                    if (self.Matrix_board[i][j - 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].left = 1
                        if (self.Matrix_board[i ][j-1].previousNode == None):
                            self.Matrix_board[i ][j-1].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i][j + 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].right = 1
                        if (self.Matrix_board[i ][j+1].previousNode == None):
                            self.Matrix_board[i ][j+1].previousNode = self.Matrix_board[i][j].id
                elif ( j == len(self.Matrix_board[i]) - 1):
                    if (self.Matrix_board[i - 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].up = 1
                        if (self.Matrix_board[i-1 ][j].previousNode == None):
                            self.Matrix_board[i-1 ][j].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i + 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].down = 1
                        if (self.Matrix_board[i+1 ][j].previousNode == None):
                            self.Matrix_board[i+1 ][j].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i][j - 1].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].left = 1
                        if (self.Matrix_board[i ][j-1].previousNode == None):
                            self.Matrix_board[i ][j-1].previousNode = self.Matrix_board[i][j].id
                    self.Matrix_board[i][j].right = 0
                else:
                    if (self.Matrix_board[i + 1][j].id != 0 and self.Matrix_board[i][j].id !=0):
                        self.Matrix_board[i][j].down = 1
                        if (self.Matrix_board[i+1 ][j].previousNode == None):
                            self.Matrix_board[i+1 ][j].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i ][j+1].id != 0 and self.Matrix_board[i][j].id !=0):
                        self.Matrix_board[i][j].right = 1
                        if (self.Matrix_board[i ][j+1].previousNode == None):
                            self.Matrix_board[i ][j+1].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i ][j-1].id != 0 and self.Matrix_board[i][j].id !=0):
                        self.Matrix_board[i][j].left = 1
                        if (self.Matrix_board[i ][j-1].previousNode == None):
                            self.Matrix_board[i ][j-1].previousNode = self.Matrix_board[i][j].id
                    if (self.Matrix_board[i - 1][j].id != 0 and self.Matrix_board[i][j].id != 0):
                        self.Matrix_board[i][j].up = 1
                        if (self.Matrix_board[i - 1][j].previousNode == None):
                            self.Matrix_board[i - 1][j].previousNode = self.Matrix_board[i][j].id'''
        '''for i in range(len(self.Matrix_board)):
            for j in range(len(self.Matrix_board[i])):
                print(self.Matrix_board[i][j].id,' ',self.Matrix_board[i][j].up,' ',self.Matrix_board[i][j].down,'  ',self.Matrix_board[i][j].left,'  ',self.Matrix_board[i][j].right ,' ',self.Matrix_board[i][j].previousNode)
        self.visited.append(self.Matrix_board[starti][startj].id)'''
        '''arr=[1,2,3]
        print(len(arr))
        print(self.Matrix_board[starti][startj].up)
        print(starti,startj)'''
        '''id = self.Matrix_board[starti][startj].id
                            starti -= 1
                            self.visited.append(self.Matrix_board[starti][startj].id)
                            if (self.Matrix_board[starti][startj].previousNode == None):
                                self.Matrix_board[starti][startj].previousNode = id'''
        '''id = self.Matrix_board[starti][startj].id
                            starti += 1
                            self.visited.append(self.Matrix_board[starti][startj].id)
                            if (self.Matrix_board[starti][startj].previousNode == None):
                                self.Matrix_board[starti][startj].previousNode = id'''
        '''id = self.Matrix_board[starti][startj].id
                            startj -= 1
                            self.visited.append(self.Matrix_board[starti][startj].id)
                            if (self.Matrix_board[starti][startj].previousNode == None):
                                self.Matrix_board[starti][startj].previousNode = id'''
        '''id = self.Matrix_board[starti][startj].id
                            startj += 1
                            self.visited.append(self.Matrix_board[starti][startj].id)
                            if (self.Matrix_board[starti][startj].previousNode == None):
                                self.Matrix_board[starti][startj].previousNode = id'''
        #id=0
        #self.not_visited.append(self.Matrix_board[starti][startj].id)
        # self.visited.pop()


        while 1:
            if(True):
                if (self.Matrix_board[starti][startj].id == self.ending_id):
                    break
                if (self.Matrix_board[starti][startj].up == 1 and self.Matrix_board[starti-1][
                    startj].id not in self.visited and self.Matrix_board[starti-1][
                    startj].id not in self.not_visited):
                    self.not_visited.append(self.Matrix_board[starti - 1][startj].id)
                    if (self.Matrix_board[starti-1][startj].previousNode == None):
                        self.Matrix_board[starti-1][startj].previousNode = self.Matrix_board[starti][startj].id
                if (self.Matrix_board[starti][startj].down == 1 and self.Matrix_board[starti+1][
                    startj].id not in self.visited and self.Matrix_board[starti+1][
                    startj].id not in self.not_visited):
                    self.not_visited.append(self.Matrix_board[starti + 1][startj].id)
                    if (self.Matrix_board[starti+1][startj].previousNode == None):
                        self.Matrix_board[starti+1][startj].previousNode = self.Matrix_board[starti][startj].id
                if (self.Matrix_board[starti][startj].left == 1 and self.Matrix_board[starti][
                    startj-1].id not in self.visited and self.Matrix_board[starti][
                    startj-1].id not in self.not_visited):
                    self.not_visited.append(self.Matrix_board[starti][startj - 1].id)
                    if (self.Matrix_board[starti][startj-1].previousNode == None):
                        self.Matrix_board[starti][startj-1].previousNode = self.Matrix_board[starti][startj].id
                if (self.Matrix_board[starti][startj].right == 1 and self.Matrix_board[starti][
                    startj+1].id not in self.visited and self.Matrix_board[starti][
                    startj+1].id not in self.not_visited):
                    self.not_visited.append(self.Matrix_board[starti][startj + 1].id)
                    if (self.Matrix_board[starti][startj+1].previousNode == None):
                        self.Matrix_board[starti][startj+1].previousNode = self.Matrix_board[starti][startj].id
                not_var = self.not_visited.pop()
                self.visited.append(not_var)
                ijdirec = self.getdirect(not_var)
                starti=ijdirec[0]
                startj=ijdirec[1]
            if(True):
                if (self.Matrix_board[starti][startj].id == self.ending_id):
                    break
                if(self.Matrix_board[starti][startj].up == 1 and self.Matrix_board[starti - 1][
                    startj].id not in self.visited and self.Matrix_board[starti - 1][startj].id != -1):
                    continue
                elif (self.Matrix_board[starti][startj].down == 1 and self.Matrix_board[starti + 1][
                    startj].id not in self.visited and self.Matrix_board[starti + 1][startj].id != -1):
                    continue
                elif (self.Matrix_board[starti][startj].left == 1 and self.Matrix_board[starti][
                    startj - 1].id not in self.visited and self.Matrix_board[starti][startj - 1].id != -1):
                    continue
                elif (self.Matrix_board[starti][startj].right == 1 and self.Matrix_board[starti][
                    startj + 1].id not in self.visited and self.Matrix_board[starti][startj + 1].id != -1):
                    continue
                else:
                    self.Matrix_board[starti][startj].id = -1
                    if (self.Matrix_board[starti][startj].up == 1 and self.Matrix_board[starti - 1][startj].id != -1):
                        starti -= 1
                        self.Matrix_board[starti][startj].down = 0
                    elif (self.Matrix_board[starti][startj].down == 1 and self.Matrix_board[starti + 1][startj].id != -1):
                        starti += 1
                        self.Matrix_board[starti][startj].up = 0
                    elif (self.Matrix_board[starti][startj].left == 1 and self.Matrix_board[starti][startj - 1].id != -1):
                        startj -= 1
                        self.Matrix_board[starti][startj].right = 0
                    elif (self.Matrix_board[starti][startj].right == 1 and self.Matrix_board[starti][startj + 1].id != -1):
                        startj += 1
                        self.Matrix_board[starti][startj].left = 0



        ijdirec =[]
        id=self.ending_id
        l=[]
        while id!=self.starting_id:
            l.append(id)
            ijdirec = self.getdirect(id)
            id = self.Matrix_board[ijdirec[0]][ijdirec[1]].previousNode
        l.append(id)
        l.reverse()

        self.path=l
        self.fullPath = self.visited
        return self.fullPath, self.path
# endregion
#region Gaming
class Gaming:
    def __init__(self):
        self.COLOR_BLUE = (0, 0, 240)
        self.COLOR_BLACK = (0, 0, 0)
        self.COLOR_RED = (255, 0, 0)
        self.COLOR_YELLOW = (255, 255, 0)
        self.Y_COUNT = int(5)
        self.X_COUNT = int(8)
        self.PLAYER = 0
        self.AI = 1
        self.PLAYER_PIECE = 1
        self.AI_PIECE = 2
        self.WINNING_WINDOW_LENGTH = 3
        self.EMPTY = 0
        self.WINNING_POSITION = []
        self.SQUARESIZE = 80
        self.width = self.X_COUNT * self.SQUARESIZE
        self.height = (self.Y_COUNT + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)
        self.screen = pygame.display.set_mode(self.size)
    def create_board(self):
        board = np.zeros((self.Y_COUNT, self.X_COUNT))
        return board
    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece
    def is_valid_location(self, board, col):
        return board[self.Y_COUNT - 1][col] == 0
    def get_next_open_row(self, board, col):
        for r in range(self.Y_COUNT):
            if board[r][col] == 0:
                return r
    def print_board(self, board):
        print(np.flip(board, 0))
    def winning_move(self, board, piece):
        self.WINNING_POSITION.clear()
        for c in range(self.X_COUNT - 2):
            for r in range(self.Y_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r, c + 1])
                    self.WINNING_POSITION.append([r, c + 2])
                    return True
        for c in range(self.X_COUNT):
            for r in range(self.Y_COUNT - 2):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r + 1, c])
                    self.WINNING_POSITION.append([r + 2, c])
                    return True
        for c in range(self.X_COUNT - 2):
            for r in range(self.Y_COUNT - 2):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r + 1, c + 1])
                    self.WINNING_POSITION.append([r + 2, c + 2])
                    return True
        for c in range(self.X_COUNT - 2):
            for r in range(2, self.Y_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r - 1, c + 1])
                    self.WINNING_POSITION.append([r - 2, c + 2])
                    return True
    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = self.PLAYER_PIECE
        if piece == self.PLAYER_PIECE:
            opp_piece = self.AI_PIECE
        if window.count(piece) == 3:
            score += 100
        elif window.count(piece) == 2 and window.count(self.EMPTY) == 1:
            score += 5
        if window.count(opp_piece) == 3 and window.count(self.EMPTY) == 1:
            score -= 4
        return score
    def score_position(self, board, piece):
        score = 0
        center_array = [int(i) for i in list(board[:, self.X_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3
        for r in range(self.Y_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(self.X_COUNT - 3):
                window = row_array[c: c + self.WINNING_WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)
        for c in range(self.X_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(self.Y_COUNT - 3):
                window = col_array[r: r + self.WINNING_WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)
        for r in range(self.Y_COUNT - 3):
            for c in range(self.X_COUNT - 3):
                window = [board[r + i][c + i] for i in range(self.WINNING_WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)
        for r in range(self.Y_COUNT - 3):
            for c in range(self.X_COUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(self.WINNING_WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)
        return score
    def is_terminal_node(self, board):
        return self.winning_move(board, self.PLAYER_PIECE) or self.winning_move(board, self.AI_PIECE) or len(
                self.get_valid_locations(board)) == 0
    def AlphaBeta(self, board, depth, alpha, beta, currentPlayer):
        valid_locations = self.get_valid_locations(board)
        value = -math.inf
        column = random.choice(valid_locations)
        '''Implement here'''
        if(depth==0 or self.is_terminal_node(board)):
            if self.is_terminal_node(board):
                if self.winning_move(board, self.AI_PIECE):
                    return (None, 999999999)
                elif self.winning_move(board, self.PLAYER_PIECE):
                    return (None, -99999999)
                else:
                    return (None, 0)

            else:
                return (None, self.score_position(board, self.AI_PIECE))

        column = random.choice(valid_locations)
        if(currentPlayer == True):
            value = -math.inf

            for column_iteration in valid_locations:
                valid_row = self.get_next_open_row(board, column_iteration)
                board_copy = board.copy()
                self.drop_piece(board_copy, valid_row, column_iteration, self.AI_PIECE)
                current_score = self.AlphaBeta(board_copy, depth - 1, alpha, beta, False)[1]

                if current_score > value:
                    value = current_score
                    column = column_iteration
                alpha = max(alpha, value)
                if alpha >= beta:
                    break

        else:
            value = math.inf
            #column = random.choice(valid_locations)
            for column_iteration in valid_locations:
                valid_row = self.get_next_open_row(board, column_iteration)
                board_copy = board.copy()
                self.drop_piece(board_copy, valid_row, column_iteration, self.PLAYER_PIECE)
                current_score = self.AlphaBeta(board_copy, depth - 1, alpha, beta, True)[1]

                if current_score < value:
                    value = current_score
                    column = column_iteration

                beta = min(beta, value)
                if alpha >= beta:
                    break
                    # return self.score_position(self, board,self.AI_PIECE)
        return column, value

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(self.X_COUNT):
            if self.is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations
    def pick_best_move(self, board, piece):
        best_score = -10000
        valid_locations = self.get_valid_locations(board)
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self.get_next_open_row(board, col)
            temp_board = board.copy()
            self.drop_piece(temp_board, row, col, piece)
            score = self.score_position(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col
        return best_col
    def draw_board(self, board):
        for c in range(self.X_COUNT):
            for r in range(self.Y_COUNT):
                pygame.draw.rect(self.screen, self.COLOR_BLUE,
                                 (c * self.SQUARESIZE, r * self.SQUARESIZE + self.SQUARESIZE, self.SQUARESIZE,
                                  self.SQUARESIZE))
                pygame.draw.circle(self.screen, self.COLOR_BLACK, (
                        int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                        int(r * self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE / 2)),
                                   self.RADIUS)
        for c in range(self.X_COUNT):
            for r in range(self.Y_COUNT):
                if board[r][c] == self.PLAYER_PIECE:
                    pygame.draw.circle(self.screen, self.COLOR_RED, (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)),
                                       self.RADIUS)
                elif board[r][c] == self.AI_PIECE:
                    pygame.draw.circle(self.screen, self.COLOR_YELLOW, (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)),
                                       self.RADIUS)
        pygame.display.update()
#endregion
# region KMEANS
class DataItem:
    def __init__(self, item):
        self.features = item
        self.clusterId = -1
    def getDataset(self):
        data = []
        data.append(DataItem([0, 0, 0, 0]))
        data.append(DataItem([0, 0, 0, 1]))
        data.append(DataItem([0, 0, 1, 0]))
        data.append(DataItem([0, 0, 1, 1]))
        data.append(DataItem([0, 1, 0, 0]))
        data.append(DataItem([0, 1, 0, 1]))
        data.append(DataItem([0, 1, 1, 0]))
        data.append(DataItem([0, 1, 1, 1]))
        data.append(DataItem([1, 0, 0, 0]))
        data.append(DataItem([1, 0, 0, 1]))
        data.append(DataItem([1, 0, 1, 0]))
        data.append(DataItem([1, 0, 1, 1]))
        data.append(DataItem([1, 1, 0, 0]))
        data.append(DataItem([1, 1, 0, 1]))
        data.append(DataItem([1, 1, 1, 0]))
        data.append(DataItem([1, 1, 1, 1]))
        return data
class Cluster:
        def __init__(self, id, centroid):
            self.centroid = centroid
            self.data = []
            self.id = id
        def update(self, clusterData):
            self.data = []
            for item in clusterData:
                self.data.append(item.features)
            tmpC = np.average(self.data, axis=0)
            tmpL = []
            for i in tmpC:
                tmpL.append(i)
            self.centroid = tmpL
class SimilarityDistance:
        def euclidean_distance(self, p1, p2):
            distancevalue =0
            for i in range(len(p1)):
                distancevalue+=(p1[i]-p2[i])**2
            return sqrt(distancevalue)
            #pass
        def Manhattan_distance(self, p1, p2):
            distancevalue =0
            for i in range(len(p1)):
                distancevalue+= abs((p1[i]-p2[i]))
            return distancevalue
            #pass
class Clustering_kmeans:
        def __init__(self, data, k, noOfIterations, isEuclidean):
            self.data = data
            self.k = k
            self.distance = SimilarityDistance()
            self.noOfIterations = noOfIterations
            self.isEuclidean = isEuclidean
        def initClusters(self):
            self.clusters = []
            for i in range(self.k):
                self.clusters.append(Cluster(i, self.data[i * 10].features))
        def getClusters(self):
            self.initClusters()
            '''Implement Here'''
            if (self.isEuclidean == 1):
                for iteration in range(self.noOfIterations):
                    for item in self.data:
                        minDistance = 10000
                        for cluster in self.clusters:
                            clusterDistance = self.distance.euclidean_distance(cluster.centroid, item.features)
                            if (clusterDistance < minDistance):
                                item.clusterId = cluster.id
                                minDistance = clusterDistance
                        clusterData = [x for x in self.data if x.clusterId == item.clusterId]
                        self.clusters[item.clusterId].update(clusterData)
                return self.clusters
            else :
                for iteration in range(self.noOfIterations):
                    for item in self.data:
                        minDistance = 100000
                        for cluster in self.clusters:
                            clusterDistance = self.distance.Manhattan_distance(cluster.centroid, item.features)
                            if (clusterDistance < minDistance):
                                item.clusterId = cluster.id
                                minDistance = clusterDistance
                        clusterData = [x for x in self.data if x.clusterId == item.clusterId]
                        self.clusters[item.clusterId].update(clusterData)
                return self.clusters



            pass
# endregion
#################################### Algorithms Main Functions #####################################
# region Search_Algorithms_Main_Fn
def SearchAlgorithm_Main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    fullPath, path = searchAlgo.DFS()
    print('**DFS**\n Full Path is: ' + str(fullPath) +'\n Path is: ' + str(path))
# endregion
#region Gaming_Main_fn
def Gaming_Main():
    game = Gaming()
    board = game.create_board()
    game.print_board(board)
    game_over = False
    pygame.init()
    game.draw_board(board)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 50)
    turn = 1
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(game.screen, game.COLOR_BLACK, (0, 0, game.width, game.SQUARESIZE))
                posx = event.pos[0]
                if turn == game.PLAYER:
                    pygame.draw.circle(game.screen, game.COLOR_RED, (posx, int(game.SQUARESIZE / 2)), game.RADIUS)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(game.screen, game.COLOR_BLACK, (0, 0, game.width, game.SQUARESIZE))
                if turn == game.PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx / game.SQUARESIZE))
                    if game.is_valid_location(board, col):
                        row = game.get_next_open_row(board, col)
                        game.drop_piece(board, row, col, game.PLAYER_PIECE)
                        if game.winning_move(board, game.PLAYER_PIECE):
                            label = myfont.render("Player Human wins!", 1, game.COLOR_RED)
                            print(game.WINNING_POSITION)
                            game.screen.blit(label, (40, 10))
                            game_over = True
                        turn += 1
                        turn = turn % 2
                        # game.print_board(board)
                        game.draw_board(board)
        if turn == game.AI and not game_over:
            col, minimax_score = game.AlphaBeta(board, 5, -math.inf, math.inf, True)
            if game.is_valid_location(board, col):
                row = game.get_next_open_row(board, col)
                game.drop_piece(board, row, col, game.AI_PIECE)
                if game.winning_move(board, game.AI_PIECE):
                    label = myfont.render("Player AI wins!", 1, game.COLOR_YELLOW)
                    print(game.WINNING_POSITION)
                    game.screen.blit(label, (40, 10))
                    game_over = True
                # game.print_board(board)
                game.draw_board(board)
                turn += 1
                turn = turn % 2
        if game_over:
            pygame.time.wait(3000)
            return game.WINNING_POSITION
#endregion
# region KMeans_Main_Fn
def Kmeans_Main():
    dataset = DataItem.getDataset(1)
    # 1 for Euclidean and 0 for Manhattan
    clustering = Clustering_kmeans(dataset, 2, len(dataset),1)
    clusters = clustering.getClusters()
    for cluster in clusters:
        for i in range(4):
            cluster.centroid[i] = round(cluster.centroid[i], 2)
        print(cluster.centroid[:4])
    return clusters
# endregion
######################## MAIN ###########################33
if __name__ == '__main__':
    SearchAlgorithm_Main()
    Gaming_Main()
    Kmeans_Main()

