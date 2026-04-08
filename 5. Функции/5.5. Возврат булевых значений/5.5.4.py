def convert_to_python_case(text):
    nt = ""
    for i in range(len(text)):
        if i == 0:
            nt += text[0].lower()
            continue
        if text[i] == text[i].lower():
            nt += text[i]
        else:
            nt = nt + "_" + text[i].lower()
    return nt
