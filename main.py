import filemanagement.DataPrinter as dp
import exception.exceptionExample as exceptionExample
import filemanagement.FileManager as fileManager
from model.Employee import Employee

import webapi.webApiManager as webApiManager

import model.timestamps as timestampFunctions
import strings.strings as Stringutils
import basic.dataStructures as dataStructures


def main():
    # dp.printme("str")
    #
    # PRINT LIST NUMBERS
    # listOfNumbers = ['2', '5', '7', '37', '67', '46', '745', '732', '734', '756']
    # dp.printFullList(listOfNumbers)
    # dp.printListFromTo(listOfNumbers, 3, 8)

    # File function

    # fileManager.writeIntoFile("asen.txt","content to write and read after that")
    # #fileManager.deleteFile("asen.txt")
    # fileManager.readFile("asen.txt")
    # fileManager.renameFile("renamed.txt","asen.txt")
    # fileManager.updateFileAddLine("asen.txt", "sentence one more")

    # inheritance
    # emp = Employee("Asen", 2000000)
    # emp.displayCount()
    # emp.displayEmployee()

    # webApiManager.callWebApi()
    #
    # timestampFunctions.printTime()
    # timestampFunctions.printCalendar()

    # pythonSentence = "Python Programming!"
    # Stringutils.printSubstring(pythonSentence,0,6)
    # Stringutils.printSubstring(pythonSentence, 6, 12)
    #
    # list7 = [1, 2, 3, 4, 5, 6, 7];
    # listIndexToIndex = list7[0:4]
    # print(listIndexToIndex)
    #
    # for i in list7:
    #     if i % 2 == 0:
    #         print(i , " is even")
    #     else:
    #         print(i , " is odd")

    # count = 0
    # while (count < 9):
    #     print('The count is:', count)
    #     count = count + 1

    #     datastructures

    # dataStructures.list()
    # dataStructures.tulpe()
    # dataStructures.array()
    # dataStructures.twoDimensionalarray()
    # dataStructures.map()
    # dataStructures.setExperience()
    # dataStructures.stack()
    dataStructures.deque()

main()
