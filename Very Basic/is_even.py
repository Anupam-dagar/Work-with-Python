#check if the number is even or not.
def is_even(x):
    if x % 2 == 0:
        return "Yes, it is an even number."
    else:
        return "No, it is not an even number."
number = int(raw_input("enter a number:"))
answer = is_even(number)
print answer