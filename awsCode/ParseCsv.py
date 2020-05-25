import sys
import re
import csv
from sklearn import metrics


def Analyze(filename):
    mismatch = -1
    truePositivesP = -1
    truePositivesNeg = -1
    truePositivesN = -1
    falsePositivesP = -1
    falsePositivesNeg = -1
    falsePositivesN = -1

    filename = './awsJira.csv'

    with open(filename, newline='', encoding="ISO-8859-1") as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')
        mLabels = []
        AwsLabels = []

        for row in FileText:
            manualLabel = row[0].split(",")[2].lower()
            contents = row[0].split(",")[4].lower()
            mLabels.append(manualLabel)
            AwsLabels.append(contents)


            if (contents!= manualLabel):
                mismatch += 1
                if (contents == "neutral"):
                    falsePositivesN += 1
                elif (contents == "positive"):
                    falsePositivesP += 1
                elif (contents == "negative"):
                    falsePositivesNeg += 1
            elif (contents == "neutral"):
                truePositivesN += 1
            elif (contents == "positive"):
                truePositivesP += 1
            elif (contents == "negative"):
                truePositivesNeg += 1


        csvfile.close()
    print(mismatch)
    print(str(truePositivesP) + '\n' +
    str(truePositivesNeg) + '\n' +
    str(truePositivesN) + '\n' +
    str(falsePositivesP) + '\n' +
    str(falsePositivesNeg) + '\n' +
    str(falsePositivesN) + '\n')

    print("COHENKAPPPPPAAAAAA\n\n")
    print(metrics.cohen_kappa_score(AwsLabels,mLabels))




def main():
    Analyze("AWSparsable.csv")


if __name__ == '__main__':
    main()