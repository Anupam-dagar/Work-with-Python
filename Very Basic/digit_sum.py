#calculate sum of digits in an integer
def digit_sum(n):
    result = 0
    while n > 0:
        result = result + (n % 10)
        n = n / 10
    return result
number = int(raw_input("enter a number:"))
answer = digit_sum(number)
print answer