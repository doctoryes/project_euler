
#
#
#
#  56
#  56 / 2 = 28
#  2, 28
#  28 / 2 = 14
#  2, 2, 14
#  14 / 2 = 7
#  2, 2, 2, 7
#  [2, 2, 2, 7]

#[ 56 ]
#-> [2, 28]
#-> [2, 2, 14]
#-> [2, 2, 2, 7]
#-> [2, 2, 2, 7]

def factor_list(factors):
    for num in factors:
	#print "num=", num
	i = 2
	while i < num / 2 + 1:
	    #print "i=", i
	    if num % i == 0:
	       print "Factor found!"
	       print factors, " -> ",
	       factors.remove(num)
	       factors.append(i)
	       factors.append(num / i)
	       print factors
	       return (factors, True)
	    else:
	       i += 1
    return (factors, False)

num_list = [ 600851475143 ]
while 1:
   (x, factor_found) = factor_list(num_list)
   if not factor_found:
      print num_list
      break
   num_list = x



	    

