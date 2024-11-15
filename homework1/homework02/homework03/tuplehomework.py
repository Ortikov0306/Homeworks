#Tuple tasks
#1.Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
# a = (1,2,3,44,5,6,7,10,11,12,13,14,10,10,12,True,'salom')
# c = input()
# if a.count(c) == 0:
#     print(a.count(int(c)))
# else:
#     print(a.count(c))

# 2 and 3.Max and Min Element: From a given tuple, determine the largest and smallest element.
# a = (1,2,3,1,1,1,1)
# print(max(a))
#print(min(a))

# 4.Check Element: Given a tuple and an element, check if the element is present in the tuple.
# Y = (1,2,3,1,1,1,1,'m')
# x = input()
# if int(x in Y ) == 1:
#     print('mavjud')
# elif int(x in Y ) == 0:
    
#     if int(int(x) in Y) == 1:
#         print('Mavjud ')
#     else:
#         print('mavjud emas')
# 5 and 6.First and Last Element: Access the first and Last element of a tuple, considering what to return if the tuple is empty.
# a = (1,2,3,1,1,1,1,'m')
# if len(a) == 0:
#     print('listingizda element mavjud emas')
# else:
#     print('birinchi elementi:',a[0], "\nso'ngi elementi:", a[-1] )

# 7.Tuple Length: Determine the number of elements in the tuple.
# a = (1,2,3,1,1,1,1,'m')
# print(len(a))
# 8.Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
# a = (1,2,3,1,1,1,1,'m')
# b = (a[0],a[1],a[2])
# print(b)

# 9.Concatenate Tuples: Given two tuples, create a new tuple that combines both.
# a = (1,2,3,4,44,33,3,5,"salom","salom", True,None)
# b = (55555555555555555,"salom")
# print(a + b)

# 10.Check if Tuple is Empty: Determine if a tuple has any elements.
# a = (1,2,3,4,44,33,3,5,"salom","salom", True,None)
# if len(a)>0:
#     print('elementi mavjud')
# else:
#     print('element mavjud emas')

# 11.Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
# Y = (1,2,3,44,5,6,7,10,11,12,13,14,10,10,12,'m')
# x = input()
# for i in range(len(Y)):
#     if int(x in Y ) == 1 and Y[Y.index(x)] == Y[i]:
#         print(i)
#     elif int(x in Y ) == 0:
        
#         if int(int(x) in Y) == 1 and Y[Y.index(int(x))] == Y[i]:
#             print(i)
#             if int(int(x) in Y) == 0:
#                 print('mavjud emas')

# 12.Find Second Largest: From a given tuple, find the second largest element.
# 13.Find Second Smallest: From a given tuple, find the second smallest element.
# a = (1,3,44,33,3,5,877,44,1,1,877,0,0)
# a = set(a)
# a = list(a)
# a[a.index(max(a))] = min(a)
# print(max(a))   
# a[a.index(min(a))] = max(a)
# print(min(a))

# 14.Create a Single Element Tuple: Create a tuple that contains a single specified element.
# x = input()
# a = ()
# if x == int():
#     print(a + (int(x)))
# else:
#     print(tuple(x))

# 15.Convert List to Tuple: Given a list, create a tuple containing the same elements.
# a = [1,3,44,33,3,5,877,44,1,1,877,0,0]
# a = tuple(a)
# print(a)

# 16.Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
# a = (1,2,3,4,5,7,7,8)
# b = 0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i > j and a[i]>= a[j]:
#             b +=1
#         else:
#             b +=0
            
# if b == len(a) * (len(a)-1)/2:
#     print(True)
# else:
#     print(False)

# 17.Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
# 18.Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
# a = (1,2,3,44,5,6,7,11,12,13,14,10,10,12)
# starting_index = int(input())
# ending_index = int(input())
# print(max(a[starting_index:ending_index]))
# print(min(a[starting_index:ending_index]))

# 19.Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# Y = (1,2,3,44,5,6,7,10,11,12,13,14,10,10,12,'m')
# Y = list(Y)
# x = input()
# for i in range(len(Y)):
#     if int(x in Y ) == 1:
#         Y.remove(x)
#         print(tuple(Y))
#     elif int(x in Y ) == 0:
        
#         if int(int(x) in Y) == 1:
#             Y.remove(int(x))
#             print(tuple(Y))
#     else: 
#         print('mavjud emas')

# 20.Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# a = (1,2,3,44,5,6,7,10,11,12,13,14,10,10,12)
# m = list()
# x = int(input())
# t = len(a)%x
# if len(a)%x == 0:
#     for i in range(len(a)):
#         if (i+1)%x == 0:
#             m+=[(a[i+1-x:i+1])]
# else:
#     for i in range(len(a)):
#         if (i+1)%x == 0:
#             m+=[(a[i+1-x:i+1])]
#     m +=[(a[len(a)-t:])]

# print(tuple(m))

# 21.Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# a = (1,2,3,44,5,6,7,11,12,13,14,10,10,12)
# m = ()
# n = int(input())
# for i in range(1,n+1):
#     m +=a
# print(m)

# 22.Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# a = (1,2,3,44,5,6,7,10,11,12,13,14,10,10,12)
# x = int(input())
# y = int(input())
# b = a[x:y+1:1]
# print(b)

# 23.Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
# a = (1,2,3,44,5,6,7,10,11,12,13,14,10,10,12)
# print(a[::-1])

# 24.Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# a = (1,2,3,44,5,6,7,10,11,12,13,14,10,10,12)
# a2 = a[-1::-1]
# c = bool(a == a2 )
# if c==1:
#     print("palindrom")
# else:
#     print("palindrom emas")

# 25.Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
# a = [0,1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# n = []
# m = []
# for i in range(len(a)):
#     if a[i] in n:
#         m+=[a[i]]
#     else:
#         n+=[a[i]]
# print(tuple(n))







