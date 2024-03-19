# a,b,c = 9, 8, 7, 8
# print(a, b,c)

# a, b=c=7, 8
# print(a)
# print(b)
# print(c)

# a=b, c = 4, 2
# print(a, b, c)

# ----> swapping of variable
a = 7
b = 5
Eg:1
#temp=a #temp=7
#a=b     #a=5
#b=temp  #b=7

# a=5, b=7
print(a, b)

Eg:2
a=a+b 
b=a-b 
a=a-b 

print(a, b)

a=a*b #a=35
b=a/b #b=35/7 = 5.0
a=a/b #a=35/5 = 7.0
print(int(a), int(b))

# id() --> used to find the memory address of the variable
a = 7
b = 8
print(id(a))
print(id(b))

# -----> Keywords
#Keywords are reserved words which provides special meaning to
#compiler interpretor
#import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))

# To check if the string is keyword or not
# print(keyword.is keyword("sid"))# False

# if = 8
# print(if) # error coz if is a keyword

# !-----> Literals
# Literal is the constant value asssigned  to variable
# A variable is consider to be constant when it is defines
# in caps

# a = 78 # is variable
# A = 78 # A is constant

n1 = 89 + 7j
print(hash(n1))


f1 = [7, 8, 9]
print(hash(f1))# error

a = 9
b = 9
b = 90
# print(id(a))
# print(id(b))

#! ----> Operators
# ? Opertors are symbols which is used to perform various operations
# ? between 2 or more operands

# Arithmatic
# Assignment
# Logical
# Relational or comparison
# Bitwise
# Identity
# Membership

#todo -----> Arithmatic  --> +, -, *, /, %, //, **
# Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c)

# input() --> used to get the runtime input
# eval() --> used to get the runtime values of all datatype
n1 =  eval(input(" Enter the value: "))
print(type(n1))

a = 4
b = 2
print(a/b) # is used to get the quotient value
print(a%a) # is used to get the remainder value
 
# ! // ---> floor devision

a = 765433
b = 19
# print(a//b) # ->  the output will be inn integer & the output will be
# based on floor value

#! ** --> used for power of a number
# print(2**4) # --> 16

# ! Assignment --> +-=, -=, *=, //=, **=, &=, |=

# a = 8
# a+=2
# print(a)

# a=30
# a-=5
#print(a)
# ! Comparison --> ==, >, <, !=, <=, >=
a = 8
b = 7
print(a>b)

a = 9
b = 5
print(a==b)
# ! Bitwise operator --> &, |, ^, ~, <<, >>
a = 7
b = 4
print(a&b)

# 2^4 2^3 2^2 2^1 2^0
# 8   4     2   1

# 0   1     1    1    # --> 7
# 0   1     0    0    # --> 4 &
# ------------------------
# 0    1     0     0
# AND
# A  B  A&B
# 0  0  0
# 0  1  0
# 1  0  0
# 1  1  1
# a = 9876
# print(~a)


# a = 9

# 128 64 32 16 8 4 2 1
#  0   0  0  0  1 0 0 1 # -->9

# 256 128 64 32 16 8 4 2 1
# 0    0   0  0  0  0 1 0 1    3<
# 0    0    0  1 0  1  0 0 0  -->40
#107

# <<,>>
# print(5>>1)
# 16>4

# ! Logical --> used to compare the expressions
# and ,or ,not
#a = 6
# print(a>3 and a>10)
# print(a>7 or <30)
# print(not(a<8 and a>10))

#! Identity operator
# ? are stored
# is, is not
# a = 8
# b = 8
 #print(a is b)
 #print(a==b)

 #a = [1, 2, 3]
 #b = [1, 2, 3]
 #print(a is b)
#a = [1, 2, 3]
 # b = [1, 2, 3]
 #print(a is not b)

# ! Membership operator
# in, not in

# l1 = [7,8,9,0,6,5]
# num = 55
# print(num in l1)
# print(num not in l1)

# num = 678
# print(8 in num) # error

# ! Conditional statement
# if , elif , else

# Eg:1
# --> C syntax
#if (condition){
#    statement;
#    statement;
#    statement;
#}
# Python syntax
# if condition:
#    statement
#    statement
#    statement
# statement

# Eg:1
# a = 6
# if a:
#     print("hello")
# Eg2:
#a = 6
#if a>3:
#    print("yes")
#else:
#    print("no")
    
#Eg:3
#if 7>8:
#    print("hello")


# print("no")

Eg:4
a = 0
 #a = None
 #a = False
 #a = ""
if a:
    print("yes")
#    else:
#        print("no")

     #number is even or odd
n = int(input("enter the number: "))
if n %2==0:
    print(n, "is even")
else:
    print(n, "is odd")

  
