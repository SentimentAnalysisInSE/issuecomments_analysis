import sys
import re
import csv
from sklearn import metrics

def Kappa(filename):
    watsonlabels = []
    google20Labeles = []
    google25Labeles = []
    MicrosoftLabeles = []
    awsLabels = []
    manuelLabel = []


    with open(filename, newline='') as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')

        for row in FileText:
            manuelLabel.append(row[0].split(",")[8])
            awsLabels.append(row[0].split(",")[10])
            watsonlabels.append(row[0].split(",")[2])
            google25Labeles.append(row[0].split(",")[5])
            google20Labeles.append(row[0].split(",")[6])
            MicrosoftLabeles.append(row[0].split(",")[7])

    csvfile.close()       
    print("Microsoft v Google")
    print(metrics.cohen_kappa_score(MicrosoftLabeles, google20Labeles))
    #print(metrics.cohen_kappa_score(MicrosoftLabeles,manuelLabel, None, 'linear', [[0,1,2],[1,0,1],[2,1,0]]))
    print()
    print("Microsoft v Watson")
    print(metrics.cohen_kappa_score(MicrosoftLabeles, watsonlabels))
    # print(metrics.cohen_kappa_score(MicrosoftLabeles,manuelLabel, None, 'linear', [[0,1,2],[1,0,1],[2,1,0]]))
    print()
    print("Microsoft v aws")
    print(metrics.cohen_kappa_score(MicrosoftLabeles, awsLabels))
    # print(metrics.cohen_kappa_score(MicrosoftLabeles,manuelLabel, None, 'linear', [[0,1,2],[1,0,1],[2,1,0]]))
    print()
    print("Google20 v Watson")
    print(metrics.cohen_kappa_score(google20Labeles,watsonlabels))
    print()
    print("Google20 v aws")
    print(metrics.cohen_kappa_score(google20Labeles, awsLabels))
    print()
    print("Google25")
    print(metrics.cohen_kappa_score(google25Labeles,manuelLabel))
    print()
    print("Watson v aws")
    print(metrics.cohen_kappa_score(watsonlabels, awsLabels))
    print()
    print("aws")
    print(metrics.cohen_kappa_score(awsLabels, manuelLabel))
    print()



def main():
    Kappa("parsable.csv")


if __name__ == '__main__':
    main()