from collections import Counter
def is_isogram(string):
    counter = Counter(string)
    for i in counter:
        if counter[i] > 1 and i != ' ' and i != '-':
            return True
    return False
