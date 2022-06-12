#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

longest_sequence = []

for x in xrange(1,1000001):
	sequence = [x]
	while sequence[-1] != 1:
		last_num = sequence[-1]
		if last_num % 2 == 0:
			# Even.
			sequence.append(last_num / 2)
		else:
			# Odd.
			sequence.append(3 * last_num + 1)

	# Done - last term in sequence is one.
	if len(sequence) > len(longest_sequence):
		print "Longest chain so far - length %5d - starts with %6d" % (len(sequence), sequence[0])
		print sequence
		longest_sequence = sequence

print "Answer: %6d" % len(longest_sequence)

