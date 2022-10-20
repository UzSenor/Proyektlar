import re
matn = input("Matn: ")

# Lotin-kirill so'zlar uchun
latin_suzlar = {
    "sentabr":"сентябр",                   "Sentabr":"Сентябр",          
    "oktabr":"октябр",                     "Oktabr":"Октябр",
    "budjet":"бюджет",                     "Budjet":"Июджет", 
    "seziy":"цезий",                       "Seziy":"Цезий", 
    "seytnot":"цейтнот",                   "Seytnot":"Цейтнот", 
    "sellofan":"целлофан",                 "Sellofan":"Целлофан", 
    "sellyuloza":"целлюлоза",              "Sellyuloza":"Целлюлоза", 
    "selsiy":"целсий",                     "Selsiy":"Целсий", 
    "sement":"цемент",                     "Sement":"Цемент", 
    "senzor":"цензор",                     "Senzor":"Цензор", 
    "senzura":"цензура",                   "Senzura":"Цензура", 
    "sentner":"центер",                    "Sentner":"Центер", 
    "sex":"цех",                           "Sex":"Цех", 
    "setse":"цетсе",                       "Setse":"Цетсе", 
    "sivilizatsiya":"цивилизация",         "Sivilizatsiya":"Цивилизация", 
    "sikl":"цикл",                         "Sikl":"Цикл", 
    "siklon":"циликон",                    "Siklon":"Циликон", 
    "silindr":"цилиндр",                   "Silindr":"Цилиндр", 
    "silindrik":"цилиндрик",               "Silindrik":"Цилиндрик", 
    "silindrsimon":"цилиндрсимон",         "Silindrsimon":"Цилиндрсимон", 
    "sirka":"сирка",                       "Sirka":"Сирка",
    "sirk":"цирк",                         "Sirk":"Цирк", 
    "sirkul":"циркул",                     "Sirkul":"Циркул", 
    "sisterna":"цистерна",                 "Sisterna":"Цистерна", 
    "sitrus":"цитрус",                     "Sitrus":"Цитрус", 
    
    "avtomobilda":"автомобилда",           "Avtomobilda":"Автомобилда",
    "avtomobilga":"автомобилга",           "Avtomobilga":"Автомобилга",
    "avtomobilni":"автомобилни",           "Avtomobilni":"Автомобилни",
    "avtomobilning":"автомобилнинг",       "Avtomobilning":"Автомобилнинг",
    "avtomobillar":"автомобиллар",         "Avtomobillar":"Автомобиллар",
    "avtomobillarda":"автомобилларда",     "Avtomobillarda":"Автомобилларда",
    "avtomobillarga":"автомобилларга",     "Avtomobillarga":"Автомобилларга",
    "avtomobillarni":"автомобилларни",     "Avtomobillarni":"Автомобилларни",
    "avtomobillarning":"автомобилларнинг", "Avtomobillarning":"Автомобилларнинг",
    "avtomobil":"автомобиль",              "Avtomobil":"Автомобиль",
    
    
    "kompyuter":"компьютер",               "Kompyuter":"Компьютер",
    "mashab":"масҳаб",                     "Mashab":"Масҳаб",
    "mo''tabar":"мўътабар",                "Mo''tabar":"Мўътабар",
    "mo''tadil":"мўътадил",                "Mo''tadil":"Мўътадил",
    "ishoq":"исҳоқ",                       "Ishoq":"Исҳоқ"
}
latin_birikmalar = {
    "ya":"я",   "Ya":"Я",    "YA":"Я",
    "yu":"ю",   "Yu":"Ю",    "YU":"Ю",
    "ch":"ч",   "Ch":"Ч",    "CH":"Ч",
    "sh":"ш",   "Sh":"Ш",    "SH":"Ш",
    "ye":"е",   "Ye":"Е",    "YE":"Е",
    "o'":"ў",   "O'":"Ў",
    "g'":"ғ",   "G'":"Ғ", 
    "yo'":"йў", "Yo'":"Йў",  "YO'":"ЙЎ",
    "yo":"ё",   "Yo":"Ё",    "YO":"Ё",
    "ts":"ц",   "Ts":"Ц",    "TS":"Ц"
}
latin_harflar = {
    "a":"а",  "A":"А",
    "b":"б",  "B":"Б",
    "d":"д",  "D":"Д",
    "e":"е",  "E":"Е",
    "f":"ф",  "F":"Ф",
    "g":"г",  "G":"Г",
    "h":"ҳ",  "H":"Ҳ",
    "i":"и",  "I":"И",
    "j":"ж",  "J":"Ж",
    "k":"к",  "K":"К",
    "l":"л",  "L":"Л",
    "m":"м",  "M":"М",
    "n":"н",  "N":"Н",
    "o":"о",  "O":"О",
    "p":"п",  "P":"П",
    "q":"қ",  "Q":"Қ",
    "r":"р",  "R":"Р",
    "s":"с",  "S":"С",
    "t":"т",  "T":"Т",
    "u":"у",  "U":"У",
    "v":"в",  "V":"В",
    "x":"х",  "X":"Х",
    "y":"й",  "Y":"Й",
    "z":"з",  "Z":"З",
    "'":"ъ"
}

# Kiril-lotin so'zlar uchun
cyril_suzlar = {
    "сентябр":"sentabr",                   "Сентябр":"Sentabr",          
    "октябр":"oktabr",                     "Октябр":"Oktabr",
    "бюджет":"budjet",                     "Июджет":"Budjet", 
    "цезий":"seziy",                       "Цезий":"Seziy", 
    "цейтнот":"seytnot",                   "Цейтнот":"Seytnot", 
    "целлофан":"sellofan",                 "Целлофан":"Sellofan", 
    "целлюлоза":"sellyuloza",              "Целлюлоза":"Sellyuloza", 
    "selsiy":"целсий",                     "Целсий":"Selsiy", 
    "цемент":"sement",                     "Цемент":"Sement", 
    "цензор":"senzor",                     "Цензор":"Senzor", 
    "цензура":"senzura",                   "Цензура":"Senzura", 
    "центер":"sentner",                    "Центер":"Sentner", 
    "цех":"sex",                           "Цех":"Sex", 
    "цетсе":"setse",                       "Цетсе":"Setse", 
    "цивилизация":"sivilizatsiya",         "Цивилизация":"Sivilizatsiya", 
    "цикл":"sikl",                         "Цикл":"Sikl", 
    "циликон":"siklon",                    "Циликон":"Siklon", 
    "цилиндр":"silindr",                   "Цилиндр":"Silindr", 
    "цилиндрик":"silindrik",               "Цилиндрик":"Silindrik", 
    "цилиндрсимон":"silindrsimon",         "Цилиндрсимон":"Silindrsimon", 
    "сирка":"sirka",                       "Сирка":"Sirka",
    "цирк":"sirk",                         "Цирк":"Sirk", 
    "циркул":"sirkul",                     "Циркул":"Sirkul", 
    "цистерна":"sisterna",                 "Цистерна":"Sisterna", 
    "цитрус":"sitrus",                     "Цитрус":"Sitrus", 
    "автомобил":"avtomobil",               "Автомобил":"Avtomobil",  
    "компьютер":"kompyuter",               "Компьютер":"Kompyuter",
    "масҳаб":"mashab",                     "Масҳаб":"Mashab",
    "мўътабар":"mo''tabar",                "Мўътабар":"Mo''tabar",
    "мўътадил":"mo''tadil",                "Мўътадил":"Mo''tadil",
    "исҳоқ":"ishoq",                       "Исҳоқ":"Ishoq"
}
cyril_birikmalar = {
    "я":"ya",   "Я":"Ya", 
    "ю":"yu",   "Ю":"Yu",
    "ч":"ch",   "Ч":"Ch",
    "ш":"sh",   "Ш":"Sh",
    "е":"ye",   "Е":"Ye",
    "ў":"o'",   "Ў":"O'",
    "ғ":"g'",   "Ғ":"G'",
    "йў":"yo'", "Йў":"Yo'",  
    "ё":"yo",   "Ё":"Yo",   
    "ц":"ts",   "Ц":"Ts"
}
cyril_harflar = {
    "а":"a",  "А":"A",
    "б":"b",  "Б":"B",
    "д":"d",  "Д":"D",
    "е":"e",  "Е":"E",
    "ф":"f",  "Ф":"F",
    "г":"g",  "Г":"G",
    "ҳ":"h",  "Ҳ":"H",
    "и":"i",  "И":"I",
    "ж":"j",  "Ж":"J",
    "к":"k",  "К":"K",
    "л":"l",  "Л":"L",
    "м":"m",  "М":"M",
    "н":"n",  "Н":"N",
    "о":"o",  "О":"O",
    "п":"p",  "П":"P",
    "қ":"q",  "Қ":"Q",
    "р":"r",  "Р":"R",
    "с":"s",  "С":"S",
    "т":"t",  "Т":"T",
    "у":"u",  "У":"U",
    "в":"v",  "В":"V",
    "х":"x",  "Х":"X",
    "й":"y",  "Й":"Y",
    "з":"z",  "З":"Z",
    "ъ":"'",  "ь":""
}
# Latin-kiril funksiyalar
def latin_suz(s, text):
    reg = re.compile("|".join(map(re.escape, s.keys())))
    return reg.sub(lambda s1: s[s1.group()], text)
def latin_harf(h, text):
    reg = re.compile("|".join(map(re.escape, h.keys())))
    return reg.sub(lambda h1: h[h1.group()], text)
def latin_birikma(b, text):
    reg = re.compile("|".join(map(re.escape, b.keys())))
    return reg.sub(lambda b1: b[b1.group()], text)

# Kiril-lotin funksiyalar
def cyril_suz(s, text):
    reg = re.compile("|".join(map(re.escape, s.keys())))
    return reg.sub(lambda s1: s[s1.group()], text)
def cyril_harf(h, text):
    reg = re.compile("|".join(map(re.escape, h.keys())))
    return reg.sub(lambda h1: h[h1.group()], text)
def cyril_birikma(b, text):
    reg = re.compile("|".join(map(re.escape, b.keys())))
    return reg.sub(lambda b1: b[b1.group()], text)

# natija chiqarish
# matnda lotin harflar bo'lsa kirilga o'tkazadi
l = re.findall(r"[a-zA-Z+]", matn)
k = re.findall(r"[а-яА-Я+]", matn)
if len(l)>len(k):
    matn1 = latin_suz(latin_suzlar, matn)
    matn2 = latin_birikma(latin_birikmalar,matn1)
    natija = latin_harf(latin_harflar,matn2)
    print(natija)
# Yoki lotinga o'tkazadi
else:
    matn1 = cyril_suz(cyril_suzlar, matn)
    matn2 = cyril_birikma(cyril_birikmalar,matn1)
    natija = cyril_harf(cyril_harflar,matn2)
    print(natija)
