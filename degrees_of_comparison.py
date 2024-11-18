import re
from segment import Adj_F

def degrees_of_comparison(word: str) -> str:
    
    suppletives = {
        "хорош" : "кращ",
        "гарн" : "кращ",
        "поган" : "гірш",
        "велик" : "більш",
        "мал" : "менш"
    }
    
    R = ["м'як", "різк", "лег", "гірк", "яскрав"]

    flexions = {
        "я" : "а",
        "ю" : "у",
        "є" : "е",
        "ій" : "ий",
    }

    O_cut = ["довг"]

    P = "най"
    S1 = "іш"
    S2 = "ш"
    S3 = "ч"
    S = S1
    
    try:
        O, F = Adj_F(word)
    except ValueError:
        return 'Слово не є прикметником.'

    bad_suffix = re.findall(r"(ісіньк|юсіньк|еньк|ав|яв|уват|юват|яст|енн|езн|ющ|ущ|ащ|ист|ляв)\b", O) \
        and O not in R
    bad_prefix = re.findall(r"\b(пре|за|над|пра)", O) \
        and O not in R
    not_applicable = bad_suffix or bad_prefix

    if not_applicable:
        return 'Слово не має ступенів порівняння.'
    elif O in suppletives:
        O = suppletives[O]
        S = ""
    else:
        if O in O_cut:
            O = O[:-1]
            S = S2
        else:
            cut_ok_ek = re.findall(r"([\w\']+)(ок|ек)\b", O)
            cut_k = re.findall(r"([\w\']+)(к)\b", O)
            if cut_ok_ek and O not in R:
                O = (cut_ok_ek[0])[0]
                if O.endswith('л'):
                    O += "ь"
                    S = S2
            elif not cut_ok_ek and cut_k and O not in R:
                O = (cut_k[0])[0]
                S = S2

            alternate_h = re.findall(r"г\b", O)
            alternate_z = re.findall(r"зь\b", O)
            alternate_s = re.findall(r"с\b", O)

            if alternate_h and O not in O_cut:
                O = re.sub(r"г\b", "ж", O)
                S = S3
            if alternate_z:
                O = re.sub(r"зь\b", "ж", O)
                S = S3
            elif alternate_s:
                O = re.sub(r"с\b", "щ", O)
                S = S3

            if S == S3 and O.endswith("щ"):
                S = ""

            if O.endswith("ж"):
                S = S3 

    if F in flexions.keys():
        F = flexions[F]

    higher_degree = O + S + F
    highest_degree = P + higher_degree

    return f"{higher_degree}, {highest_degree}"

test_list = [
    "далека", "веселу", "сильним", "швидкий", "розумного",
    "хороший", "поганий", "великий", "малий", "широкий", "м'який",
    "важкий", "складний", "високий", "низький", "старий", "молодий",
    "холодний", "теплий", "смачному", "гострий", "багатий", "світлий",
    "тяжкий", "коротких", "вузький", "дужий", "густий", "міцний",
    "яскравий", "тривожний", "щасливий", "сумне", "синє", "злий",
    "добрий", "прозорий", "гарячий", "огидний", "різкий", "темний",
    "солодкий", "кислий", "гіркий", "солоний", "рідний", "дурний",
    "твердий", "красивий", "чудових"
]

for word in test_list:
    print(word)
    print(degrees_of_comparison(word))