
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#           f"{vyil-tyil} yil umr ko'rgan.")


# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)

# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)


# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")


# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")

# ----------------------------------------------------------------------------------


# avto0 = {
#     "model":"Onix",
#     "narhi":"15000$",
#     "rangi":"Qora",
#     "davlat":"Uzbekistan"
# }

# avto1 = {
#     "model":"Bmw m3 gtr",
#     "narhi":"3000010$",
#     "rangi":"Kok",
#     "davlat":"Germaniya"
# }

# avto2 = {
#     "model":"Tesla",
#     "narhi":"1500000$",
#     "rangi":"Pushti",
#     "davlat":"Aqsh",
# }
# avtolar = [avto0,avto1,avto2]
# for avto in avtolar:
#     print(f"Nomi {avto["model"]} va Narhi {avto["narhi"]} va Rangi {avto["rangi"]} va Davlati {avto["davlat"]}")

# phones = {
#     "iphone":['iphone 11 max','iphone 8 plus',"iphone air"],
#     "SAMSUNG":["samsung a17","samsung s21","samsung s25 ultra"],
#     "REDMI":["redmi note 10","redmi 9a","redmi 7a"],
# }

# for k,q in phones.items():
#     print(f"{k} Rusumlari")
#     for ql in q:
#         print(f"{ql} ")


# komputers = {
#     "macbook":{
#         "model":"macbook air",
#         "rangi":"qora",
#         "narhi":"800$",
#         "xotira":"1TB"
#     },
#     "asus":{
#         "model":"asus rog",
#         "rangi":"blue",
#         "narhi":"420$",
#         "xotira":"450GB"
#     },
#     "victus":{
#         "model":"victus pro",
#         "rangi":"pink",
#         "narhi":"120$",
#         "xotira":"500GB"
#     },
# }

# for model,inf in komputers.items():
#     print(f"Bizning dokonimizda {model} {inf["model"]} bor. Va xotirasi {inf["xotira"]}. Narhi esa {inf["narhi"]}")

# -----------------------------------------------------------------

# buxoriy01 = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tugulgan':810,
#            'vafot':870,
#            'joy':'Buxoro'
#            }

# qodiriy02 = {'ism':'Abdulla Qodiriy',
#            'tugulgan':1894,
#            'vafot':1938,
#            'joy':'Toshkent'
#            }

# vohidov03 = {'ism':'Erkin Vohidov',
#            'tugulgan':1936,
#            'vafot':2016,
#            'joy':"Farg'ona"
#            }

# navoiy04 = {'ism':'Alisher Navoiy',
#            'tugulgan':1441,
#            'vafot':1501,
#            'joy':"Xirot"
#            }

# shaxslar = [buxoriy01, qodiriy02, vohidov03, navoiy04]

# for adiblar in shaxslar:
#     ism = adiblar['ism']
#     tugulgan = adiblar['tugulgan']
#     vafot = adiblar['vafot']
#     joy = adiblar['joy']
#     print(f"{ism} {tugulgan} yilda {joy}da tugulgan topgan, "
#           f"{vafot-tugulgan} shuncha yil ko'rgan.")
# ---------------------------------------------------
# buxoriy01 = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tugulgan':810,
#            'vafot':870,
#            'joy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# paveldurov02 = {'ism':'Pavel Durov',
#            'tugulgan':1990,
#            'joy':'Aqsh',
#            'asarlar':["Telegram","Starts",'NFT']
#            }

# jahongirotajonov03 = {'ism':'Jahongir Otajonov',
#            'tugulgan':1989,
#            'joy':"Toshkent",
#            "asarlar":["happy birthday","qadi sarvar"]
#            }


# shaxslar = [buxoriy01, paveldurov02, jahongirotajonov03]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari yoki qoshiqlari yoki loyihasi: ")
#     for asar in asarlar:
#         print(asar)
# ---------------------------------------------------------
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':453212,
#                    'aholi':"36mln",
#                    'pul birligi':"som"
#                    },
#     "yaponiya":{'poytaxt':"tokio",
#                    'maydon':1600546,
#                    'aholi':"145mln",
#                    'pul birligi':"yen"
#                    },
#     "argentina":{'poytaxt':"bueno vayst",
#                    'maydon':"9631418mln",
#                    'aholi':3270004000,
#                    'pul birligi':"yevro"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':257000000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='argentina':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']} shunaqa boladi")

# ------------------------------------------------------------------------

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':453212,
#                    'aholi':"36mln",
#                    'pul birligi':"som"
#                    },
#     "yaponiya":{'poytaxt':"tokio",
#                    'maydon':1600546,
#                    'aholi':"145mln",
#                    'pul birligi':"yen"
#                    },
#     "argentina":{'poytaxt':"bueno vayst",
#                    'maydon':"9631418mln",
#                    'aholi':3270004000,
#                    'pul birligi':"yevro"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':257000000,
#                    'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']} shuncha"
#           f"\nPul birligi: {info['pul birligi']} shunaqa")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas iltimos boshqasini yozing")

# kinolar = {
#     'abror':['ujastik','rembo','marvel'],
#     'hasanbek':['shaytanat','airman','ironman'],
#     'asadbek':['seshanbadan shanbagacha','taqdirlar','bomba']
# }

# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)