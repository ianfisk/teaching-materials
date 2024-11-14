import random

# Look at how we can easily compose utility functions in unique ways within
# business logic functions that complete common business tasks. Why might
# we use many functions?
#    - Code reuse
#    - Implementation detail abstraction (hide implementation details that the
#        whole program shouldn't "know" about)
#    - Code health, ease of refactoring.
#    - Give meaningful names to some code
#    - Testability
#    - Stub out business logic, fill in details later
#    - Functional composition

# Real life utility libraries:
#    - Google's SafeValues: https://github.com/google/safevalues
#    - Faithlife Utility: https://github.com/Faithlife/FaithlifeUtility/tree/master
#    - Lodash: https://www.npmjs.com/search?q=keywords:lodash-modularized
#    - ... so many


# Utility functions:
SUPER_SECRET_ID_PREFIX = 'superSecretIdPrefix'
def get_employee_id(firstName, lastName):
	# Only get_employee_id and find_employee_by_id need to be aware of the ID's
	# format and the fact the ID really contains the employee's name.
	return f"{SUPER_SECRET_ID_PREFIX}{firstName}*{lastName}"

def find_employee_by_id(id):
	# Parse the employee's name which is hidden in their ID.
	idWithoutPrefix = id.replace(SUPER_SECRET_ID_PREFIX, '')
	return idWithoutPrefix.split('*')

def get_lunch_group():
	# For now, this is random. BUT that might change and it's easier to refactor
	# if this logic is only here.
	random.randint(1, 5)

def get_greeting(firstName, lastName):
	raise Exception('Not implemented')

# Business logic functions:
# 2) So we need to fill in an onboard_employee function. What would we need to
#    tell the new employee? You can write this whole function by calling
#    yet-to-be-implemented functions stubs...
def onboard_employee(firstName, lastName):
	print(get_greeting(firstName, lastName))
	print(f"We've assigned you to lunch group: {get_lunch_group()}")
	print(f"Your employee ID is: {get_employee_id(firstName, lastName)}")
	print("Enjoy your time working on the ALGORITHM.")

# 3) Then imagine we need to pay the employee. What would be some possible
#    steps in that task? Again, we can stub out this implementation and
#    then fill in the other functions after we see the logical structure.
def pay_employee(employeeId):
	amountPaid = transfer_money_to_employee(employeeId)
	send_employee_payday_confirmation(employeeId, amountPaid)

def transfer_money_to_employee(employeeId):
	# Probably do more things here in the real implementation...
	amountPaid = random.randint(1, 10000)
	return amountPaid

def send_employee_payday_confirmation(employeeId, amountPaid):
	firstName, lastName = find_employee_by_id(employeeId)
	print(get_greeting(firstName, lastName))
	print(f"This is a confirmation of your pay for this period. It is a total of ${amountPaid}")
	print("Sincerely,\nManagement")

# 1) This is what we ultimately want our program to do: onboard and pay a new
#    employee.
onboard_employee('Ian', 'Fisk')
pay_employee(get_employee_id('Ian', 'Fisk'))
