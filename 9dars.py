# telefon = input("Bitta telefon nomini yozing:")
# talaba_0 = {
#     'ism':'alijon',
#     'familya':'valijonov',
#     "model":"Samsung A50"
# }
# # print(talaba_0.items())
# print(talaba_0.keys())
# print(talaba_0.values())
# if telefon in talaba_0['model']:
#     print(f"Bizda {telefon} bor")
# if telefon not in talaba_0:
#     print(f"Bizda {telefon} yoq")
# avtomobile = input("Avtomobilingizni kiriting->>> ")
# moshinalar = {
#     "bmw":15000000,
#     "mers":140000000,
#     "toyota":1000000,
#     "Laceti":45000,
#     "byd":40000,
# }

# # if avtomobile not in moshinalar.keys():
# #     print(f"Bizda {avtomobile} yoq")
# # else:
# #     print(f"Bizda {avtomobile} bor")

# for k in sorted(moshinalar.keys()):
#     print(k)
# model = moshinalar.items()
# model = moshinalar.items()

# for k,q in sorted(model):
#     print(f"Avtomobilarmiz {k}ning narhi {q} $ ga teng")



# lugat = {
#     "boolen":"Mantiqiy qiymat",
#     "Float":"Onlik son",
#     "for":"Biror amalni qayta bajarishi",
#     "If":"Shartlar tekshirish",
#     "Interger":"Butun son"
# }
# model = lugat.items()
# for k,q in sorted(model):
#     print(f"{k} - {q}")

davlatlar = {
    "Aqsh":"Vashington",
    "Italiya":"rim",
    "Russia":"Moskva",
    "Ozbekiston":"Toshkent",
    "Qozogiston":"Bishkek"
}
model = davlatlar.keys()
print("Dunyo davlatlari:\n")
for k in sorted(model):

    print(f"{k}\n")
model2 = davlatlar.values()
print("Dunyo poytaxtlari:\n")
for q in sorted(model):
    print(f"{q}")