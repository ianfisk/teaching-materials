# How might we make this function easier to understand?
# SIDE NOTE: There is a problem with a symbol name here. Can you find it?
def can_ride_many_conditions(age, height):
    is_too_young_or_old = age < 18 or age >= 80
    is_too_short_or_tall = height <= 60 or height >= 84

    return not (is_too_young_or_old or is_too_short_or_tall)
