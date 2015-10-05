
def is_palindrome(x):
    print "Checking %d..." % x
    y = list(str(x))
    for i in range(0, len(y) / 2):
	#print "Comparing %s to %s - " % (y[i], y[len(y)-i-1]), 
	if y[i] != y[len(y)-i-1]:
	   #print "No!"
	   return False	
    print "Palindrome!"
    return True

#is_palindrome(9098778909)

palindromes = []

for x in range(100, 999):
    for y in range(x, 999):
	z = x * y
	if is_palindrome(z):
	   if z not in palindromes:
	      palindromes.append(z)

palindromes.sort()
print palindromes
print palindromes[-1]
