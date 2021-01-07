import csv
import numpy as np

def main():

    abs_file_path = "C:/Users/Richard/Desktop/filteredViralGenomes_eukaryotes.csv"
    with open(abs_file_path, newline='') as csvfile:
        totalData = list(csv.reader(csvfile))


    """accessions = list(np.array(totalData)[1:,1])
    accessionsSet = list(set(accessions))
    accessionsSet = set(accessionsSet[1:])
    print(len(accessionsSet))"""

    filteredData = []

    """for i in range(len(totalData)):
        if ((np.array(totalData)[i,1] in accessionsSet) and (np.array(totalData)[i,2] == 'complete')):
            filteredData.append(totalData[i])"""

    for i in range(len(totalData)):
        if np.array(totalData)[i,9] != 'land plants' and np.array(totalData)[i,9] !='fungi' and np.array(totalData)[i,9] !='protozoa':
            filteredData.append(totalData[i])


    #print(filteredData)
    myFile = open('/Users/Richard/Desktop/viralGenome_noPlants.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(filteredData)


main()