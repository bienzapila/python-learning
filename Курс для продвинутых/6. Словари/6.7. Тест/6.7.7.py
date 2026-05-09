def merge(values):
    final = {}
    for i in range(len(values)):
        for key in values[i].keys():
            if key not in final:
                final[key] = {values[i][key]}
            else:
                final[key].add(values[i][key])
    return final
