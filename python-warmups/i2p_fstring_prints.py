# Intro to Programming (2024 Q2)

####################################

# What if we want to accept a user's age, and print that out in sentence?
age = int(input('Please enter your age: '))
decades = age // 10 # integer division (throw away decimal part)

print('You are ' + str(age) + ' years old.')
print('You have been alive for ' + str(decades) + ' decades.\n')

####################################

# Updated with syntactic sugar...
print()
print()

# See https://realpython.com/python-string-formatting/ for more examples
