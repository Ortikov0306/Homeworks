# 1.Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
# 2.Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
# 3.Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# s2 = {1, 3, 44, 33, 3, 5, 877, 44, 1, 1, 877, 0, 0}
# print(s1|s2, '\n', s1&s2, '\n', s1 -s2)

# 4.Check Subset: Given two sets, check if one set is a subset of the other.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# s2 = {1, 3, 44, 33, 3, 5, 877, 44, 1, 1, 877, 0, 0}
# if s1&s2==s1 or s1&s2==s2:
#     print(True)
# else:
#     print(False)

# 5.Check Element: Given a set and an element, check if the element exists in the set.
# listdagi bilan bir xil:x in s1

# 6.Set Length: Determine the number of unique elements in a set.
# listdagai bilan bir xil:len(s1)

# 7.Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.
# a = [1,2,3,4,'n','dhafhfkhk',True,21]
# a = set(a)
# print(a)

# 8.Remove Element: Given a set and an element, remove the element if it exists.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# s1.remove(12)
# print(s1)

# 9.Clear Set: Create a new empty set from an existing set.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# s1.clear()
# print(s1)

# 10.Check if Set is Empty: Determine if a set has any elements.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# if len(s1) == 0:
#     print('Empty')
# else:
#     print('not empty')

# 11.Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# s2 = {1, 3, 44, 33, 3, 5, 877, 44, 1, 1, 877, 0, 0}
# print((s1|s2) - (s1&s2))

# 12.Add Element: Given a set and an element, add the element to the set if it is not already present.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# s1.add(99)
# print(s1)

# 13.Pop Element: Given a set, remove and return an arbitrary element from the set.
# s = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2}
# print(s.pop())

# 14.Find Maximum: From a given set of numbers, find the maximum element.
# 15.Find Minimum: From a given set of numbers, find the minimum element.
# Listdagi bilan bir xil:print(min(s)) and print(max(s))

# 16.Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.
# 17.Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.
# s = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2}
# a = list(s)
# m = []
# n = []
# for i in range(len(a)):
#     if a[i]%2 == 1:
#         m+=[a[i]]
#     else:
#         n += [a[i]]

# print(set(m), "toq sonlar")
# print(set(n) , "juft sonlar")

# 18.Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).
# s = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2}
# a = list(s)
# x = int(input())
# y = int(input())
# b = a[x:y+1:1]
# print(set(b))

# 19.Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.
# s1 = [12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1]
# s2 = [1, 3, 44, 33, 3, 5, 877, 44, 1, 1, 877, 0, 0]
# s3 = s1 + s2
# print(set(s3))

# 20.Check Disjoint Sets: Given two sets, check if they have no elements in common.
# s1 = {12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1}
# s2 = {1, 3, 44, 33, 3, 5, 877, 44, 1, 1, 877, 0, 0}
# s3 = s1&s2
# if len(list(s3)) == 0:
#     print('no common elements')
# else:
#     print('there is at least one common element')

# 21.Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.
# s = [12, 10, 10, 14, 13, 12, 11, 10, 7, 6, 5, 44, 3, 2, 1]
# s = set(s)
# print(list(s))

# 22.Get Unique Elements in Order: Given a list, create a set that contains unique elements while maintaining their first appearance order.
# a = [0,1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# n = []
# m = []
# for i in range(len(a)):
#     if a[i] in n:
#         m+=[a[i]]
#     else:
#         n+=[a[i]]
# print(set(n))

# 23.Create Nested Sets: Create a set of sets, where each inner set contains a specified number of unique elements.
# s = {1,2,3,44,5,6,7,10,11,12,13,14,10,10,12}
# a = list(s)
# m = []
# k = {}
# x = int(input())
# t = len(a)%x
# if len(a)%x == 0:
#     for i in range(len(a)):
#         if (i+1)%x == 0: 
#             m+=[set(a[i+1-x:i+1])]
# else:
#     for i in range(len(a)):
#         if (i+1)%x == 0:
#             m+=[set(a[i+1-x:i+1])]
#     m +=[set(a[len(a)-t:])]

# print(m)

# 24.Count Unique Elements: Given a list, determine the count of unique elements using a set.
# a = [0,1,2,3,44,5,6,7,10,11,12,13,14,10,10,12]
# m = 0
# for i in range(len(a)):
#         for j in range(len(a)):
#             i!=j and a[i] == a[j]
# m+=1
# print(len(list(set(a))) - m)

# 25.Generate Random Set: Create a set with a specified number of random integers within a certain range.
# s = {1,2,3,44,5,6,7,10,11,12,13,14,10,10,12}
# s = list(s)
# a = int(input())
# m = []
# import random
# s1 = list(random.sample(range(0,len(s) - 1), a))
# for i in range(len(s1)):
#     m +=[s[s1[i]]]

# print(set(m))







































