# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def compute_proper_div_sum(num):
    i = 1
    count = 0
    while i < (num / 2) + 1:
        if num % i == 0:
            count += i
        i += 1
    return count


def main():
    divSums = {}
    # Compute all the sums of proper divisors.
    for i in range(1, 10001):
        div_sum = compute_proper_div_sum(i)
        divSums[i] = div_sum

    # Iterate through the sums to find amicable numbers.
    amicables = []
    for k, v in divSums.iteritems():
        if k in amicables or v in amicables or k == v:
            continue
        if divSums.has_key(k) and divSums[k] == v and divSums.has_key(v) and divSums[v] == k:
            amicables.append(k)
            amicables.append(v)

    print "Amicables = {}".format(amicables)
    print "Answer = {}".format(sum(amicables))

main()

