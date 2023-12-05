#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listdivs = []
    for i in my_list:9
        if (i % 2) == 0:
            listdivs.append(True)
        else:
            listdivs.append(False)
    return listdivs
