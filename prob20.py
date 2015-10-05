# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math

f = math.factorial(100)
print f
f_str = "{}".format(f)
print f_str
count = 0
for n in f_str:
    count += int(n)
print "Answer = ", count
