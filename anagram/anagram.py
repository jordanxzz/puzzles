def find_anagrams(word, candidates):
    anagrams = []
    for i in range(len(candidates)):
        curr_cand = candidates[i]
        word_new = word
        for j in range(len(curr_cand)):
            curr_cand_lett = curr_cand[j]
            if (curr_cand_lett in word_new) and (len(word_new) > 0):
                word_new = word_new.replace(curr_cand_lett, "", 1)
            elif
