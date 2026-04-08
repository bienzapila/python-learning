def is_one_away(word1, word2):
    if len(word1) == len(word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                cnt += 1
        if cnt == len(word1) - 1:
            return True
        else:
            return False
    else:
        return False
