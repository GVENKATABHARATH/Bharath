
# ! -----> common function for list


l1 = [6, 7, 8, 9, 0]
print(len(l1))

print(max(l1))
print(min(l1))

l1 = [6, 8, 9, "p", "u"]
# print(max(l1)) # ----> error coz its a combination of int and string
# print(min(l1)) # ----> error coz its a combination of int and string

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# print(min(l1)) # -5

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index ()  ---> to get index value of specific element
# print(l1.index(9))

l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count() --> how many num of times an element is repeated
# print(l1.count(6))

# ! some functions which is specifically used for list

# To add elelment inside list
# ? Insert(index_value, element)
l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1.insert(2, "car")
print(l1)

# ? to delete element from list
l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
#pop()
l1.pop()
print(l1)
# pop(index_value)
l1.pop(4)
print(l1)

# * remove(element) ---> used to delete element directly
l1.remove(8.89)
print(l1)

#* clear() ----> complete delete all element in list
l1.clear()
print(l1)

# del --> to delete
#del l1
print(l1)

# ? ----> join 2 list

l1 = [9, 0, 8]
l2 = ["p", "o", "t", 34]
print(l1+l2)

# or
# exetend() --> to combine 2 list
l1.extend(l2)
print(l1)

# ? -----> copy()
l1 = [6, 7, 8, 9, 3]
l2 = l1.copy
print(l2)
print(l1)

print(id(l1))
print(id(l2))

# ! diff between shallow copy and deep copy
# shallo copy
import copy

l1 = [8, 9, 0, [5, 6],[3, 2, 1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

# * deep copy
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
print(l1[-1][1])

l2 = copy.deepcopy(l1)
l1.append('cars')
print(l1)
print(l2)

# ? sort ---> arrange elements in list in ascending or descending order
l1 = [9, 7, 45, 0, -6, 5, 12]
l1.sort()
print(l1)

l1.sort(reverse=True) 
print(l1)

l1 = ['z', 'i', 'o', 'p', 9]
#l1.sort()
print(l1)

# list constructor
#list() ---> to convert other collection data type to list
l3 = ((8, 9, 0))
print(list(l3))

# ! ---> nested list

l1 = [8, 9, [0, 8, 7], ["p", "o", 'y'], [8, 't']]
print(l1[-2][1])

print(l1[1:4])
print(l1[1:-1])

# ? to delete "t" from l1
l1[-1].remove('t')
print(l1)

# ? combine these ["p", "o", 'y'],[8, 't'] lists in l1 to ["p", "o", 'y',8, 't']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

# ! ------> Tuple
# * char of tuple

# 1.) Tuple have to be sourrund by ()
# 2.) the elements inside tuple are not chargable
# 3.) The elements inside tuple are indexed
# 4.) The elements will execute in order
# 5.) It is heterogenous
# 6.) It allow duplicate elements

# * eg:1
t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "hey", 9+6j)
print(t1)
print(type(t1))

# ? Indexing, slicing are all same as list

l1 = (8)
print(type(l1)) # int

l1 = 8,9
print(type(t1)) # tuple
t2= 8,
print(type(t2)) # tuple

# len(), min(), max(), index(), count() ----> all the same as list
# cannot delete any element from tuple

#join 2 tuples
t1 = (8, 9 , 0)
t2 = (6, 7, 8)
print(t1+t2)
# To add all element inside list
#sum()
l1 = [8, 9, 7, 6]
print(sum(l1))

# *sort tuple
t1 = (8,9,0,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse = True)))

l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)

# * Iteration based on index value
l1 = [9,8,0,6,5,8,56]
for i  in range(0,len(l1)):
    print(l1[i])

print(l1[i])

# ! ----->strimg
s1 = 'o'
print(type(s1))

s1 = "u"
print (type(s1))

s1 = "hello world"
# to access string
print(s1)
# indexing and slicing ---->same as list and tuple

print(s1[0:5])

# ----> common functions
#len(), min(), max(), index(),count()
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))

# ord() ----. used to find the ASCII value of a character
s1  = 'u'
print(ord(s1))

# function of atring
s1 = "hello world"
# ? to convert all characters to upper case
print(s1.upper())

# to cover to lower case
s1 = " HFREDGiou"
print(s1.lower())

# strip()  ---> to eliminate the space in beginning and end of string
s1 = "  Where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

#split() ---> to split the words in string based on a character

s1 = " Where are you?"
print(s1.split())
print(s1.split("r"))

print(s1.count('e'))

# *replace()----> to replace a specific char in the string
s1 = "Where are you?"
print((s1.replace)('r', '&&'))

# swapcase() ----> to convert capital to small and small to capital at a time
s1 = "HEY there"
print(s1.swapcase())

#* title()
s1 = 'never giveUP'
print(s1.title())

# capitalize() --> 1st char of string will be coverted to capital
s1 = 'never giveUP'
print(s1.capitalize())

# join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)

s1 = '''how are you
 i am fine
 hey there
 '''

# splitlines() ----> used to split the string based on lines
print(s1.splitlines())

# find()
s1 = "hello world"
print(s1.find('h'))
print(s1.index('o'))

#join() 
l1 = ["hey", "there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "Welcome to all"
print(s1. endswith('I'))
print(s1.startswith('W'))

s1 = "67"
print(type(s1))
print(s1.isdigit())

#print the string in reverse manner
s1 = "Welcome to all"
print(s1[::-1])


#  Eg:1
s1 = "HEY  there you aRE"
# wap to find of lower case letters
s1 = "HEY  there you aRE"
count = 0
for  i in s1:
    if i .islower():
        count+=1
        print(" The total num of lower case letter:",count)

#! ----> Eg:2 r---> "$"
s1 = 'restarter'
s1 = "IMAGIN"

fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst, "$")
print(fst+txt)

# ! ----> Eg3

s1 ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'sstandard dummy text ever since the 1500s, when an unknown printertook a galley of type and scrambled it to make a typespecimen book. It has survived not only five centuries,but also the leap into electronic typesetting, remaining essentiallyunchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recentlywith desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
chracters = len(s1)
print(chracters)

words = s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)

# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]























