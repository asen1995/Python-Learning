import os
import os.path as path


writemode: str = "w"
readmode: str = "r"


def writeIntoFile(filename,content):
    try:
        fh = open(filename, writemode)
        fh.write(content)
    except IOError:
        print("Error: can\'t write to file " + filename)
    else:
        print( "Written content in the file " + filename + " successfully")
        fh.close()


def deleteFile(filename):

    if path.exists(filename):
        os.remove(filename)
        print( filename + " removed")
    else:
        print( filename + " don't exists")


def readFile(filename):

    if path.exists(filename):
        file1 = open(filename, readmode)
        print("Output of Readlines after appending")
        print(file1.readlines())
        file1.close()
    else:
        print( filename + " don't exists")



def renameFile(filename,newfilename):

    if path.exists(filename):
        os.rename(filename,newfilename)
    else:
        print( filename + " don't exists")
