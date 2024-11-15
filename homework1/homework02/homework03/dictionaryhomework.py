# 1.Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.

# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "brand" in y.keys():
#     print(y.get("brand"))
#     print("element mavjud")
# else:
#     print('element mavjud emas')

# 3.Count Keys: Determine the number of keys in the dictionary.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(len(y.keys()))

# 4.Get All Keys: Create a list that contains all the keys in the dictionary.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(list(y.keys()))

# 5.Get All Values: Create a list that contains all the values in the dictionary.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(list(y.values()))

# 6.Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = {
#   "brend": "BMW",
#   "modal": "Ferrari",
#   "yili": 1965
# }
# x.update(y)
# # z = dict()
# # z.keys() = list(y.keys) + list(y.keys)
# # z.values = list(y.values) + list(x.values)
# print(x)

# 7.Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# y = list(y)
# y.remove('brand')
# print(y)

# 8.Clear Dictionary: Create a new empty dictionary.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# y.clear()

# 9.Check if Dictionary is Empty: Determine if a dictionary has any elements.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if len(y) == 0:
#     print('emplty')
# else:
#     print('not empty')

# 10.Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(y["brand"])

# 11.Update Value: Given a dictionary, update the value for a specified key.
# y = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# y['brand']='nimadir'
# print(y["brand"])

# 12.Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
# y = {
#   "brand": "Ford",
#   "Nimadir": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(list(y.values()).count("Ford"))

# 13.Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
# y = {'a': 1, 'b': 2, 'c': 3 ,'d':1}
# n = {}
# m = []
# keys = list(y.keys())
# values = list(y.values())
# for j in range(len(y)):
#     for i in range(len(y)):
#         if values[i] not in n:
#             n[values[i]] = keys[i]
#         else:
        
#             n[values[i]] =keys[i]

# print(n)

# 14.Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value.
# y = {'a': 1, 'b': 2, 'c': 3 , 'd':1}
# n = []
# given_value = 1
# keys = list(y.keys())
# values = list(y.values())
# for i in range(len(y)):
#     if y[keys[i]] == given_value:
#         n+=[keys[i]]

# print(n)

# 15.Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# y1 = ['a' , 'b' , 'c' ,'d']
# y2 = [1 , 2 , 3 , 4, 5]
# n = {}
# for i in range(len(y1) -1):
#     n[y1[i]] = y2[i]
#     n[y1[len(y1)-1]] = y2[(len(y1)-1):]
# print(n)

# 16.Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
# y = {'a': {'a': 1, 'b': 2, 'c': 3 , 'd':1}, 'b': 2, 'c': 3 , 'd':1}
# k = list(y.values())
# for i in range(len(y)):
#     if type(k[i]) == type(y) :
#         print('bor')

# 17.Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# y = {'a': {'a': 1, 'b': 2, 'c': 3 , 'd':1}, 'b': 2, 'c': 3 , 'd':1}
# k = list(y.values())
# for i in range(len(y)):
#     if type(k[i]) == type(y) :
#         print(list((k[i]).values())[0])

# 18.Create Default Dictionary: Create a dictionary that provides a default value for missing keys.
# y = {'a': 1, 'b': 2, 'c': 3 , 'd':1}
# k = list(y.keys())
# x = input()
# if x not in k:
#     print('unday obyekt yo\'q')
# else:
#     print(list(y.values())[k.index(x)])

# 19.Count Unique Values: Given a dictionary, determine the number of unique values it contains.
# y = {'a': 1, 'b': 2, 'c': 3 , 'd':1}
# k = list(y.values())
# n = []
# for i in range(len(k)):
#     if k.index(k[i]) + k[-1::-1].index(k[i]) == len(k) - 1:
#         n+=[k[i]]
# print(n)
# print(len(n))

# 20.Sort Dictionary by Key: Create a new dictionary sorted by keys.
# 21.Sort Dictionary by Value: Create a new dictionary sorted by values.
# y = {'a': 1, 'b': 2, 'c': 3 , 'd':1}
# k1 = list(y.keys())
# k2 = list(y.values())
# print(k2)
# t1 = sorted(k1)
# t2 = sorted(k2)
# t3 = []
# n = {}
# m = {}
# for i in range(len(y)):
#     n[t1[i]] = y[t1[i]]
#     m[k1[k2.index(t2[i])]] = t2[i]
# print(n)
# print(m)

# 22.Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# y = {'a': 1, 'b': 2, 'c': 3 , 'd':1}
# k1 = list(y.keys())
# k2 = list(y.values())
# m = {}
# for i in range(len(y)):
#     if k2[i] > 2:
        
#         m[k1[i]] = k2[i]
# print(m)

# 23.Check for Common Keys: Given two dictionaries, check if they have any keys in common.
# x = {'m': 1, 'k': 2, 's': 3 , 'n':1}
# y = {'a': 1, 'b': 2, 'c': 3 , 'd':1}
# m = 0
# k1 = list(y.keys())
# k2 = list(x.keys())
# for i in range(len(x)):
#     for j in range(len(y)):
#         if k1[j] in k2 or k2[i] in k1:
#             m += 1
            
# if m>0:
#     print('they have common keys')
# else:
#     print('they do not have coomon keys')

# 24.Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.
# y = (('a',2) , ('b',4) , ('c',6) , ('d',8) , ('e',10))
# m = {}
# for i in range(len(y)):
#     m[y[i][0]] = y[i][1]

# print(m)

# 25.Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
y = {'a': 1, 'b': 2, 'c': 3 , 'd':1}
k1 = list(y.keys())
k2 = list(y.values())
m = {}
m[k1[0]] = k2[0]
print(m)
        






















