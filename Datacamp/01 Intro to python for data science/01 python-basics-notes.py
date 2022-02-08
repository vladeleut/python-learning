############
############ First Steps
############ 

#always use print() to show something:
from re import X


print(7+10)


#Basics: Addition, subtraction
print(5 + 5)
print(5 - 5)

#Basics: Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100*1.1**7)

#We can store values in variables. Python variables' names are case sensitive.
height = 1.75
weight = 79.0
height

BMI = weight / height ** 2
print(BMI)

#We can check the type of a value with type function:
type(BMI) #this is float value

day_of_week = 5 #this is int value

#types in python:
#float, int, string, booleans, 
str1 = 'This is a string' 
str2 = "This is also a string"

this_is_boolean_type = True

type(this_is_boolean_type)

#operators work differently for each data type. 
5 + 2 #adds values
'a' + 'b' #concatenates values

#we cannot simply sum strings and integers/floats:
day_of_week + 'a'
#but we can cast variables to other types of data:
str(day_of_week) + ' a'
#Similar functions such as int(), float() and bool() help us convert Python values into another type.

############
############ Lists
############ 

#We may need to work with many data points. For example, if we are going to collect the height of a group,
#it is inconvenient to create a new variable for each member. Instead, we can create a list:
list = [1.65, 1.68, 1.71, 1.80]

#we can have lists of lists:
list2 = [
    ['p1', 1.65],
    ['p2', 1.68],
    ['p3', 1.71],
    ['p4', 1.80]
]
print(list2)

#indexes are useful for accessing specific values from lists. They starts in 0 and can be negatives or in ranges. 
list3 = ['a','b','c','d','e','f','g','h']
list3[0]
list3[3:5] #WARNING! the 6th element is not included. "slicing"
list3[-1]

#to reference sublists we can use a second square bracket:
list2[2][1] #will return 1.71

#adding lists will extend them:
big_list = ['short', 'list'] + ['short', 'list']
print(big_list)

#to update or remove items, you can simply refer to the item you want to remove/edit:
del(big_list[2])
print(big_list)

#WARNING! 
#Lists are pointers in the memory. When you copy a list, you copy the reference to the place in the memory where it is stored.
#Then, if you update one list, you update the another one too:
x = ['a','b','c']
y = x
y[1] = 'z'
print(x)

#If you want to copy the values into a new list, you can explicitly copy each value or use the 'list' function:
y = x[:] #or 
y = list(x)
