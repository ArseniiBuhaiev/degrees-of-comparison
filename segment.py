import re

def Adj_F(word:str) -> str:
    word = (word.strip()).casefold()

    F_21 = r"([\w\']+)(ого|ому|ими)\b"
    F_22 = r"([\w\']+)(ий|им|ім|ої|ій|ою|их)\b"
    F_23 = r"([\w\']+)(я|є|е|а|у|і|ю)\b"

    proc21 = re.findall(F_21, (word))
    proc22 = re.findall(F_22, (word))
    proc23 = re.findall(F_23, (word))

    if proc21:
        O = (proc21[0])[0]
        F = (proc21[0])[1]
    elif proc22:
        O = (proc22[0])[0]
        F = (proc22[0])[1]
    elif proc23:
        O =( proc23[0])[0]
        F = (proc23[0])[1]
    else:
        return f"Слово \"{word}\" — не прикметник."

    return O, F