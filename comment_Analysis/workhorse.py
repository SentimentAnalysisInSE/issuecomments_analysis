import sys
import re
import csv


def Anylize(filename):
    Watsonneutral = 0
    Google25neutral = 0
    Google2neutral = 0
    Microsoftneutral = 0
    MFalseNeutral = 0
    GFalseNeutral = 0
    G2FalseNeutral = 0
    WFalseNeutral = 0

    Watsonpositive = 0
    Google25Positive = 0
    Google2Positive = 0
    MicrosoftPositive = 0
    WFalsePositive = 0
    MFalsePositive = 0
    GFalsePositive = 0
    G2FalsePositive = 0

    
    WatsonNegitive = 0
    Google25Negitive = 0
    Google2Negitive = 0
    MicrosoftNegitve = 0
    WfalseNegative = 0
    MFalseNegative = 0
    GFalseNegative = 0
    G2FalseNegative = 0


    error = 0
    Watsonmismatch = 0
    Googlemismatch = 0
    Google2mismatch = 0
    Microsoftmismatch = 0
    total = 0

    GoogleWatsonComp = 0
    with open(filename, newline='') as csvfile:
        FileText = csv.reader(csvfile, delimiter='\n')

        for row in FileText:
            manuelLabel = row[0].split(",")[8]
            watsonContents = row[0].split(",")[2]
            google25Contents = row[0].split(",")[5]
            google20Contents = row[0].split(",")[6]
            microsoftContents = row[0].split(",")[7]
            total += 1

            if (watsonContents == "neutral"):
                Watsonneutral += 1
                if(watsonContents != manuelLabel):
                    Watsonmismatch += 1
                    WFalseNeutral += 1
            elif (watsonContents == "positive"):
                Watsonpositive += 1
                if(watsonContents != manuelLabel):
                    Watsonmismatch += 1
                    WFalsePositive += 1
            elif (watsonContents == "negative"):
                WatsonNegitive += 1
                if(watsonContents != manuelLabel):
                    Watsonmismatch += 1
                    WfalseNegative += 1
            elif (watsonContents == "NA"):
                error += 1

            if (google25Contents == "neutral"):
                Google25neutral += 1
                if(google25Contents != manuelLabel):
                    Googlemismatch += 1
                    GFalseNeutral +=1
            elif (google25Contents == "positive"):
                Google25Positive += 1
                if(google25Contents != manuelLabel):
                    Googlemismatch += 1
                    GFalsePositive +=1
            elif (google25Contents == "negative"):
                Google25Negitive += 1
                if(google25Contents != manuelLabel):
                    Googlemismatch += 1
                    GFalseNegative += 1
            
            if (google20Contents == "neutral"):
                Google2neutral += 1
                if(google20Contents != manuelLabel):
                    Google2mismatch += 1
                    G2FalseNeutral +=1
            elif (google20Contents == "positive"):
                Google2Positive += 1
                if(google20Contents != manuelLabel):
                    Google2mismatch += 1
                    G2FalsePositive +=1
            elif (google20Contents == "negative"):
                Google2Negitive += 1
                if(google20Contents != manuelLabel):
                    Google2mismatch += 1
                    G2FalseNegative += 1

            if (microsoftContents == "neutral"):
                Microsoftneutral += 1
                if(microsoftContents != manuelLabel):
                    Microsoftmismatch += 1
                    MFalseNeutral += 1
            elif (microsoftContents == "positive"):
                MicrosoftPositive += 1
                if(microsoftContents != manuelLabel):
                    Microsoftmismatch += 1
                    MFalsePositive += 1
            elif (microsoftContents == "negative"):
                MicrosoftNegitve += 1
                if(microsoftContents != manuelLabel):
                    Microsoftmismatch += 1
                    MFalseNegative += 1












            if(google25Contents != watsonContents):
                GoogleWatsonComp += 1
        csvfile.close()

        writer = open("anylized.csv", 'w')
        writer.write(
            "WatsonPositive,WatsonNeutral,WatsonNegative,WatsonMismatch, false Positive,false neutral,false negative, Total\n")
        writer.write(str(Watsonpositive) + "," + str(Watsonneutral) + "," +
                     str(WatsonNegitive)+","+str(Watsonmismatch)+","+str(WFalsePositive)+","+str(WFalseNeutral)+","+str(WfalseNegative)+ ","+str(total)+"\n\n\n")

        writer.write(
            "GooglePositive,GoogleNeutral,GoogleNegative,GoogleMismatch, false Positive,false neutral,false negative, Total\n")
        writer.write(str(Google25Positive) + "," + str(Google25neutral) + "," + str(Google25Negitive)+","+
                     str(Googlemismatch)+","+
                     str(GFalsePositive)+","+str(GFalseNeutral)+","+ str(GFalseNegative)+","+
                     str(total)+"\n")
        writer.write(
            "comparison between google and watson, mismatch: "+str(GoogleWatsonComp)+"\n\n\n\n")

        writer.write(
            "Google2Positive,Google2Neutral,Google2Negative, Google2Mismatch, false Positive,false neutral,false negative, Total\n")
        writer.write(str(Google2Positive) + "," + str(Google2neutral) + "," +str(Google2Negitive)+","+str(Google2mismatch)+","+
                     str(G2FalsePositive)+","+str(G2FalseNeutral)+","+str(G2FalseNegative)+","+str(total)+"\n\n\n\n\n")

        writer.write(
            "Microsoft Positive,Neutral,Negative, Mismatch, false Positive,false neutral,false negative, Total\n")
        writer.write(str(MicrosoftPositive) + "," + str(Microsoftneutral) + "," +str(MicrosoftNegitve)+","+str(Microsoftmismatch)+","+
                     str(MFalsePositive)+","+str(MFalseNeutral)+","+str(MFalseNegative)+","+str(total)+"\n")
                    
        


def main():
    Anylize("parsable.csv")


if __name__ == '__main__':
    main()
