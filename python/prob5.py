
# Problem 5:

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


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

#num_list = [ 600851475143 ]
#while 1:
#   (x, factor_found) = factor_list(num_list)
#   if not factor_found:
#      print num_list
#      break
#   num_list = x

# Combines two lists of factors 
def combine_factors(factors, factors_to_combine):
    # Make a copy of factors.
    combined_factors = list(factors)
    remaining_factors = list(factors)
    for factor in factors_to_combine:
        if factor in remaining_factors:
            # Factor already exists. Remove it from remaining.
            remaining_factors.remove(factor)
        else:
            # Factor doesn't exist. Add it to the combined.
            combined_factors.append(factor)
    return combined_factors

def main():
    all_factors = []
    for i in range(20, 1, -1):
        factor_found = True
        num_list = [i]
        while factor_found:
            (factors, factor_found) = factor_list(num_list)
            num_list = factors
        #print "factors: " , factors
        all_factors = combine_factors(all_factors, factors)
        print "all_factors: ", all_factors
    answer = 1
    for factor in all_factors:
        answer *= factor
    print "Answer = ", answer

if __name__ == "__main__":
    main()


	    

