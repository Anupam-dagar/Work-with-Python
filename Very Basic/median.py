#find median in an input list.
def median(lst):
    lst = sorted(lst)
    print "sorted list is:"
    print lst
    length = len(lst)
    result = 0
    if length % 2 == 0:
        result = (lst[(length/2)-1] + lst[(length/2)])/2.0
        return result
    else:
        result = lst[(length/2)]
        return result
my_list = [] #input list.
number = int(raw_input("how many numbers you want to insert in the string:"))
for num in range(0,number):
    scan_number = input("enter number to be inserted:")
    my_list.append(scan_number)
answer = median(my_list)
print answer