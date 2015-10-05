
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

def factor_list(factors):
   for num in factors:
      #print "num=", num
      i = 2
      while i < num / 2 + 1:
         #print "i=", i
         if num % i == 0:
            #print "Factor found!"
            #print factors, " -> ",
            factors.remove(num)
            factors.append(i)
            factors.append(num / i)
            #print factors
            return (factors, True)
         else:
            i += 1
   return (factors, False)


primes = [2]
curr_num = 3
while curr_num < 2000000:
   factors = [curr_num]
   (factors, factor_found) = factor_list(factors)
   if not factor_found and len(factors) == 1:
      primes.append(factors[0])
      if len(primes) % 100 == 0:
         print "Found %d primes (@ %d)." % (len(primes), primes[-1])
   curr_num += 2

print "%d primes were found." % len(primes)
print
print "Answer = ", sum(primes)
