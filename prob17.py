

# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


NUM_TO_STR = {
#	0 : 'zero',
	1 : 'one',
	2 : 'two',
	3 : 'three',
	4 : 'four',
	5 : 'five',
	6 : 'six',
	7 : 'seven',
	8 : 'eight',
	9 : 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety'
}

class Number:
	def __init__(self, num):
		assert num > 0
		assert num < 10000
		self.num = num

	def _numToStr(self, num):
		assert num >= 0 and num < 10
		assert NUM_TO_STR.has_key(num)
		return NUM_TO_STR[num]

	def _partThousands(self, num):
		if num == 0:
			return ""
		return self._numToStr(num) + " thousand"

	def _partHundreds(self, num):
		if num == 0:
			return ""
		return self._numToStr(num) + " hundred"

	def _partTensOnes(self, num):
		assert num >= 0 and num < 100
		if NUM_TO_STR.has_key(num):
			return NUM_TO_STR[num]
		numWord = ""
		numStr = "%02d" % num
		tensNum = (num / 10) * 10
		onesNum = num % 10
		assert NUM_TO_STR.has_key(tensNum)
		assert NUM_TO_STR.has_key(onesNum)
		return NUM_TO_STR[tensNum] + "-" + NUM_TO_STR[onesNum]

	def asWord(self):
		numStr = "%04d" % self.num
		numWord = ""
		thousands = False
		hundreds = False
		if numStr[0] != '0':
			numWord += self._partThousands(int(numStr[0]))
			thousands = True
		if numStr[1] != '0':
			numWord += self._partHundreds(int(numStr[1]))
			hundreds = True
		if numStr[2] != '0' or numStr[3] != '0':
			if hundreds:
				numWord += " and "
			numWord += self._partTensOnes(int(numStr[2:4]))
		return numWord


def main():
	assert Number(1000).asWord() == 'one thousand'
	print Number(999).asWord()
	assert Number(999).asWord() == 'nine hundred and ninety-nine'
	answer = 0
	for i in range(1, 1001):
		num = Number(i)
		numWord = num.asWord()
		letterCount = 0
		for c in numWord:
			if c != ' ' and c != '-':
				letterCount += 1
		print i, " = ", num.asWord(), "(", letterCount, ")"
		answer += letterCount
	print "Answer = ", answer

if __name__ == "__main__":
	main()
