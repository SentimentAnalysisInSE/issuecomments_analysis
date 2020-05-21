import sys
import re
import csv
from sklearn import metrics

def Kappa(filename):
    watsonlabels = []
    google20Labeles = []
    google25Labeles = []
    MicrosoftLabeles = []
    manuelLabel = []


    with open(filename, newline='') as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')

        for row in FileText:
            manuelLabel.append(row[0].split(",")[8])
            watsonlabels.append(row[0].split(",")[2])
            google25Labeles.append(row[0].split(",")[5])
            google20Labeles.append(row[0].split(",")[6])
            MicrosoftLabeles.append(row[0].split(",")[7])

    csvfile.close()       
    print("Microsoft")
    print(metrics.cohen_kappa_score(MicrosoftLabeles,manuelLabel))
    print()
    print("Google20")
    print(metrics.cohen_kappa_score(google20Labeles,manuelLabel))
    print()
    print("Google25")
    print(metrics.cohen_kappa_score(google25Labeles,manuelLabel))
    print()
    print("Watson")
    print(metrics.cohen_kappa_score(watsonlabels,manuelLabel))
    print()



def main():
    Kappa("parsable.csv")


if __name__ == '__main__':
    main()