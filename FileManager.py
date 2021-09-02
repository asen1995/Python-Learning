import os
import os.path as path


writemode: str = "w"

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