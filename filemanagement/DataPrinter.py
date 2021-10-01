def printme(str):
    "This prints a passed string called str into this function"
    print(str)
    return;


def printFullList(thelist):
    "This prints a full list passed into this function"
    for element in thelist:
        print(element)


def printListFromTo(thelist, fromIndex, toIndex):
    "This prints list from index to index into this function"
    print(fromIndex, toIndex)
    print(list[fromIndex:toIndex])
