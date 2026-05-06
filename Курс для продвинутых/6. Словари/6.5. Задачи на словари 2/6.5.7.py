def scrabble(letters, word):
    let = {}
    for s in letters.lower():
        if s not in let:
            let[s] = 1
        else:
            let[s] += 1

    wor = {}
    for s in word.lower():
        if s not in wor:
            wor[s] = 1
        else:
            wor[s] += 1

    for key in wor.keys():
        if key in let:
            if wor[key] == let[key]:
                continue
            else:
                return False
                break
        else:
            return False
            break
    else:
        return True


print(scrabble("BEEGEEK", "geekbee"))
