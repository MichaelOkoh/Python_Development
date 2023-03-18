#Concatenation:
# concatenation is the joining of two or more data types together
# in other to form a sentence or to give a certain output.

# Data types:  variable, strings, int and random numbers.

#Types of concatenations:

# Variables + Variables concatenation:
#variable       #assignment        #strings
Word1               =              'python '
word2               =              'bootcamp'

print(Word1 + word2)# varable + variable concatenation

#variable + strings concatenation:
data1 = 'welcome'
print('you are ' + data1) #strings + variable concatenation

#strings + strings concatenation"
print('my name is ' + 'Michael') #string + string concatenation

#variable + interger concatenation:
print(Word1 + str (23)) #variables + integer concatenation

#strings + inegers concatenation:
print('Michael' + str(1820)) # strings + integer concatenation

#integers + integers concatenation

print (str (23) + str (24)) #integer + integer concatenation


#FORMATTING:
# (): Bracket
# []: square Bracket
# {}: Curly Brackets
# <> : Angle Brackets

# converting uppercase to lower case using .lower()
data2 = 'DATA SCIENCE'
print ('PYTHON'.lower()) #converting uppercase to lower case
print (data2.lower()) # converting uppercas to lower case


# converting lowercase to upper case using .upper()
print ( 'michael'.upper())


#Removing a space before and after a string using .strip()
print('  what is your name?'.strip()) #removing a space before a string

# removing a space after a string using .strip()
print('michael        '.strip()+ 'oche') #removing a space after a string


# getting a maximum numbers using max()
values = [33,45,32,70,97,202]
print(max(values)) #finding maximum number using max()

print(min(values)) # finding minimum number using min()





