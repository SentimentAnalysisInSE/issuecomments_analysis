import sys
import re
import csv


def Analyze(filename):
    mismatch = 0
    filename = './rest30.csv'

    with open(filename, newline='', encoding="ISO-8859-1") as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')

        for row in FileText:
            manualLabel = row[0].split(",")[2]
            contents = row[0].split(",")[4]
            if (contents.lower() != manualLabel.lower()):
                mismatch += 1


        csvfile.close()

    print(mismatch - 1)


def main():
    Analyze("AWSparsable.csv")


if __name__ == '__main__':
    main()