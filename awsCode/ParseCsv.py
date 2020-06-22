import sys
import re
import csv
import pandas as pd
from sklearn import metrics

mismatch = 0
truePositivesP = 0
truePositivesNeg = 0
truePositivesN = 0
falsePositivesP = 0
falsePositivesNeg = 0
falsePositivesN = 0
mLabels = []
AwsLabels = []

def evalLabels(data):
    global mismatch
    global truePositivesP
    global truePositivesNeg
    global truePositivesN
    global falsePositivesP
    global falsePositivesNeg
    global falsePositivesN
    global mLabels
    global AwsLabels
    manualLabel = data['label'].lower()
    contents = data['AWS Labels'].lower()
    mLabels.append(manualLabel)
    AwsLabels.append(contents)

    if (contents != manualLabel):
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

def Analyze(filename):
    filename = '../comment_Analysis/stackAWS.csv'

    with open(filename, newline='', encoding="ISO-8859-1") as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')
        df = pd.read_csv(filename, encoding="ISO-8859-1", dtype='str')
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df[['label', 'AWS Labels']]    #change to zero

        df.apply(evalLabels, axis=1)
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