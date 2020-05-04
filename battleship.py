#!/usr/bin/env python3

# global variables for size of board and the board itself
emptycell = "."
boardsize = 4
theBoard = [[emptycell] * boardsize for i in range(boardsize)]

def print_board(board):
	for row in board:
		print(' '.join([elem for elem in row]))
	print('')

def placeboat(inrow, incol, board, boatlength, marker):
	#attempt horizontal placement
	if incol > (boardsize - boatlength):
		print(f'Cant place boat horizontally at {inrow}, {incol}')
	else:
		print(f'Attempting to place boat horizontally at {inrow}, {incol}')
		ableToPlace = True
		for i in range (incol, incol + boatlength):
			if board[inrow][i] != emptycell:
				ableToPlace = False
		if ableToPlace:
			print(f'Placing boat horizontally at {inrow}, {incol}')
			for i in range (incol, incol + boatlength):
				board[inrow][i] = marker
		else:
			print(f'Cannot place boat horizontally at {inrow}, {incol}')
		print_board(board)

	#attempt vertical placement
	#if inrow > (boardsize - boatlength):
	#	print(f'Cant place boat vertically at {inrow}, {incol}')
	#else:
	#	print(f'Will attempt to place boat vertically at {inrow}, {incol}')

def testing():
	# indices start at 0, and not just because RANGE (above) starts at zero.
	#theBoard[0][0] = 'A'
	#theBoard[2][3] = 'B'
	#theBoard[3][2] = 'C'
	#print_board(theBoard)
	#placeboat(0, 0, theBoard, 3, 'X')  #OK
	#placeboat(1, 1, theBoard, 3, 'X')  #OK
	#placeboat(0, 2, theBoard, 3, 'X')  #OK
	#placeboat(1, 0, theBoard, 3, 'X')  #OK
	pass

def main():
	#testing()

	for i in range(boardsize):
		for j in range(boardsize):
			placeboat(i, j, theBoard, 3, 'X')

# need this to make this run from command line
if __name__ == '__main__':
	main()



