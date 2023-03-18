
# 1. concatenate your first name as string and your sun name as a variable?
# 2. concatinate your first name as variable and any number of your choice as integer?
# 3. demostrate the use of .upper(), .lower(), .capitalize() and .strip()
# 4. demostrate the use of max() and min()?


#Answers:
#concatenation:
# variable + string concatenation

data1 = 'michael'
print('Okoh ' + data1)


# variables + int concatenation
data1 = '100'
print('Michael' + data1) #concatenation of variable + int
print('Michael' + str(100))


#convertion of lower case to uppercase using .upper()
Course = 'bootcamp'
print(Course .upper())
print('python' .upper())


#convertion of upper case to lower case using .lower()
data2 = 'MICHAEL'
print(data2 .lower())
print('OKOH' .lower())

#convertion of lower case to capital using .capitalize()
data3 = 'great men are great thinkers'
print(data3 .capitalize())


# removing of space before and after a string using .strip()
print('    How old are you?'.strip())

print('I am 10 years     ' .strip()+ ' old')


# How to get maximium & minimium number from a set of numbers using max() and Min()

Numbers = [10,20,30,40,50,60,70,80,90,100]
print(max(Numbers))

print(min(Numbers))







