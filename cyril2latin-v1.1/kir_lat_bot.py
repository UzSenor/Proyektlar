import telebot
import re
bot = telebot.TeleBot('5526836670:AAG2885QNQTyMSjIQrv4RavyMKgX9_eQqJw')


@bot.message_handler(commands=['start'])
def start(message):
    name = str(message.from_user.first_name)
    bot.send_message(message.from_user.id ,'Assalomu aleykum ' + name +'!\n (kiril --> lotin) yoki (lotin --> kiril) botiga xush kelibsiz!')

@bot.message_handler(content_types=['text'])
def send(message):
    text = message.text

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
    l = re.findall(r"[a-zA-Z+]", text)
    k = re.findall(r"[а-яА-Я+]", text)
    if len(l)>len(k):
        text1 = latin_suz(latin_suzlar, text)
        text2 = latin_birikma(latin_birikmalar,text1)
        natija = latin_harf(latin_harflar,text2)
        bot.send_message(message.from_user.id , natija)
    # Yoki lotinga o'tkazadi
    else:
        text1 = cyril_suz(cyril_suzlar, text)
        text2 = cyril_birikma(cyril_birikmalar,text1)
        natija = cyril_harf(cyril_harflar,text2)
        bot.send_message(message.from_user.id , natija)
    
bot.polling(none_stop= True)
