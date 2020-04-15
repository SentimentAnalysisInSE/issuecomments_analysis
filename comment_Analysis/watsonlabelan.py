import sys
import re
import csv
def Anylize(filename):
    neutral = 0
    positive = 0
    negative = 0
    error = 0
    mismatch = 0
    with open( filename , newline='') as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')
        
        for row in FileText:
            manuelLabel = row[0].split(",")[6]
            contents = row[0].split(",")[2]
            if (contents == "neutral"):
                neutral += 1
            elif (contents == "positive"):
                positive += 1
            elif (contents == "negative"):
                negative +=1
            elif (contents == "NA"):
                error += 1
            else: print(contents)
            if(contents != manuelLabel):
                mismatch +=1


        csvfile.close()  

        writer = open("anylized.csv", 'w')
        writer.write("Positive,Neutral,Negative,Mismatch\n")
        writer.write(str(positive) +"," + str(neutral) +","+str(negative)+","+str(mismatch))


def main():
    Anylize("parsable.csv")


if __name__ == '__main__':
  main()