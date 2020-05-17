fileName = input("Paste file name here")

with open(fileName) as inputFile:
    data = inputFile.readlines()
    inputFile.close()

for i, line in enumerate(data):
    searchPhrase1 = input("what phrase are you looking for?")
    if searchPhrase1 in line:
        return line
