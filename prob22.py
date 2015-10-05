# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
# by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

FIRST_NAME_FILE = "p022_names.txt"

# Compute alphabet dict.
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
LETTER_TO_POS = dict([(v, i + 1) for i, v in enumerate(ALPHABET)])


def read_names(filename):
    """
    Read in all names from file into an array.
    """
    with open(filename, "r") as nameFile:
        all_names = nameFile.readline().replace('"', '').split(',')
    return all_names

def compute_name_score(name):
    """
    Compute the name score, given a name, by summing each letter position.
    For example, COLIN is worth 3 + 15 + 12 + 9 + 14 = 53
    """
    scores = [LETTER_TO_POS[letter.lower()] for letter in name]
    return sum(scores)

def main():

    all_names = sorted(read_names(FIRST_NAME_FILE))
    #print all_names
    all_scores = [compute_name_score(name) for name in all_names]
    #print all_scores
    adjusted_scores = [score * (i + 1) for i, score in enumerate(all_scores)]
    #print adjusted_scores
    print "Answer = ", sum(adjusted_scores)

main()
