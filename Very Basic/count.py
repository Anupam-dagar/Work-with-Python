#count no. of occurence of an item in dictionary
def count(sequence,item):
    count = 0
    for items in sequence:
        if items == item:
            count += 1
    return count
dictionary = {} #enter you dictionary
search = " " #enter key to count in dictionary
answer = count(dictionary, search)
print answer