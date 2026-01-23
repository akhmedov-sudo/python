# # def qoshamiz(*a):

# #     return a

# # print(qoshamiz(5,45,474,12))

# # def info(**salom):
# #     return salom

# # print(info(ism="ali", yosh=25))



# def qoshamiz(*a):
#     yigindi = 0
#     for s in a:
#         yigindi += s
#     return yigindi
# print(qoshamiz(5,45,474,12))



# def info(**salom):
#     for k, v in salom.items():
#         print(k, ":", v)

# info(ism="ali", yosh=25, tugilgan_yil=2004)



# def kopaytirma(**sonlar):
#     kopaytma = 1
#     for v in sonlar.values():
#         kopaytma *= v
#     return kopaytma
# print(kopaytirma(a=5, b=10, c=4))

# def talabalar(**malumot):
#     for k, v in malumot.items():
#         print(f"{k} : {v}")

# talabalar(ism="ali", yosh=25, kurs=3, fakultet="matematika")
# talabalar(ism="vali", yosh=24, kurs=3, fakultet="fizika")