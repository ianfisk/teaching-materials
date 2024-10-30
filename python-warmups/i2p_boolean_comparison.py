def is_even_bad(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_even(num):
    return num % 2 == 0


# Similar mistake
def is_old_enough(age):
    is_adult = age >= 18
    return is_adult == True

# How would we write is_old_enough correctly?
