
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for x in range(1, 1000):
   for y in range(2, 1000):
      if x > y:
         # Increase y until greater than x.
         continue
      for z in range(3, 1000):
         if y > z:
            # Increase z until greater than y.
            continue
         elif x + y + z != 1000:
            # Not the answer.
            continue
         x_sq = x * x
         y_sq = y * y
         lval = x_sq + y_sq
         z_sq = z * z
         if lval == z_sq:
            print "%5d^2 + %5d^2 = %5d^2" % (x, y, z)
            if x + y + z == 1000:
               print "ANSWER!!!! Product abc = ", x*y*z
               exit()
         elif lval < z_sq:
            # No point in increasing z anymore.
            break
               
