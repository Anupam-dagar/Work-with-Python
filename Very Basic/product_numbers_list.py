#program to find product of numbers in a list.
def product(integers):
    result = 1
    for integer in integers:
        result = result * integer
    return result
my_list = [] #enter your list.
number = int(raw_input("how many numbers you want to insert in list:"))
for num in range(0,number):
	input_number  = input("enter number to be inserted in list:")
	my_list.append(input_number)
answer = product(my_list)
print answer