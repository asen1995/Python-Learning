def list():
    list = ["apple", "banana", "cherry"]
    print(list)
    print("len is ", len(list))
    print(type(list))
    list.append("orange")
    print(list)
    list.insert(0, "Asen")
    print(list)
    list.remove("Asen")
    print(list)


def tulpe():
    # A tuple is a collection which is ordered and unchangeable.
    mytuple = ("apple", "banana", "cherry")
    print(mytuple)
    print(type(mytuple))

    for x in mytuple:
        print(x)


def array():
    cars = ["Ford", "Volvo", "BMW"]

    for x in cars:
        print(x)
    cars[1] = "Mazda"

    for x in cars:
        print(x)


def twoDimensionalarray():
    numbers = [1,2,3],[4,5,6],[7,8,9]
    print(numbers[1],[2])