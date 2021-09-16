import time
import calendar

def printTime():
    localtime = time.asctime(time.localtime(time.time()))
    print("Local current time :" + localtime)

def printCalendar():
    cal = calendar.month(2008, 1)
    print("Here is the calendar :" + cal)

