def purify(inlst):
    new_lst = []
    for item in inlst:
        if (item % 2) == 0:
            new_lst.append(item)
    return new_lst
