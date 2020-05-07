f = open("setiments.txt")
allLines = f.readlines()
f.close()
for line in allLines:
    checker = line.split(" ")
    if "Overall" not in checker:
        if "positive\n" in checker:
            print("positive")
        elif "neutral\n" in checker:
            print("neutral")
        elif "negative\n" in checker:
            print("negative")
        elif "mixed\n" in checker:
            print("neutral") 
#redirect putput to desired file