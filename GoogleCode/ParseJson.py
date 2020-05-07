import json
jsonFile = open('parse.json', 'r')
f = open("magnitude.txt", "a")
values = json.load(jsonFile)
i=0

while i < 2100 :
    print(str(values[i]["documentSentiment"]["score"]))
    f.write(str(values[i]["documentSentiment"]["magnitude"])+"\n")
    i+=1

jsonFile.close()
f.close