

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10,001st prime number?

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
while len(primes) < 10002:
   factors = [curr_num]
   (factors, factor_found) = factor_list(factors)
   if not factor_found and len(factors) == 1:
      primes.append(factors[0])
      if len(primes) % 100 == 0:
         print "Found %d primes." % len(primes)
   curr_num += 2

print primes
print
print "Answer = ", primes[10000]
