#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Power digit sum
# Problem 16

# 2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2 ^ 1000?

total = 0
x = 2 ** 1000
strX = str(x)
print strX
for str_num in strX:
	#print str_num
	n = int(str_num)
	total += n

print "Answer: ", total

