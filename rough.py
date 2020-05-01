lst = [1,2,3,4,5,6]
for e in lst:
    if isinstance(e, list) is True:
        for i in e:
            print(i, end=" ")
        print()
    else:
        print(e, end=" ")
