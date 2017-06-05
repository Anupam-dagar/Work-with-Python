#check if prime or not.
def is_prime(x):
    if (x < 2):
        return "No, it is not a Prime Number."
    if x == 2:
        return "Yes, it is a Prime number."
    for n in range(2,x-1):
        if x % n == 0:
            return "No, it is not a Prime number."
    else:
        return True
number = input("enter a number:")
answer = is_prime(number)
print answer