# def salomlash(ism):
#     print(f"{ism.title()} Qalesan !")


# # salomlash("adhamjon")
# # salomlash("sulton")


# def yoshi_nechi(ism, tyil):
#     print(f"Salom {ism.title()}, Sen {2026-tyil} yoshdasan")

# yoshi_nechi("asad", 2007)

# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# oyil = int(input("Vafot etgan yilini kiriting:"))

# def nechi_yosh(tyil, oyil):
#     print(f"Sen {oyil - tyil} yoshdasan")
# nechi_yosh(tyil, oyil)

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# def aniq_katta(a, b):
#     if a>b:
#         print(f"{a} katta son")
#     else:
#         print(f"{b} katta son")

# aniq_katta(a, b)

# def nechi_yosh(tyil, ism="ali"):
#     print(f"Salom {ism.title()}, Siz {2026 - tyil} yoshda")

# nechi_yosh(2004)
# ism = input("Ismingiz nima? ")
# tyil = int(input("Tug'ilgan yilingiz nechchi? "))

# def info(ism, tyil):
#     print(f"Ismingiz {ism.title()}, Siz {2026 - tyil} yoshdasiz")
# info(ism, tyil)

# son = int(input("Istalgan son kiriting: "))
# def kvadrat_kub(kvadrat, kub):
#     print(f"{son} ning kvadrati {kvadrat} ga teng")
#     print(f"{son} ning kubi {kub} ga teng")
# kvadrat_kub(son**2, son**3)

# son = int(input("Istalgan son kiriting: "))
# def juft_toq(son):
#     if son%2==0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")

# juft_toq(son)


# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))

# def teng_yoki_katta(son1, son2):
#     if son1==son2:
#         print(f"{son1} va {son2} sonlari teng")
#     elif son1>son2:
#         print(f"{son1} soni katta")
#     else:
#         print(f"{son2} soni katta")

# teng_yoki_katta(son1, son2)

# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# def x_y(x, y):
#     print(f"{x} ning {y} darajasi {x**y} ga teng")

# x_y(x,y)


# x = int(input("Birinchi sonni kiriting: "))

# def x_y(x, y=2):
#     print(f"{x} ning {y} darajasi {x**y} ga teng")

# x_y(x)

# son = int(input("Istalgan son kiriting: "))

# def bolinish_alomatlari(son):
#     for n in range(2,11):
#         if son%n==0:
#             print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# bolinish_alomatlari(son)