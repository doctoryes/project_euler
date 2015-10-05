
oldest_num = 1
old_num = 1
curr_num = 1
sum = 0

print old_num

while curr_num < 4000000:
      print curr_num
      oldest_num = old_num
      old_num = curr_num
      curr_num = old_num + oldest_num
      if curr_num % 2 == 0:
	 sum += curr_num

print "Sum = ", sum

      
      
