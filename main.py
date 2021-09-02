import filemanagement.DataPrinter as dp
import exception.exceptionExample as exceptionExample
import filemanagement.FileManager as fileManager
from model.Employee import Employee

def main():

    # dp.printme("str")
    #
    # PRINT LIST NUMBERS
    # listOfNumbers = ['2', '5', '7', '37', '67', '46', '745', '732', '734', '756']
    # dp.printFullList(listOfNumbers)
    # dp.printListFromTo(listOfNumbers, 3, 8)
    #
    # fileManager.writeIntoFile("asen.txt","content to write and read after that")
    # #fileManager.deleteFile("asen.txt")
    # fileManager.readFile("asen.txt")
    # fileManager.renameFile("renamed.txt","asen.txt")
    # fileManager.updateFileAddLine("asen.txt", "sentence one more")

    emp = Employee("Asen", 2000000)
    emp.displayCount()
    emp.displayEmployee()


main()

