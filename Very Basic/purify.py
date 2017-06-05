#program to remove all odd numbers from the list.
def purify(inlst):
    new_lst = []
    for item in inlst:
        if (item % 2) == 0:
            new_lst.append(item)
    return new_lst
my_list = []
number = input("how many numbers you want to insert in list:")
for num in range(0,number):
	scan_number = input("enter number to be inserted in list:")
	my_list.append(scan_number)
answer = purify(my_list)
print answer	