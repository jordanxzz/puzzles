def count_words(sentence):
    sentence = sentence.lower()
    sentence_unique = sentence.split()
    for word in sentence_unique:
        if(sentence_unique.count(word) > 1):
            sentence_unique.remove(word)
    for word in sentence_unique:
        count = sentence.count(word)
        print(word + ": " + str(count))
