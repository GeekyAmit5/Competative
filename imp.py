

# Trick #1
# Reversing a string in Python
# >>> a =  "codementor"
# >>> print "Reverse is",a[::-1]
# Reverse is rotnemedoc

# Trick #2
# Transposing a Matrix
# >>> mat = [[1, 2, 3], [4, 5, 6]]
# >>> zip(*mat)
# [(1, 4), (2, 5), (3, 6)]
# Trick #3
# a = [1,2,3]
# Store all three values of the list in 3 new variables
# >>> a = [1, 2, 3]
# >>> x, y, z = a
# >>> x
# 1
# >>> y
# 2
# >>> z
# 3
# Trick #4
# a = ["Code", "mentor", "Python", "Developer"]
# Create a single string from all the elements in list above.
# >>> print " ".join(a)
# Code mentor Python Developer
# Trick #5
# List 1 = ['a', 'b', 'c', 'd']
# List 2 = ['p', 'q', 'r', 's']
# Write a Python code to print
# ap
# bq
# cr
# ds
# >>> for x, y in zip(list1,list2):
# ...    print x, y
# ...
# a p
# b q
# c r
# d s
# Trick #6
# Swap two numbers with one line of code.
# >>> a=7
# >>> b=5
# >>> b, a =a, b
# >>> a
# 5
# >>> b
# 7
# Trick #7
# Print "codecodecodecode mentormentormentormentormentor" without using loops
# >>> print "code"*4+' '+"mentor"*5
# codecodecodecode mentormentormentormentormentor
# Trick #8
# a = [[1, 2], [3, 4], [5, 6]]
# Convert it to a single list without using any loops.
# Output:- [1, 2, 3, 4, 5, 6]
# >>> import itertools
# >>> list(itertools.chain.from_iterable(a))
# [1, 2, 3, 4, 5, 6]
# Trick #9
# Checking if two words are anagrams
# def is_anagram(word1, word2):
#     """Checks whether the words are anagrams.
#     word1: string
#     word2: string
#     returns: boolean
#     """
# Complete the above method to find if two words are anagrams.

# from collections import Counter
# def is_anagram(str1, str2):
#      return Counter(str1) == Counter(str2)
# >>> is_anagram('abcd','dbca')
# True
# >>> is_anagram('abcd','dbaa')
# False
# Trick #10.
# Taking a string input.
# For example "1 2 3 4" and return [1, 2, 3, 4]

# Remember list being returned has integers in it.
# Don't use more than one line of code.

# >>> result = map(lambda x:int(x) ,raw_input().split())
# 1 2 3 4
# >>> result
# [1, 2, 3, 4]

# x = 10 if (y == 9) else 20
# Likewise, we can do the same for class objects.

# x = (classA if y == 1 else classB)(param1, param2)
# In the above example, classA and classB are two classes and one of the class constructors would get called.

# Below is one more example with a no. of conditions joining to evaluate the smallest number.

# def small(a, b, c):
# 	return a if a <= b and a <= c else (b if b <= a and b <= c else c)

# print(small(1, 0, 1))
# print(small(1, 2, 2))
# print(small(2, 2, 3))
# print(small(5, 4, 3))

# #Output
# #0 #1 #2 #3

import more_itertools
import functools
Tips  # 8. Dictionary/Set comprehensions.
Like we use list comprehensions, we can also use dictionary/set comprehensions. They are simple to use and just as effective. Here is an example.

testDict = {i: i * i for i in xrange(10)}
testSet = {i * 2 for i in xrange(10)}

print(testSet)
print(testDict)

#set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


Tips  # 19. Unpack function arguments using the splat operator.
The splat operator offers an artistic way to unpack arguments lists. Please refer the below example for clarity.


def test(x, y, z):
    print(x, y, z)


testDict = {'x': 1, 'y': 2, 'z': 3}
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

# 1-> x y z
# 2-> 1 2 3
# 3-> 10 20 30

result = (lambda k: functools.reduce(int.__mul__, range(1, k+1), 1))(3)
print(result)

# -> 6


Tips  # 27. Create a dictionary from two related sequences.
t1 = (1, 2, 3)
t2 = (10, 20, 30)

print(dict(zip(t1, t2)))

# -> {1: 10, 2: 20, 3: 30}
TOC

Tips  # 28. In line search for multiple prefixes in a string.
print("http://www.google.com".startswith(("http://", "https://")))
print("http://www.google.co.uk".endswith((".com", ".co.uk")))

# 1-> True
# 2-> True


test = [[-1, -2], [1, 2, 3, [4, (5, [6, 7])]], (30, 40), [25, 35]]

print(list(more_itertools.collapse(test)))

# Output=> [-1, -2, 1, 2, 3, 4, 5, 6, 7, 30, 40, 25, 35]


def xswitch(x):
    return xswitch._system_dict.get(x, None)


xswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2}

print(xswitch('default'))
print(xswitch('devices'))

# 1-> None
# 2-> 2
