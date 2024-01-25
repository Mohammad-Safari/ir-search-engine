halfspace = "\u200c"
punctuations = ".,?!;:"
id_pattern, number_pattern, email_pattern = (r"\B@\w+", r"\b\d+\b", r"\b\w+@\w+\.\w+\b")
# keeping half-spaced parts in a token
token_pattern = rf"{email_pattern}|{id_pattern}|{number_pattern}|\b[\w{halfspace}]+"

affix_list_15 = {
    "post": [
        "ی",
        "ای",
        "ها",
        "های",
        "هایی",
        "تر",
        "تری",
        "ترین",
        "گر",
        "گری",
        "ام",
        "ات",
        "اش",
    ],
    "pre": ["می", "نمی"],
}
same_chars_3 = {"ی": ["ي"], "ا": ["آ"], "ک": ["ك"]}
same_terms_15 = {
    "﷽": ["بسم االله الرحمن الرحیم"],
    "آینه": ["آیینه"],
    "تاق": ["طاق"],
    "لوت": ["لوط"],
    "بلیت": ["بلیط"],
    "زغال": ["ذغال"],
    "هیأت": ["هیئت"],
    "رییس": ["رئیس"],
    "تزیین": ["تزئین"],
    "مسئله": ["مسأله"],
    "روبات": ["ربات"],
    "پروفسور": ["پرفسور"],
    "غورباغه": ["قورباغه"],
    "چهارچوب": ["چارچوب"],
    "تئاتر": ["تیاتر", "تآتر"],
}
same_digits = {
    "0":["۰","٠"],
    "1":["۱","١"],
    "2":["۲","٢"],
    "3":["۳","٣"],
    "4":["۴","٤"],
    "5":["۵","٥"],
    "6":["۶","٦"],
    "7":["۷","٧"],
    "8":["۸","٨"],
    "9":["۹","٩"],
}