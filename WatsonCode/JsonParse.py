import json
jsonFile = open('output.json', 'r')
values = json.load(jsonFile)
i=0

while i < 605 :
    print(values[i]["sentiment"]["document"]["label"])
    i+=1

jsonFile.close()
