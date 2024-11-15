#Problem 1 of Number Data Type
# d = float(input('sonni kiriting:'))
# if d == 0:
#     print(0)
# else: 
#     a = d*100
#     import math
#     b = ((math.sqrt(a**2)) + 0.5)//1
#     c = a * b 
#     c=c* ((math.sqrt(a**2))**(-1))
#     x = c / 100
#     print(x)
#-----------------------------------------------------
#Problem 2 of Number Data Type
# print("3 ta son kiriting:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# print(max(a,b,c))
# print(min(a,b,c))
#------------------------------------------------------
#Problem 3 of Number Data Type
# print("Masofani km birligida kiriting")
# a = float(input()) 
# b = a*1000
# c = b*100
# print(b , "m(meter)")
# print(c , 'sm(santimer)')
# -------------------------------------------------------
#Problem 4 of Number Data Type
# a = float(input("a = "))
# b = float(input("b = "))
# x , y = divmod(a , b)
# print(x , 'bo\'linma' ,y ,'qoldiq')
# -------------------------------------------------------
#Problem 5 of Number Data Type
# print("temperaturani gradus selsiyda kiriting")
# a = float(input("a = "))
# print("temperaturaning Farengeytda qiymati", 9*a/5 + 32 ,"ga teng")
# -------------------------------------------------------
#Problem 6 of Number Data Type
# a = int(input("a = ")) # int kiritganimni sababi oxirgi raqam faqat butun sonlarda bo'ladi
# print(a%10)
# -------------------------------------------------------
#Problem 7 of Number Data Type
# a = int(input("Sonni kiriting:")) 
# results = ['juft', 'toq']
# result = results[a % 2]
# print(f"{a} - {result} son") #buni chatgptidan soragandim imkoni bormi if else siz deb ln kodini ciqarib berdi ko'rib qoldim
# -------------------------------------------------------
#Problem 8 of Number Data Type
# a = float(input('a = '))
# b = float(input('b = '))
# x = a
# a = b
# b = x
# print('a = ', a)
# print('b = ', x)
# -------------------------------------------------------
#Problem 2 of String Data Type
# a = str(input("Matnni kiriting:"))
# b1 = a.replace('a','') 
# b2 = b1.replace('A','') 
# b3 = b2.replace('e','') 
# b4 = b3.replace('E','') 
# b5 = b4.replace('o','') 
# b6 = b5.replace('O','') 
# b7 = b6.replace('U','') 
# b8 = b7.replace('u','') 
# b9 = b8.replace('o\'','') 
# b10 = b9.replace('O\'','') 
# b11 = b10.replace('i','') 
# b12 = b11.replace('I','') 
# print(b12)
# -------------------------------------------------------
#Problem 3 of String Data Type
# a = str(input("Matnni kiriting:"))
# print(a[-1::-1])
# -------------------------------------------------------
#Problem 4 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = a.replace(' ', '_' )
# print(b)
# -------------------------------------------------------
#Problem 5 of String Data Type
# a = str(input("Matnni(so'zni) kiriting:"))
# b = a[-1::-1]
# c = int(bool(a == b))
# results = ['palindrom emas ', 'palindrom']
# result = results[c % 2]
# print(f'\"{a}\" {result}')
# -------------------------------------------------------
#Problem 6 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = a.replace('a', 'o')
# print(b)
# -------------------------------------------------------
#Problem 7 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = a.replace('@', '')

# -------------------------------------------------------
#Problem 9 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = a[1:-1:1]
# print(b)
# -------------------------------------------------------
#Problem 10 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = str(input("izlayotgan so'zingizni  kiriting:"))
# c = int(bool(b in a))
# results = ['matn ichida yo\'q ', 'matn ichida bor']
# result = results[c % 2]
# print(f'{result}')
# -------------------------------------------------------
#Problem 12 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = a[-3::1]
# print(b)
# -------------------------------------------------------
#Problem 14 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = a.replace(' ','\n' )
# print(b)
# -------------------------------------------------------
#Problem 15 of String Data Type
# a = str(input("Matnni kiriting:"))
# print(a[0::2])
# -------------------------------------------------------
#Problem 16 of String Data Type
# a = str(input("Matnni kiriting:"))
# print("Title:",a )
# -------------------------------------------------------
#Problem 17 of String Data Type
# a = str(input("Matnni kiriting:"))
# print(a[-1::-1])
# -------------------------------------------------------
#Problem 18 of String Data Type
# a = str(input("Matnni kiriting:"))
# b = str(input("Matnni kiriting:"))
# c = len(a) - len(b)
# print(int(pow(c**2, 0.5)))
# -------------------------------------------------------
#Problem 1 of Boolean Data Type
# a = str(input("Username kiriting:"))
# b = str(input("parolni kiriting:"))
# c = a.replace(' ', '\t')
# d = b.replace(' ', '\t')
# k = bool('\t' in c)
# k1 = bool('\t' in d)
# x = int(bool(int(bool('\t' in a)) * int(bool('\t' in b))))
# results = ['qabul qilindi', 'kiritishda xatolik bor']
# result = results[x % 2]
# print(f'{result}')
# -------------------------------------------------------
#Problem 2 of Boolean Data Type
# a = str(input("a = "))
# b = str(input("b = "))
# print(bool(a==b))
# -------------------------------------------------------
#Problem 3 of Boolean Data Type
# a = str(input("a = "))
# if a > 0 and a%2==0:
#     print('positive and even number') 
# else : 
#     print('it is not number that claimed')
# -------------------------------------------------------
#Problem 3 of Boolean Data Type
# a = [1,2]
# b = [3,4]
# print(a + b)
# for i in range(10):
#     #i=0
#     for j in range(5):
#     #j=0
#         print(f"{i}{j}")
# a = 4
# while a < 10:
#     a += 1
#     print(a, '10 dan kichik')
# else:
#     print('Loop finished')

print("Outside of the loop")
n = int(input())
ans = 'tub son'
for i in range(2,n):
    if n%i == 0:
        ans = 'tub son emas'
        break
print(ans)


     












