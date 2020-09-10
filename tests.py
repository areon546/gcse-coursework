import csv

def loadAir():
    """makes the file into a 2d list with stopping points at ','/ commas"""

    airports = []

    with open('Airports.txt') as csvFile:
        spamReader = csv.reader(csvFile, delimiter=',') # todo WHY SPAM READER???
        # spamREader is essentially the whiole text, the line creates a 2d list seperated by the line end and the
        # inner lists are seperated by the delimiter

        print(', '.join(spamReader))


        for row in spamReader:  #
            print(', '.join(row)) #prints row from file
            airports.append(row)
    return airports

maxCap = 500
numFirstClass = 100


numStandClass = maxCap - (2 * numFirstClass)

print(numStandClass)
