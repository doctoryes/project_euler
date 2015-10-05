

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0
square_of_sums = 0
for i in xrange(1, 101):
   sum_of_squares += pow(i, 2)
   square_of_sums += i
print "Sum of squares = ", sum_of_squares
square_of_sums = pow(square_of_sums, 2)
print "Square of sums = ", square_of_sums
print "Answer: ", square_of_sums - sum_of_squares




   
