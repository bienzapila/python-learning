def get_anagram(word):
    ans = list(word)
    import random as rnd

    rnd.shuffle(ans)
    final = "".join(ans)
    return final
