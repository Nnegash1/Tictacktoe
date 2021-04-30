import numpy as np

BOARD = numpy.zeros((8,8))

def printBoard():
    for i in range(8):
        for j in range(8):
            print('--', i,j,'--|', end='')
        
        print('\n')

