import re
matn = input("Matn: ")

latin_suzlar = {}
with open("latin_suz.txt") as suz:
    for line in suz:
       (key, val) = line.split(",")
       x = len(val)-1
       val = val[0:x]
       latin_suzlar[key] = val
       
latin_birikmalar = {}
with open("latin_birikma.txt") as birikma:
    for line in birikma:
       (key, val) = line.split(",")
       x = len(val)-1
       val = val[0:x]
       latin_birikmalar[key] = val
latin_harflar = {}
with open("latin_harf.txt") as harf:
    for line in harf:
       (key, val) = line.split(",")
       x = len(val)-1
       val = val[0:x]
       latin_harflar[key] = val

cyril_suzlar = {}
with open("cyril_suz.txt") as suz:
    for line in suz:
       (key, val) = line.split(",")
       x = len(val)-1
       val = val[0:x]
       cyril_suzlar[key] = val
cyril_birikmalar = {}
with open("cyril_birikma.txt") as birikma:
    for line in birikma:
       (key, val) = line.split(",")
       x = len(val)-1
       val = val[0:x]
       cyril_birikmalar[key] = val
cyril_harflar = {}
with open("cyril_harf.txt") as harf:
    for line in harf:
       (key, val) = line.split(",")
       x = len(val)-1
       val = val[0:x]
       cyril_harflar[key] = val
       
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
