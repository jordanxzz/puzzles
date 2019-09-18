import re

def count_words(sentence):
    sentence = re.sub('[^A-Za-z0-9\']+', ' ', sentence).lower()
    sentence_unique = sentence.split()
    count_dict = {}
    for word in sentence_unique:
        if(sentence_unique.count(word) > 1):
            sentence_unique.remove(word)
    for word in sentence_unique:
        count = sentence.count(word)
        count_dict.update({word : count})
    return(count_dict)