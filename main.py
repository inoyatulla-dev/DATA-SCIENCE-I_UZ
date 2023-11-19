
#RAJABBOYEV INOYAT ISE-51U
#1-masla
from colorama import Fore, Back, Style, init
init(autoreset=True)

import math
#1 - masala----------------
# Foydalanuvchidan doiraning maydonini olish
# S = float(input(Fore.GREEN +"Doiraning maydonini kiriting: "))
#
# # Pi ning qiymati
# pi = 3.14
#
# # Doiraning radiusini hisoblash
# radius = math.sqrt(S / pi)
#
# # Doiraning diametri
# diameter = radius * 2
#
# # Doiraning uzunligi
# length = 2 * math.pi * radius
#
# # Natijalarni chiqarish
# print(Fore.YELLOW + f"Doiraning Diametri (D):{diameter}")
# print(Fore.YELLOW+f"Doiraning Uzunligi (L): {length}")
#----------------------------------------------------------------



#2-masala
# Foydalanuvchidan uch xonali sonni olish
# uchxonali_son = int(input("Uch xonali son kiriting: "))
#
# # Yuzlik va o'nlik raqamlarni almashtirish
# birlik = uchxonali_son % 10
# onlik = (uchxonali_son // 10) % 10
# yuzlik = uchxonali_son // 100
#
# # Almashtirilgan raqamni chiqarish
# almashgan_raqam = birlik * 100 + onlik * 10 + yuzlik
#
# # Natijani chiqarish
# print(f"Kiritilgan son: {uchxonali_son}")
# print(f"Almashtirilgan son: {almashgan_raqam}")
#

#3-misol----------------------------------------------------
#
# # Foydalanuvchidan uchta raqam kiritish
# raqam1 = int(input("Birinchi raqamni kiriting: "))
# raqam2 = int(input("Ikkinchi raqamni kiriting: "))
# raqam3 = int(input("Uchinchi raqamni kiriting: "))
#
# # If shart operatori orqali o'rtadagi raqamni topish
# if raqam1 <= raqam2 <= raqam3 or raqam3 <= raqam2 <= raqam1:
#     orta_raqam = raqam2
# elif raqam2 <= raqam1 <= raqam3 or raqam3 <= raqam1 <= raqam2:
#     orta_raqam = raqam1
# else:
#     orta_raqam = raqam3
#
# # Natijani chiqarish
# print(f"Uch raqamning orasidagi o'rtadagi raqam: {orta_raqam}")
# 4-masala
# 1 kg olma narxi
# narx_1kg = float(input("1 kg olma narxini kiriting: "))
# 
# # For tsikli orqali 1 dan 10 gacha bo'lgan olmalar uchun narxni hisoblash
# for kg in range(1, 11):
#     total_narx = kg * narx_1kg
#     print(Fore.YELLOW +f"{kg} kg olma narxi: {total_narx} so'm")

# 4-masala-------------------------------------------------------------
def kvadratni_hisobla(son):
    natija = son ** 2
    return natija

# Foydalanuvchidan son olish
A = int(input("Istalgan sonni kiriting: "))

# Funktsiyani chaqirib, natijani hisoblash
B = kvadratni_hisobla(A)

# Natijani chiqarish
print(f"{A} ning kvadrati {B} ga teng.")

