
# def fibonacci_until(index, term1, term2, num_digits_limit):
#     new_term = term1 + term2
#     if len('{}'.format(new_term)) >= num_digits_limit:
#         return "Answer: Index {} with number {}".format(index + 1, new_term)
#     else:
#         return fibonacci_until(index + 1, term2, new_term, num_digits_limit)

# print fibonacci_until(3, 1, 2, 100)


index = 3
term1 = 1
term2 = 2
num_digits_limit = 1000

while True:
    new_term = term1 + term2
    if len('{}'.format(new_term)) >= num_digits_limit:
        print "Answer: Index {} with number {}".format(index + 1, new_term)
        break
    index += 1
    term1 = term2
    term2 = new_term
