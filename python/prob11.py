#!/usr/bin/env python
# -*- coding: latin-1 -*-

# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# 
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
# 
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# 
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

NUMBER_GRID = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

GRID_DIMENSION = 20
NUMBERS_IN_PRODUCT = 4

class ParseException(Exception):
   pass

class NumberGrid:
   def __init__(self, gridStr):
      self.grid = self._readGridStr(gridStr, GRID_DIMENSION)

   def _readGridStr(self, gridStr, dim):
      # Parses a grid string representing a number grid.
      # Results in a multi-dimensional list of numbers.
      grid_lines_raw = gridStr.splitlines()

      # Strip out any blank lines.
      grid_lines = [x for x in grid_lines_raw if len(x) != 0]
      if len(grid_lines) != dim:
         e_str = "Expected %d lines - got %d" % (dim, len(grid_lines))
         raise ParseException(e_str)

      grid_arr = []
      for line in grid_lines:
         num_arr = line.split()
         if len(num_arr) != dim:
            e_str = "Expected %d columns - got %d in row: %s" % (dim, len(num_arr), line)
            raise ParseException(e_str)
         num_arr = [int(x) for x in num_arr]
         grid_arr.append(num_arr)
      return grid_arr

   def dump(self):
      for i in range(0, len(self.grid)):
         row = ' '.join(['%02d' % x for x in self.grid[i]])
         print row

   def _productOfFour(self, fourNumList):
      if len(fourNumList) != NUMBERS_IN_PRODUCT:
         raise Exception("Expected four number - got %d" % len(fourNumList))
      prod = 1
      for i in range(0, NUMBERS_IN_PRODUCT):
         prod *= fourNumList[i]
      return prod

   def _findMaxProduct(self, numLists):
      "Pass in a list of four number lists. Computes the maximum product."
      max_product = 0
      max_nums = None
      for num_list in numLists:
         prod = self._productOfFour(num_list)
         if prod > max_product:
            max_product = prod
            max_nums = num_list
      return (max_product, max_nums)

   def _computeProductsVertical(self, numberGrid):
      num_lists = []
      for i in range(0, GRID_DIMENSION - NUMBERS_IN_PRODUCT + 1):
         zipped = zip(numberGrid[i], numberGrid[i+1], numberGrid[i+2], numberGrid[i+3])
         for num_list in zipped:
            num_lists.append(num_list)
      return self._findMaxProduct(num_lists)

   def _computeProductsHorizontal(self, numberGrid):
      grid_transpose = zip(*numberGrid)
      return self._computeProductsVertical(grid_transpose)

   def _computeProductsDiagUp(self, numberGrid):
      """
      Computes the upward diagonal products. In a picture, it's the numbers shown as '**':

      01 14 87 **
      32 76 ** 11
      31 ** 02 48
      ** 79 97 55

      Shift the rows so that the problem turns into vertical product calculation.
      """
      num_lists = []
      for i in range(0, GRID_DIMENSION - NUMBERS_IN_PRODUCT + 1):
         rows = []
         for j in range(0, NUMBERS_IN_PRODUCT):
            rowFrom = 3 - j
            rowTo   = len(numberGrid[i+j]) - j
            rows.append(numberGrid[i+j][rowFrom:rowTo])
         #print rows
         zipped = zip(*rows)
         #print zipped
         for num_list in zipped:
            num_lists.append(num_list)
      return self._findMaxProduct(num_lists)

   def _computeProductsDiagDown(self, numberGrid):
      """
      Computes the downward diagonal products. In a picture, it's the numbers shown as '**':

      ** 14 87 01
      32 ** 76 11
      31 02 ** 48
      80 79 97 **

      Shift the rows so that the problem turns into vertical product calculation.
      """
      num_lists = []
      for i in range(0, GRID_DIMENSION - NUMBERS_IN_PRODUCT + 1):
         rows = []
         for j in range(0, NUMBERS_IN_PRODUCT):
            rowFrom = j
            rowTo   = len(numberGrid[i+j]) - (3 - j)
            rows.append(numberGrid[i+j][rowFrom:rowTo])
         #print rows
         zipped = zip(*rows)
         #print zipped
         for num_list in zipped:
            num_lists.append(num_list)
      return self._findMaxProduct(num_lists)

   def findMaxProduct(self):
      max_products = {}
      max_nums = {}
      (max_products['vertical'], max_nums['vertical']) = self._computeProductsVertical(self.grid)
      (max_products['horizontal'], max_nums['horizontal']) = self._computeProductsHorizontal(self.grid)
      (max_products['diagup'], max_nums['diagup']) = self._computeProductsDiagUp(self.grid)
      (max_products['diagdown'], max_nums['diagdown']) = self._computeProductsDiagDown(self.grid)
      for direction in ('Vertical', 'Horizontal', 'DiagUp', 'DiagDown'):
         print "%s max:" % direction
         print max_products[direction.lower()], " - ", max_nums[direction.lower()]

def main():
   grid = NumberGrid(NUMBER_GRID)
   print "Number grid:"
   grid.dump()
   grid.findMaxProduct()
   

if __name__ == "__main__":
    main()
