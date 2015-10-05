#!/usr/bin/env python
# -*- coding: latin-1 -*-



# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
#  there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

GRID_DIMENSION = 20

def gotoLowerRight(curr_path, row, col):
	#print "Row: %d  Col: %d" % (row, col)

	right_solutions = 0
	down_solutions = 0

	# Has the path reached the lower right dot?
	if row == GRID_DIMENSION and col == GRID_DIMENSION:
		#print "--------"
		#print curr_path
		return 1

	# If the path can go right, send it right.
	if col != GRID_DIMENSION:
		# Save of the right dot into the path.
		#new_path = list(curr_path)
		#new_path.append((row, col+1))
		new_path = []
		right_solutions = gotoLowerRight(new_path, row, col+1)

	# If the path can go down, send it down.
	if row != GRID_DIMENSION:
		# Save of the down dot into the path.
		#new_path = list(curr_path)
		#new_path.append((row+1, col))
		new_path = []
		down_solutions = gotoLowerRight(new_path, row+1, col)

	return right_solutions + down_solutions

print "Answer: ", gotoLowerRight([], 0, 0)

