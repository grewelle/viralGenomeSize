def main():

    scaffoldID = '>'

    filename = "C:/Users/Richard/Desktop/ViralSequences/caliciviridae.fna"

    numList = []
    sizeList = []

    with open(filename) as myFile:
        count = 0
        for num, line in enumerate(myFile, 1):
            if scaffoldID in line:
                sizeList.append(count)
                count = 0
                numList.append(line[1:12])

            else:
                count += len(line)-1

        sizeList.append(count)

        for j in range(len(numList)):
            print(numList[j], sizeList[j+1])

main()