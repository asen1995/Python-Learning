def printtime():
    cal = calendar.month(2008, 1)
    print("Here is the calendar :" + cal)


def printCalendar():
    localtime = time.asctime(time.localtime(time.time()))
    print("Local current time :" + localtime)

