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
