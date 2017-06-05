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
