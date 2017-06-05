#check if the number is integer or not.
def is_int(x):
    if (x - int(x)) > -1 and (x - int(x)) < 1 and (x - int(x)) != 0:
        return "No, it is not an integer."
    else:
        return "Yes, it is an integer."
number = input("enter a number:")
answer = is_int(number)
print answer