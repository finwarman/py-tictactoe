#!/usr/bin/env python3

import os  # os for 'clear' terminal command.
import numpy as np


def clear():  # set correct clear command for the current OS
    os.system('cls' if os.name == 'nt' else 'clear')


# define blank 2D board array:
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

pieces = ['x', 'o']
currentPlayer = 0


def printBoard(board):
    print()
    for row in board:
        for square in row:
            print(" {} ".format(square), end="")
        print()


def checkWin(board):
    # check rows:
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':
            return True
    # check columns:
    rotated = zip(*board[::-1])
    for row in rotated:
        if len(set(row)) == 1 and row[0] != '-':
            return True
    # check diagonals:
    if board[1][1] != '-':
        return board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]
    return False


def isValidMove(move, board):
    if not move.isdigit():
        return False
    if not (1 <= int(move) <= 9):
        return False
    move = int(move)-1
    row = move // 3
    column = move % 3
    if board[row][column] != '-':
        return False
    return move


def checkDraw(board):
    if not checkWin and (board != '-').all():
        return True
    return False


def makeMove(board, piece):
    move = False
    while move is False:
        clear()
        printBoard(board)
        print(
            "\nchoose square 1-9 \n{} to move!\n".format(pieces[currentPlayer]))
        move = isValidMove(input(), board)

    row = move // 3
    column = move % 3
    board[row][column] = piece


gameWon = False
while not gameWon:
    if(checkDraw(board)):
        print("\n *+*+*+*\n Nobody Won :(\n *+*+*+*\n")
    makeMove(board, pieces[currentPlayer])
    if checkWin(board):
        clear()
        printBoard(board)
        print(
            '\n *+*+*+*\n {} wins!\n *+*+*+*\n'.format(pieces[currentPlayer]))
        gameWon = True
    currentPlayer = (currentPlayer+1) % 2
