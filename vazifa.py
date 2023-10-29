# class Mehmon:
#     def __init__(self, ismi, yoshi, emaili):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.emaili = emaili
#     def kim(self):
#         print(f"Ismi: {self.ismi}")
#         print(f"Yoshi: {self.yoshi}")
#         print(f"Emaili: {self.emaili}")
# a = Mehmon("Xurshid", 16, "xakker007@gmail.com")
# a.kim()






# class Student:
#     def __init__(self, ismi, math, english, pysics):
#         self.ismi = ismi
#         self.math = math
#         self.english = english
#         self.pysics = pysics
#     def averade_grade(self):
#         print(int((self.math + self.english + self.pysics)/3))
#
# a = Student("Abduqodir", 5, 3, 4)
# a.averade_grade()






# class Student:
#     def __init__(self, ismi, math, english, pysics):
#         self.ismi = ismi
#         self.math = math
#         self.english = english
#         self.pysics = pysics
#     def averade_grade(self):
#         print(int((self.math + self.english + self.pysics)/3))
#
#     def student1(self):
#         return int((self.math + self.english + self.pysics)/3)
#
# a = Student("Abduqodir", 5, 3, 4)
# a.averade_grade()
# b = a.student1()
# print(b)






# class Meva:
#     def __init__(self, rang, narx, kech_pishar):
#         self.rang = rang
#         self.narx = narx
#         self.kech_pishar = kech_pishar
#     def about(self):
#         print("Rangi:", self.rang)
#         print("Narxi:", self.narx)
#         if self.kech_pishar==True:
#             print("Kech pishadimi: Ha")
#         else:
#             print("Kech pishadimi: Yo'q")
# a = Meva("qizil", 10000, False)
# a.about()






# class Meva:
#     def __init__(self, rang, narx, kech_pishar):
#         self.rang = rang
#         self.narx = narx
#         self.kech_pishar = kech_pishar
#
#     def about(self):
#         print("Rangi:", self.rang)
#         print("Narxi:", self.narx)
#         if self.kech_pishar==True:
#             print("Kech pishadimi: Ha")
#         else:
#             print("Kech pishadimi: Yo'q")
#
# anor = Meva("qizil", 5000, True)
# anor.about()





# class Matem:
#     def __init__(self, son1, son2):
#         self.son1 = son1
#         self.son2 = son2
#     def ayrish(self):
#         print("Ayirma:", self.son1-self.son2)
#     def kopaytirish(self):
#         print("Ko'paytma:", self.son1*self.son2)
#     def qoldiqli_bolish(self):
#         print(f"Qoldiqli bo'lish: {self.son1} % {self.son2}")
#     def qoldiq(self):
#         b = self.son1%self.son2
#         print("Qoldiq:",b)
#     def daraja(self):
#         print(f"{self.son1} ning {self.son2} ga oshirilgan darajasi:", self.son1**self.son2)
#
# a = Matem(52, 3)
# a.ayrish()
# a.kopaytirish()
# a.qoldiqli_bolish()
# a.qoldiq()
# a.daraja()





# class Mashina:
#     def __init__(self, brend, narx, rang, yil, tezlik, maks_tezlik, yoqilgi):
#         self.brend = brend
#         self.narx = narx
#         self.rang = rang
#         self.yil = yil
#         self.tezlik = tezlik
#         self.maks_tezlik = maks_tezlik
#         self.yoqilgi = yoqilgi
#
#     def start(self):
#         if self.tezlik>40 and self.tezlik<140:
#             print("Normal tezlikda ketayapsiz!")
#
#         if self.yoqilgi<20:
#             print("Yoqilg'i kam qoldi. Uni to'ldiring")
#         elif self.yoqilgi<=20:
#             print("Yoqilg'ingiz yetarli!")
#     def stop(self):
#         if self.tezlik==0:
#             print("Mashina harakatda emas. Mashina harakatlanishi uchun o't oldiring!")
#
#     def tezlanish(self):
#         if self.tezlik>150:
#             print(f"Avtolobilni tezligi juda yuqori. uni kamaytiring. {self.brend} rusumli mashinada Uzb ning yamali yo'llarida {self.tezlik} km/s bilan avtoxalokatga uchrashingiz mumkin!")
#             print(f"Avtomobilingizning eng yuqori tezligi: {self.maks_tezlik} km/s", f"Sizda unga yetib borish uchun yana {self.maks_tezlik - self.tezlik} km/s qoldi")
#     def sekinlashish(self):
#         if self.tezlik>0 and self.tezlik<40:
#             print("Mashinangiz juda sekin xarakat qilayapti. Bu bir xil yo'nalishdagi mashinalarga noqulaylik keltirishi mumkin!")
#
#
# a = Mashina("BMW", 250000, "qop-qora", 2023, 220, 320, 10)
# a.start()
# a.stop()
# a.tezlanish()
# a.sekinlashish()





# class Shaxs:
#     def __init__(self):
#
# class Mijoz:
#     def __init__(self):
#
# class Ishchi:
#     def __init__(self):
#
# class Menejer:
#     def __init__(self):
#
# class Dasturchi:
#     def __init__(self):



