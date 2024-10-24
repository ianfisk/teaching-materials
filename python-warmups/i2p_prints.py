# Intro to Programming (2024 Q2)

####################################

# String concatenation with + operator
my_string = "Hello, world"
another_string = 'String with single quotes.'

print(my_string + '. ' + another_string)
print()

####################################

# What if we want to accept a user's age, and print that out in sentence?
age = int(input('Please enter your age: '))
decades = age // 10 # Integer division (throw away decimal part)

print('You are ' + age + ' years old.')
print('You have been alive for ' + decades + ' decades.\n')
