def is_int(x):
    if (x - int(x)) > -1 and (x - int(x)) < 1 and (x - int(x)) != 0:
        return False
    else:
        return True
