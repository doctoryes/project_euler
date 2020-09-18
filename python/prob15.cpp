#include <iostream>

const size_t GRID_DIMENSION = 20;

size_t gotoLowerRight(size_t row, size_t col)
{
	size_t right_solutions = 0;
	size_t down_solutions = 0;

	// Has the path reached the lower right dot?
	if (row == GRID_DIMENSION && col == GRID_DIMENSION)
		//print "--------"
		//print curr_path
		return 1;

	// If the path can go right, send it right.
	if (col != GRID_DIMENSION)
	{
		// Save of the right dot into the path.
		//new_path = list(curr_path)
		//new_path.append((row, col+1))
		right_solutions = gotoLowerRight(row, col+1);
	}

	// If the path can go down, send it down.
	if (row != GRID_DIMENSION)
	{
		// Save of the down dot into the path.
		//new_path = list(curr_path)
		//new_path.append((row+1, col))
		down_solutions = gotoLowerRight(row+1, col);
	}

	return right_solutions + down_solutions;
}

int main()
{
	std::cout << "Answer: " << gotoLowerRight(0, 0) << std::endl;
}
