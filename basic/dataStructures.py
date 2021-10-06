import collections


# list example
from basic.Stack import Stack


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
    del list


# tuple example
def tulpe():
    # A tuple is a collection which is ordered and unchangeable.
    mytuple = ("apple", "banana", "cherry")
    print(mytuple)
    print(type(mytuple))

    for x in mytuple:
        print(x)
    del mytuple


# simple example
def array():
    cars = ["Ford", "Volvo", "BMW"]

    for x in cars:
        print(x)
    cars[1] = "Mazda"

    for x in cars:
        print(x)
    del cars


# two dimensional array example
def twoDimensionalarray():
    numbers = [1, 2, 3], [4, 5, 6], [7, 8, 9]
    print(numbers[1], [2])
    del numbers


# map example
def map():
    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}

    res = collections.ChainMap(dict1, dict2)
    print('Keys = {}', res.keys())
    print('Values = {}', res.values())
    print(res.get("day3"))
    res['day6'] = "saturday"
    print(res.get("day6"))
    # update value
    res.update({'day2': 'Tuesday'})
    print(res.get("day2"))
    # delete
    print('before delete day6')
    print(res)
    del res['day6']
    print(res)
    del res


def setExperience():
    Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    Days.remove("Tue")
    Months = {"Jan", "Feb", "Mar"}
    Months.remove("Mar")
    Dates = {21, 22, 17}
    Dates.add(21)
    Dates.add(55)
    # print(Days)
    # print(Months)
    # print(Dates)
    Days.discard("Sun")  # other way of delete
    # for d in Days:
    #     print(d)

    # Intersection of Sets
    DaysA = set(["Mon", "Tue", "Wed"])
    DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
    AllDays = DaysA & DaysB
    print(AllDays)

def stack():
    stack = Stack()
    stack.add("Mon")
    stack.add("Tue")
    stack.peek()
    print(stack.peek())
    print(stack.size())
    stack.add("Wed")
    stack.add("Thu")
    print(stack.peek())
    print(stack.size())


def deque():
    DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
    DoubleEnded.append("Thu")

    print("Appended at right - ")
    print(DoubleEnded)

    DoubleEnded.appendleft("Sun")
    print("Appended at right at left is - ")
    print(DoubleEnded)

    DoubleEnded.pop()
    print("Deleting from right - ")
    print(DoubleEnded)

    DoubleEnded.popleft()
    print("Deleting from left - ")
    print(DoubleEnded)