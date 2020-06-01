#!/usr/bin/env python3

# global variables for size of board and the board itself
emptycell = "."
boardsize = 4
theBoard = [[emptycell] * boardsize for i in range(boardsize)]

def print_board(board):
	for row in board:
		print(' '.join([elem for elem in row]))
	print('')

def print_bool(alwaysPrint, boolInput)
	if boolInput:
		print(alwaysPrint + ' true')
	else:
		print(alwaysPrint + ' false')

def placeboat(board, inrow, incol, boatlength, direction, marker):
	returnVal = False
	if direction == 'horizontal':
		if incol <= (boardsize - boatlength):
			#print(f'Attempting to place boat horizontally at {inrow}, {incol}')
			ableToPlace = True
			for i in range (incol, incol + boatlength):
				if board[inrow][i] != emptycell:
					ableToPlace = False
			if ableToPlace:
				print(f'Placing boat horizontally at {inrow}, {incol}')
				for i in range (incol, incol + boatlength):
					board[inrow][i] = marker
				returnVal = True
				print_board(board)
			else:
				print(f'Cannot place boat horizontally at {inrow}, {incol}')
		else:
			print(f'Cant place boat horizontally at {inrow}, {incol}')
	else:
		if inrow <= (boardsize - boatlength):
			#print(f'Attempting to place boat vertically {inrow}, {incol}')
			ableToPlace = True
			for i in range (inrow, inrow + boatlength):
				if board[i][incol] != emptycell:
					ableToPlace = False
			if ableToPlace:
				print(f'Placing boat vertically at {inrow}, {incol}')
				for i in range (inrow, inrow + boatlength):
					board[i][incol] = marker
				returnVal = True
				print_board(board)
			else:
				print(f'Cannot place boat vertically at {inrow}, {incol}')
		else:
			print(f'Cant place boat vertically at {inrow}, {incol}')
	return returnVal

def testing():
	# indices start at 0, and not just because RANGE (above) starts at zero.
	#theBoard[0][0] = 'A'
	#theBoard[2][3] = 'B'
	#theBoard[3][2] = 'C'
	#print_board(theBoard)
	#placeboat(theBoard, 0, 0, 3, 'horizontal', 'X')
	print_bool('able to place at 1,1', placeboat(theBoard, 1, 1, 3, 'horizontal', 'X'))
	print_bool('able to place at 1,3', placeboat(theBoard, 1, 1, 3, 'horizontal', 'X'))

def main():
	testing()

	#for i in range(boardsize):
	#	for j in range(boardsize):
	#		placeboat(i, j, theBoard, 3, 'X')

# need this to make this run from command line
if __name__ == '__main__':
	main()



