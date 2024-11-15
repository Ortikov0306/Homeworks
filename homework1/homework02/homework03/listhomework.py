#1.Count Occurrences: Given a list and an element, find how many times the element appears in the list.
# a = eval(input())
# b = eval(input())
# m = 0
# c = len(a)
# for i in range (0,c):
#     k = int(bool(b == a[i]))
#     m += k 
# print(m)

#2.Sum of Elements: Given a list of numbers, calculate the total of all the elements.
# a = eval(input())
# total = sum(a)
# print('total :', total)

#3.Max Element: From a given list, determine the largest element.
# a = eval(input())
# print(max(a))

# 4.Min Element: From a given list, determine the smallest element.
# a = eval(input())
# print(min(a))

# 5.Check Element: Given a list and an element, check if the element is present in the list.
# a = eval(input("Enter your list:"))
# b = eval(input("ENter your element:"))
# if b in a:
#     print("element mavjud")
# else:
#     print('mavjud emas')    

# 6.First Element: Access the first element of a list, considering what to return if the list is empty.
# 7.Last Element: Access the last element of a list, considering what to return if the list is empty.
# a = eval(input("Enter your list:"))
# if len(a) == 0:
#     print('listingizda element mavjud emas')
# else:
#     print('birinchi elementi:',a[0], 'so\'ngi elementi:', a[-1] )

# 8.Slice List: Create a new list that contains only the first three elements of the original list.
# 9.Reverse List: Create a new list that contains the elements of the original list in reverse order.
# a = eval(input("Enter your list:"))
# b = [a[0],a[1],a[2]]
# c = a[::-1]
# print(b)
# print(c)

# 10.Create a new list that contains the elements of the original list in sorted order.
# a = eval(input("Enter your list:"))
# print(sorted(a))

# 11.Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.
# a = eval(input())
# c = set(a) 
# d = list(c)
# print(d)

# 12.Insert Element: Given a list and an element, insert the element at a specified index.
# a = eval(input())
# b = input()
# c = int(input())
# a[c] = b
# print(a)

# 13.Index of Element: Given a list and an element, find the index of the first occurrence of the element.
# a = eval(input())
# b = eval(input())
# print(a.index(b))

# 14.Check for Empty List: Determine if a list is empty and return a boolean.
# a = eval(input())
# if len(a) == 0:
#     print(True)
# else:
#     print(False)

# 15 and 16.Count Even and Odd Numbers: Given a list of integers, count how many of them are even and odd.
# a = [1,2,3,4,5,6,7,11,12,13,14,10,10,12]
# m = 0
# for i in range(0,len(a)):
#     if a[i]%2 == 1:
#         m+=1
#     else:
#         n = len(a) - 1 - m

# print(m, "ta toq son bor")
# print(n , "ta juft son bor")

# 17.Concatenate Lists: Given two lists, create a new list that combines both lists.
# a = [1,2,3,4,44,33,3,5,"salom","salom", True,None]
# b = [55555555555555555,"salom"]
# print(a + b)

# 18.Find Sublist: Given a list and a sublist, check if the sublist exists within the list.
# a = [[1,3,44],44,33,3,5,"salom","salom", True,None]
# b = [1,3,44]
# c = ["bilmadim",True]
# if int(b in a) == 0:
#     print(" b subto'plam a to'plam ichiga kirmaydi")  
# else:
#     print(" b subto'plam a to'plam ichida mavjud")

# if int(c in a) == 0:
#     print("c subto'plam a to'plam ichiga kirmaydi") 
# else:
#     print("c subto'plam a to'plam ichida mavjud")

# 19.Replace Element: Given a list, replace the first occurrence of a specified element with another element.
# a = [1,3,44,44,33,3,5,"salom","salom", True,None]
# a[a.index(44)] = 33
# print(a)

# 20 and 21.Find Second Largest: From a given list, find the second largest and smallest element.
# a = [1,3,44,33,3,5,877,44,1,1,877,0,0]
# a = set(a)
# a = list(a)
# a[a.index(max(a))] = min(a)
# print(max(a))   
# a[a.index(min(a))] = max(a)
# print(min(a))

# 22 and 23.Filter Even and odd Numbers: Given a list of integers, create a new list that contains only the even numbers and odd numbers.
# a = [1,2,3,4,5,6,7,11,12,13,14,10,10,12]
# m = []
# n = []
# for i in range(0,len(a)):
#     if a[i]%2 == 1:
#         m+=[a[i]]
#     else:
#         n+=[a[i]]
# print(m)
# print(n)

# 24.List Length: Determine the number of elements in the list.
# a = [1,2,3,4,5,6,7,11,12,13,14,10,10,12]
# print(len(a))

# 25.Create a Copy: Create a new list that is a copy of the original list.
# a = [1,2,3,4,5,6,7,11,12,13,14,10,10,12]
# from copy import copy
# b = a.copy()
# print(b)

# 26.Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
# a = [1,2,3,4,5,6,7,11,12,13,14,10,10,12]
# if len(a)%2 == 0:
#     print(a[int((len(a))/2)])
#     print(a[int((len(a))/2 +1)])
# else:
#     x = int((len(a)+1)/2)
#     print(a[x])

# 27.Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.
# 28.Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.
# a = [1,2,3,44,5,6,7,11,12,13,14,10,10,12]
# starting_index = int(input())
# ending_index = int(input())
# print(max(a[starting_index:ending_index]))
# print(min(a[starting_index:ending_index]))

# 29.Remove Element by Index: Given a list and an index, remove the element at that index if it exists.
# a = [1,2,3,44,5,6,7,11,12,13,14,10,10,12]
# b_index = int(input())
# b = a[b_index]
# print(b)
# a.remove(b)
# print(a)

# 30.Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.
# a = [1,2,3,44,5,6,7,11,12,13,14,10,10,12]
# b = a.sort()
# if a == b:
#     print(True)
# else:
#     print(False)

# 31.Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.
# a = [1,2,3,44,5,6,7,11,12,13,14,10,10,12]
# m = []
# n = int(input())
# for i in range(1,n+1):
#     m +=a

# print(m)

# 32.Merge and Sort: Given two lists, create a new sorted list that merges both lists.
# a = [1,2,3,44,5,6,7,11,12,13,14,10,10,12]
# b = [1,3,44,44,33,3,5,True]
# c = a+b
# print(sorted(c))

# 33.Find All Indices: Given a list and an element, find all the indices of that element in the list.
# a = [1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# b = int(input('Enter element:'))
# print(a[a.index(b)])
# for i in range(len(a)):
#     if a[a.index(b)] == a[i]:
#         print(i)

# 34.Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
# a = [1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# a = a[-1::-1]
# print(a)

# 35.Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).
# a = [1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# x = int(input())
# y = int(input())
# b = a[x:y+1:1]
# print(b)

# 36.Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.
# 37.Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.
# a = [1,2,-3,44,-5,6,7,-10,-11,12,13,14,10,10,12]
# m = 0
# n = 0
# for i in range(len(a)):
#     if a[i] > 0:
#         m += a[i]
#     elif a[i] < 0:
#         n+=a[i]

# print(m)
# print(n)

# 38.Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
# a = [1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# a2 = a[-1::-1]
# c = bool(a == a2 )
# if c==1:
#     print("palindrom")
# else:
#     print("palindrom emas")

# 39.Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
# a = [1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# m = []
# x = int(input())
# t = len(a)%x
# if len(a)%x == 0:
#     for i in range(len(a)):
#         if (i+1)%x == 0:
#             m+=[a[i+1-x:i+1]]
# else:
#     for i in range(len(a)):
#         if (i+1)%x == 0:
#             m+=[a[i+1-x:i+1]]
#     m +=[a[len(a)-t:]]

# print(m)

#40.Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.
# a = [0,1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# n = []
# m = []
# for i in range(len(a)):
#     if a[i] in n:
#         m+=[a[i]]
#     else:
#         n+=[a[i]]
# print(n)





