import math
from common.math_util import get_divisors

def factor(num, results=[]):
    for div in range(2, int(math.sqrt(num) + 1)):
        if num % div == 0:
            return factor(div, results) + factor(num / div, results)
    return [num]


#print factor(31493242849887234930)
print get_divisors(31493242849887234930)