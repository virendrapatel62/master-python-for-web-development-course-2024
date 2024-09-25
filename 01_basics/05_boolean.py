"""
A Boolean is a true/false, yes/no, one/zero value.
We can use it to make decisions.
In Python, True and False are keywords to represent these values.
"""
age = 19
are_you_18 = age == 18
are_you_19 = age == 19
is_over_18 = age > 18

print(are_you_18, (are_you_19))
print("Is Over 18", is_over_18)


are_you_human = True
are_you_man = True
are_you_animal = False

# True and True => True
# True and False => False
# False and True => False
# False and False => False


# True or True => True
# True or False => True
# False or True => True
# False or False => False

print(are_you_human and are_you_animal)
print(are_you_human or are_you_animal)
print(are_you_human and are_you_man)
print(are_you_human or are_you_man)
