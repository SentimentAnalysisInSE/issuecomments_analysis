import sys
import re
import csv
def Anylize(filename):
    Watsonneutral = 0
    Googleneutral =0
    Watsonpositive = 0
    GooglePositive=0
    WatsonNegitive = 0
    GoogleNegitive = 0
    error = 0
    Watsonmismatch = 0
    Googlemismatch = 0
    total = 0

    GoogleWatsonComp=0
    with open( filename , newline='') as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')
        
        for row in FileText:
            manuelLabel = row[0].split(",")[6]
            watsonContents = row[0].split(",")[2]
            googleContents = row[0].split(",")[5]
            total +=1
            if (watsonContents == "neutral"):
                Watsonneutral += 1
            elif (watsonContents == "positive"):
                Watsonpositive += 1
            elif (watsonContents == "negative"):
                WatsonNegitive +=1
            elif (watsonContents == "NA"):
                error += 1
            if(watsonContents != manuelLabel):
                Watsonmismatch +=1

            if (googleContents == "neutral"):
                Googleneutral += 1
            elif (googleContents == "positive"):
                GooglePositive += 1
            elif (googleContents == "negative"):
                GoogleNegitive +=1
            if(googleContents != manuelLabel):
                Googlemismatch +=1

            if(googleContents != watsonContents):
                GoogleWatsonComp +=1
        


        csvfile.close()  

        writer = open("anylized.csv", 'w')
        writer.write("WatsonPositive,WatsonNeutral,WatsonNegative,WatsonMismatch,Total\n")
        writer.write(str(Watsonpositive) +"," + str(Watsonneutral) +","+str(WatsonNegitive)+","+str(Watsonmismatch)+","+str(total)+"\n\n\n")

        writer.write("GooglePositive,GoogleNeutral,GoogleNegative,GoogleMismatch,Total\n")
        writer.write(str(GooglePositive) +"," + str(Googleneutral) +","+str(GoogleNegitive)+","+str(Googlemismatch)+","+str(total)+"\n")
        writer.write("comparison between google and watson, mismatch: "+str(GoogleWatsonComp))


def main():
    Anylize("parsable.csv")


if __name__ == '__main__':
  main()