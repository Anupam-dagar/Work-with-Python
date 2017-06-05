def count(sequence,item):
    count = 0
    for items in sequence:
        if items == item:
            count += 1
    return count
