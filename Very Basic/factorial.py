#calculate factoial of a number
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result = result * i
    return result
number = int(raw_input("enter a number:"))
answer = factorial(number)
print answer