#program to remove duplicate number in list.
def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        count = 0
        for number in new_lst:
            if item == number:
                count += 1
        if count == 0:
            new_lst.append(item)
    return new_lst
my_list = []
number = input("how many numbers you want to insert in list:")
for num in range(0,number):
	scan_number = input("enter number to be inserted in list:")
	my_list.append(scan_number)
answer = remove_duplicates(my_list)
print answer	