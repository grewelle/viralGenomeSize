import csv
import numpy as np
from matplotlib import pyplot as plt

def main():

    abs_file_path = "C:/Users/Richard/Desktop/genomeLists.csv"
    with open(abs_file_path, newline='') as csvfile:
        totalData = list(csv.reader(csvfile))


    #stderror1 = 4315.207953
    #stderror2 = 12595.1338

    #stderror1 = 693.3029923
    #stderror2 = 2492.524557

    #stderror1 = 226.7624853
    #stderror2 = 861.4092455

    #stderror1 = 188.4432734
    #stderror2 = 344.1210494

    stderror1 = 284.5622597
    stderror2 = 644.5031247

    group1 = list(np.array(totalData)[1:,8])
    group2 = list(np.array(totalData)[1:,9])
    group1 = list(filter(None, group1))
    group2 = list(filter(None, group2))
    numgroup1 = []
    numgroup2 = []
    for j in range(len(group1)):
        numgroup1.append(int(group1[j]))
    for k in range(len(group2)):
        numgroup2.append(int(group2[k]))
    print(max(numgroup2))
    min1 = min(numgroup1) - round(2*stderror1)
    min2 = min(numgroup2) - round(2*stderror2)
    max1 = max(numgroup1) + round(2*stderror1)
    max2 = max(numgroup2) + round(2*stderror2)

    if min1 < min2:
        mini = 100*(min1//100)
    else:
        mini = 100*(min2//100)

    if max1 > max2:
        maxi = 100*(max1//100)
    else:
        maxi = 100*(max2//100)

    summation1 = ''
    summation2 = ''




    for i in range(len(group1)):
        summation1 = summation1 + '+ np.exp(-((num-'+ str(group1[i]) + ')/stderror1)**2/2)/(stderror1*np.sqrt(2*np.pi))'


    for s in range(len(group2)):
        summation2 = summation2 + '+ np.exp(-((num -' + str(group2[s]) + ') / stderror2) ** 2 / 2) / (stderror2 * np.sqrt(2 * np.pi))'



    summation1 = '(' + summation1 + ')/' + str(len(group1))
    summation2 = '(' + summation2 + ')/' + str(len(group2))
    x = np.linspace(mini,maxi,(int((maxi-mini)/100)+1))
    solved1=[]
    solved2=[]
    under = np.zeros(len(x))
    for u in x:
        num = u
        solved1.append(eval(summation1))
        solved2.append(eval(summation2))


    figure = plt.figure(figsize=(20,5))
    plt.plot(x, solved1)
    plt.plot(x, solved2)

    plt.fill_between(x, under, solved1, facecolor='blue', alpha=0.5)
    plt.fill_between(x,under, solved2, facecolor='red', alpha=0.5)

    figure.savefig('group6.png')



    plt.show()









main()