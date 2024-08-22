def check_list(l1):
    for l in l1:
        if type(l) is list:
            check_list(l)
        else:
            l2.append(l)


x = [1, 2, 3, [1, [[2, 4, 5], 6, 7], 7, 8, [1, 2, 34]]]
global l2
l2 = []
check_list(x)
print(l2)
