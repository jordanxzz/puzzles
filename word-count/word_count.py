from collections import Counter
def count_words(sentence):
    return dict(Counter(sentence.split(' ')))
