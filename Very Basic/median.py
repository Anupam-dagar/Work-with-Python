def median(lst):
    lst = sorted(lst)
    print lst
    length = len(lst)
    result = 0
    if length % 2 == 0:
        result = (lst[(length/2)-1] + lst[(length/2)])/2.0
        return result
    else:
        result = lst[(length/2)]
        return result
