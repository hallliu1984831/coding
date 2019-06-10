fileName = 'a.txt'
try:
    with open(fileName) as fileObj:
        content = fileObj.read()
        print(content.rstrip())
except FileNotFoundError:
    print("No file found:" + fileName + ", create that file with default content")
    with open(fileName, 'w') as writeFileObj:
        writeFileObj.write("create new file.\n")
        writeFileObj.write("create second line. \n")
