
#RAJABBOYEV INOYAT ISE-51U
#1-masla
from colorama import Fore, Back, Style, init
init(autoreset=True)

import math
#1 - masala
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
#
#2-masala
# Foydalanuvchidan uch xonali sonni olish
uchxonali_son = int(input("Uch xonali son kiriting: "))

# Yuzlik va o'nlik raqamlarni almashtirish
birlik = uchxonali_son % 10
onlik = (uchxonali_son // 10) % 10
yuzlik = uchxonali_son // 100

# Almashtirilgan raqamni chiqarish
almashgan_raqam = birlik * 100 + onlik * 10 + yuzlik

# Natijani chiqarish
print(f"Kiritilgan son: {uchxonali_son}")
print(f"Almashtirilgan son: {almashgan_raqam}")









#2-misol

init(autoreset=False)

