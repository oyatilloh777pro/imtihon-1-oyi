# Imtihon qoidalari, aldamang, atrofga qaramang!
# Savollarga javob yozing va namuna kodini taqdim eting


# 1-savol: print() bu...

#Javob:
# Kod namunasi:
# import math
# from math import sqrt

# ism = " oyatilloh "
# familya = " qobiljonov "

# print(ism.upper() + familya.upper())

# print()


# 2-savol: input() bu...

#Javob: input bu foydalanuvchidan savol soraydi.
# Kod namunasi:
# abd = input(int("To'rtburchakning 1 tomonini kiriting: "))

# ulk = input(int("To'rtburchakning 2 tomonini kiriting: "))

# yui = input(int("To'rtburchakning yuzini kiriting: "))

# if abd == ulk > yui:
#  print("Javobi shu:")


# 3-savol: O'zgaruvchi nima?

#Javob:
# Kod namunasi:
# O'zgaruvchi - bu
# o’zida ma’lum bir toifadagi qiymatlarni saqlaydi. O’zgaruvchining nomi va qiymatlari bo’ladi.
#  O’zgaruvchining nomi orqali qiymat saqlanayotgan xotira qismiga murojaat qilinadi.
#  Programma ishlashi jarayonida o’zgaruvchining qiymatini o’zgartirish mumkin.
#  Har qanday o’zgaruvchini ishlatishdan oldin, uni e’lon qilish lozim.



# 4-savol: 4 ta maʼlumot turini sanab oʻting va misol keltiring:

#Javob:# int() , float() , str() , bool()
# Kod namunasi:
# ularga misol:
# inteygrga:
# soni=25
# floatga:
# narxi=20.45
# strga:
# name='Ahmad'
# boolinga:
# a=True
# b=False

# 5-savol: String formatlash nima va Pythonda ikkita formatlash usuliga misol keltiring:

#Javob:
#  upper() va lower()
# Kod namunasi:
#  str.upper()
#  str.lower()


# 6-savol: If, elif, else for nima va ular bilan misol ko'ring:

#Javob: ular agar degani.
# Kod namunasi:
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')


# 7-savol: Taqqoslash operatorlarini sanab bering va ularga misol keltiring:

#Javob:<,>,=
# Kod namunasi:
# trub = input(int("To'rtburchakning 1 tomonini kiriting: "))

# trub1 = input(int("To'rtburchakning 2 tomonini kiriting: "))

# trub2 = input(int("To'rtburchakning yuzini kiriting: "))

# if trub == trub1 > trub2:
#  print("Javobi shu:")

# trub = input("Son kiriting kiriting: ")

# if trub == 

# 8-savol: Mantiqiy operatorlar and, or, not bularning vazifasi nima va unga misol keltiring:

#Javob: AND va OR operatorlari ma'lumotlarni birdan ortiq shartlar bilan filtrlash uchun ishlatiladi.
#  NOT operatori berilgan shartni qanoatlantirmaydigan qatorlarni tanlab beradi.
# Kod namunasi:
# SELECT * FROM ishchilar WHERE oylik > 5000000 AND idora = 'Sotuvlar';


# 9-savol: Loop(sikl) nima va while sikli qanday ishlaydi:

#Javob: for (o’zgaruvchi ; munosabat amallari ; postfiks) { Operator yoki blok; (yoki sikl tanasi) }
# Kod namunasi:
# for i in range(10, 200):
    # print(i)
#     if str(i) == str(i)[::-10]:
#         print(i)
#         c +=1
# print()
# print(c)

# while ga misol:
#   for i in while(10 ,85)
 
 # print(i)
#     if str(i) == str(i)[::-10]:
#         print(i)
#         c +=1
# print()
# print(c)


# 10-savol: For va while o'rtasidagi farq nima va misol keltiring:

#Javob: For — sikl operatori bajariladigan qadamlar soni aniq bo’lganda ishlatiladi.
# While — sikl operatori bajariladigan qadamlar soni aniq bo’lmaganda va shartni avval tekshirish zarur bo’lganda ishlatiladi.
# Kod namunasi:
# for l in range(10, 87):
    # print(l)
#     if str(l) == str(l)[::-10]:
#         print(l)
#         c +=1
# print()
# print(c)

# while ga misol:
#   for l in while(10 ,54)
 
 # print(l)
#     if str(l) == str(i)[::-10]:
#         print(l)
#         c +=1
# print()
# print(c)


# 11-chi: Endi siz o'yin qilishingiz kerak: tosh, qog'oz, qaychi.
# Ya'ni, bu o'yinni ikkita o'yinchi o'ynashiga ishonch hosil qilishingiz kerak, omad tilaymiz!
# Kodi:

# import random

# def tosh_qaychi_qogoz():
#     print("Tosh, qaychi, qog'oz o'yiniga xush kelibsiz!")
    
#     variantlar = ["tosh", "qaychi", "qog'oz"]
    
#     user_tanlovi = input("Tanlovingizni kiriting (tosh, qaychi, qog'oz): ").lower()
    
#     komp_tanlovi = random.choice(variantlar)
    
#     print(f"Siz tanladingiz: {user_tanlovi}")
#     print(f"Kompyuter tanladi: {komp_tanlovi}")
    
#     if user_tanlovi == komp_tanlovi:
#         print("Durang!")
#     elif (user_tanlovi == "tosh" and komp_tanlovi == "qaychi") or \
#          (user_tanlovi == "qaychi" and komp_tanlovi == "qog'oz") or \
#          (user_tanlovi == "qog'oz" and komp_tanlovi == "tosh"):
#         print("Siz g'olib!")
#     else:
#         print("Kompyuter g'olib!")

# tosh_qaychi_qogoz()

